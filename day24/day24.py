import sys
import aocd
from math import inf
from collections import defaultdict, deque


if len(sys.argv) > 2 and sys.argv[2] == "submit":
    SUBMIT = True
else:
    SUBMIT = False


def submit(val, part, day, year):
    if SUBMIT:
        aocd.submit(val, part=part, day=day, year=year)
    else:
        print(f"Not submiting {val} for 12/{day}/{year} part {part}")


with open(sys.argv[1]) as f:
    data = f.readlines()


blizzards = dict()
for r, line in enumerate(data):
    line = line.rstrip()
    for c, g in enumerate(line):
        match g:
            case ".":
                continue
            case _:
                blizzards[(c, r)] = [g]


def get_valley_size(blizzards):
    maxx = max(p[0] for p in blizzards.keys())
    maxy = max(p[1] for p in blizzards.keys())
    return maxx, maxy


def get_doors(blizzards):
    c, r = get_valley_size(blizzards)
    start, end = (None, None)
    for c in range(c + 1):
        if blizzards.get((c, 0)) is None:
            start = (c, 0)
        if blizzards.get((c, r)) is None:
            end = (c, r)
    return start, end


def print_valley(blizzards, elves):
    cols, rows = get_valley_size(blizzards)
    for r in range(rows + 1):
        for c in range(cols + 1):
            p = blizzards.get((c, r), ["."])
            if elves is not None and (c, r) == elves:
                assert p == ["."]
                p = ["E"]
            glyph = p[0] if len(p) == 1 else len(p)
            print(glyph, end="")
        print()
    print()


start, end = get_doors(blizzards)
c, r = get_valley_size(blizzards)

# print_valley(blizzards, start)

WALL = ["#"]


def walk(blizzards, start, end, c, r):
    pass


def crossblizzard(p, b, c, r):
    match b:
        case "<":
            nm = (c - 1, p[1])
        case ">":
            nm = (1, p[1])
        case "^":
            nm = (p[0], r - 1)
        case "v":
            nm = (p[0], 1)
        case _:
            raise Exception(p)

    return nm


def move_blizzrds(blizzards, c, r):
    next_blizzards = dict()
    moves = {">": (1, 0), "<": (-1, 0), "v": (0, 1), "^": (0, -1)}
    for p, blizzard in blizzards.items():
        if blizzard == WALL:
            next_blizzards[p] = WALL
        else:
            for b in blizzard:
                m = moves[b]
                nm = (p[0] + m[0], p[1] + m[1])
                if blizzards.get(nm) == WALL:
                    nm = crossblizzard(p, b, c, r)
                if nm not in next_blizzards:
                    next_blizzards[nm] = []
                next_blizzards[nm].append(b)

    return next_blizzards


def state(blizzards, elf):
    s = list()
    for c, v in blizzards.items():
        v.sort()
        s.append((c, tuple(v)))
    s.append(elf)
    return tuple(s)


def cross_valley(blizzards, tstates, c, r, start, goal, t):
    elves = start
    mint = inf
    end = goal
    moves = deque()
    tstates[0] = blizzards

    ELF_MOVES = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
    moves.append([t, start])
    visited = set()

    while len(moves) > 0:
        m, e = moves.popleft()
        s = (m, e)
        if m > mint:
            continue
        if s in visited:
            continue
        visited.add(s)

        if e == end:
            mint = min(mint, m)
        else:
            nm = m + 1
            if nm in tstates:
                nb = tstates[nm]
            else:
                nb = move_blizzrds(tstates[m], c, r)
                tstates[nm] = nb
            for em in ELF_MOVES:
                ne = (e[0] + em[0], e[1] + em[1])
                if ne not in nb and ne[1] > -1 and ne[1] < (r + 1):
                    if (m + 1, ne) not in visited:
                        moves.append([m + 1, ne])

    return mint


# The blizzards will repeat modulo something - find this cycle and we an index by
# modulo arithmetic - or not? TODO look into this later?
def get_tstates(blizzards, c, r):
    states = set()
    tstates = dict()
    nb = blizzards
    for i in range(700):
        tstates[i] = nb
        st = state(nb, (0, 0))
        if st in states:
            break
        states.add(st)
        nb = move_blizzrds(nb, c, r)
    return tstates


tstates = dict()
t = cross_valley(blizzards, tstates, c, r, start, end, 0)
submit(t, "a", 24, 2022)
t2 = cross_valley(blizzards, tstates, c, r, end, start, t)
t3 = cross_valley(blizzards, tstates, c, r, start, end, t2)
submit(t3, "b", 24, 2022)
