import sys
import aocd
from collections import deque


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


class Elf:
    north = [(-1, -1), (0, -1), (1, -1)]
    south = [(-1, 1), (0, 1), (1, 1)]
    east = [(1, -1), (1, 0), (1, 1)]
    west = [(-1, -1), (-1, 0), (-1, 1)]

    def __init__(self, x, y):
        self.last_move = None
        self.dir = deque(["S", "W", "E", "N"])
        self.x = x
        self.y = y

    def neighbors(self, elves):
        north = [[-1, -1], [0, -1], [1, -1]]
        south = [[-1, 1], [0, 1], [1, 1]]
        east = [[1, -1], [1, 0], [1, 1]]
        west = [[-1, -1], [-1, 0], [-1, 1]]

        neighbors = set()
        for dx, dy in north + south + east + west:
            if elves.get((dx + self.x, dy + self.y)) is not None:
                neighbors.add((dx, dy))
        return neighbors


elves = dict()


def print_elves(elves):
    minx = min(p[0] for p in elves.keys())
    maxx = max(p[0] for p in elves.keys())
    miny = min(p[1] for p in elves.keys())
    maxy = max(p[1] for p in elves.keys())

    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            if elves.get((x, y)) is not None:
                print("#", end="")
            else:
                print(".", end="")
        print("")

    return (minx, maxx, miny, maxy)


for y, line in enumerate(data):
    line = line.strip()
    for x, c in enumerate(line):
        if c == "#":
            e = Elf(x, y)
            elves[(x, y)] = e


for _, elf in elves.items():
    print(f"elf: {elf.x} {elf.y}")
    print("--->", elf.neighbors(elves))
    print()


print_elves(elves)
