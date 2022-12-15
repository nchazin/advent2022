import sys
import aocd

from collections import defaultdict

from math import inf

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

maxj = -inf


def make_cavern(data):
    global maxj
    cavern = defaultdict(str)
    for line in data:
        points = [p.split(",") for p in line.replace(" -> ", " ").strip().split(" ")]
        points = [[int(p1), int(p2)] for p1, p2 in points]
        for l in range(len(points) - 1):
            p1, p2 = points[l : l + 2]
            if p1[0] == p2[0]:
                i = p1[0]
                if p1[1] <= p2[1]:
                    j1 = p1[1]
                    j2 = p2[1]
                else:
                    j2 = p1[1]
                    j1 = p2[1]
                for j in range(j1, j2 + 1):
                    if j > maxj:
                        maxj = j
                    cavern[(i, j)] = "#"
            elif p1[1] == p2[1]:
                j = p1[1]
                if j > maxj:
                    maxj = j
                if p1[0] <= p2[0]:
                    i1 = p1[0]
                    i2 = p2[0]
                else:
                    i2 = p1[0]
                    i1 = p2[0]
                for i in range(i1, i2 + 1):
                    cavern[(i, j)] = "#"
            else:
                raise RuntimeError("oops:", p1, " and ", p2, "have no line")
    return cavern


cavern = make_cavern(data)

count = 0
while True:
    sandp = (500, 0)
    count += 1
    while sandp[1] < maxj:
        i, j = sandp
        if cavern[(i, j + 1)] == "":
            sandp = (i, j + 1)
        elif cavern[(i - 1, j + 1)] == "":
            sandp = (i - 1, j + 1)
        elif cavern[(i + 1, j + 1)] == "":
            sandp = (i + 1, j + 1)
        else:
            cavern[sandp] = "o"
            break
    if sandp[1] >= maxj:
        break

# Subtract one for going one too far
count -= 1
submit(count, "a", 14, 2022)


floor = maxj + 1
while True:
    sandp = (500, 0)
    count += 1
    if cavern[sandp] == "o":
        break
    while sandp[1] < maxj + 2:
        i, j = sandp
        if j == maxj + 1:
            cavern[(i, j)] = "o"
            break
        if cavern[(i, j + 1)] == "":
            sandp = (i, j + 1)
        elif cavern[(i - 1, j + 1)] == "":
            sandp = (i - 1, j + 1)
        elif cavern[(i + 1, j + 1)] == "":
            sandp = (i + 1, j + 1)
        else:
            cavern[sandp] = "o"
            break

# Subtract one for going one too far
submit(count - 1, "b", 14, 2022)
