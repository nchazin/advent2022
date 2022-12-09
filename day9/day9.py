import sys
import aocd
import math
from collections import defaultdict


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
    print(sys.argv[1])
    data = f.readlines()

rope_path = defaultdict(int)
start = [0, 0]
head_pos = start
tail_pos = start
rope_path[tuple(start)] = 1


def move_tail(tail_pos, head_pos):
    ti, tj = tail_pos
    hi, hj = head_pos

    # within 1 don't move
    if abs(ti - hi) > 1 or abs(tj - hj) > 1:
        if ti == hi:
            if tj > hj:
                tj -= 1
            else:
                tj += 1
        elif tj == hj:
            if ti > hi:
                ti -= 1
            else:
                ti += 1
        else:
            # move diagonal
            if tj > hj:
                tj -= 1
            elif tj < hj:
                tj += 1
            if ti > hi:
                ti -= 1
            else:
                ti += 1

    return [ti, tj]


def move_head(head_pos, dir):
    i, j = head_pos
    if dir == "U":
        i += 1
    elif dir == "D":
        i -= 1
    elif dir == "L":
        j -= 1
    elif dir == "R":
        j += 1
    return [i, j]


def solver(knots, data):
    rope_path = defaultdict(int)
    rope_path[tuple(knots[-1])] = 1

    for line in data:
        dir, step = line.strip().split()
        step = int(step)
        for _ in range(step):
            knots[0] = move_head(knots[0], dir)
            for i in range(1, len(knots)):
                knots[i] = move_tail(knots[i], knots[i - 1])
                if i == len(knots) - 1:
                    rope_path[tuple(knots[-1])] = 1

    return len(rope_path)


knots = [[0, 0], [0, 0]]
submit(solver(knots, data), "a", 9, 2022)


knots = [[0, 0] for i in range(10)]
submit(solver(knots, data), "b", 9, 2022)
