import sys
import aocd
import math


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

# this is a big field ... to playin (probably a smarter way...)
rope_path = [[0] * 1000 for i in range(1000)]
start = [500, 500]
head_pos = start
tail_pos = start
rope_path[start[0]][start[1]] = 1


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


for line in data:
    dir, step = line.strip().split()
    step = int(step)

    if dir == "R":
        for i in range(step):
            head_pos = [head_pos[0], head_pos[1] + 1]
            new_tail_pos = move_tail(tail_pos, head_pos)
            if new_tail_pos != tail_pos:
                rope_path[new_tail_pos[0]][new_tail_pos[1]] = 1
                tail_pos = new_tail_pos

    elif dir == "L":
        for i in range(step):
            head_pos = [head_pos[0], head_pos[1] - 1]
            new_tail_pos = move_tail(tail_pos, head_pos)
            if new_tail_pos != tail_pos:
                rope_path[new_tail_pos[0]][new_tail_pos[1]] = 1
                tail_pos = new_tail_pos

    elif dir == "U":
        for i in range(step):
            head_pos = [head_pos[0] + 1, head_pos[1]]
            new_tail_pos = move_tail(tail_pos, head_pos)
            if new_tail_pos != tail_pos:
                try:
                    rope_path[new_tail_pos[0]][new_tail_pos[1]] = 1
                except:
                    print(head_pos)
                    print(new_tail_pos)
                    raise

                tail_pos = new_tail_pos
                tail_pos = new_tail_pos

    elif dir == "D":
        for i in range(step):
            head_pos = [head_pos[0] - 1, head_pos[1]]
            new_tail_pos = move_tail(tail_pos, head_pos)
            if new_tail_pos != tail_pos:
                rope_path[new_tail_pos[0]][new_tail_pos[1]] = 1
                tail_pos = new_tail_pos


rows = [sum(r) for r in rope_path]
submit(sum(rows), "a", 9, 2022)

head_pos = start
tail_pos = start
tails = [tail_pos for i in range(9)]
rope_path = [[0] * 1000 for i in range(1000)]
rope_path[start[0]][start[1]] = 1


for line in data:
    dir, step = line.strip().split()
    step = int(step)

    if dir == "R":
        for i in range(step):
            head_pos = [head_pos[0], head_pos[1] + 1]
            for i in range(len(tails)):
                if i == 0:
                    head = head_pos
                else:
                    head = tails[i - 1]
                new_pos = move_tail(tails[i], head)
                if i == 8:
                    if new_pos != tails[8]:
                        rope_path[new_pos[0]][new_pos[1]] = 1
                tails[i] = new_pos

    elif dir == "L":
        for i in range(step):
            head_pos = [head_pos[0], head_pos[1] - 1]
            for i in range(len(tails)):
                if i == 0:
                    head = head_pos
                else:
                    head = tails[i - 1]
                new_pos = move_tail(tails[i], head)
                if i == 8:
                    if new_pos != tails[8]:
                        rope_path[new_pos[0]][new_pos[1]] = 1
                tails[i] = new_pos

    elif dir == "U":
        for i in range(step):
            head_pos = [head_pos[0] + 1, head_pos[1]]
            for i in range(len(tails)):
                if i == 0:
                    head = head_pos
                else:
                    head = tails[i - 1]
                new_pos = move_tail(tails[i], head)
                if i == 8:
                    if new_pos != tails[8]:
                        rope_path[new_pos[0]][new_pos[1]] = 1
                tails[i] = new_pos

    elif dir == "D":
        for i in range(step):
            head_pos = [head_pos[0] - 1, head_pos[1]]
            for i in range(len(tails)):
                if i == 0:
                    head = head_pos
                else:
                    head = tails[i - 1]
                new_pos = move_tail(tails[i], head)
                if i == 8:
                    if new_pos != tails[8]:
                        rope_path[new_pos[0]][new_pos[1]] = 1
                tails[i] = new_pos

rows = [sum(r) for r in rope_path]
submit(sum(rows), "b", 9, 2022)
