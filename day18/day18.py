import sys
import aocd


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


cubes = set()
for line in data:
    (x, y, z) = line.strip().split(",")
    cubes.add((int(x), int(y), int(z)))

misses = set()
miss_count = 0
for cube in cubes:
    x, y, z = cube
    for diff in [+1, -1]:
        if (x + diff, y, z) not in cubes:
            misses.add((x + diff, y, z))
            miss_count += 1
        if (x, y + diff, z) not in cubes:
            misses.add((x, y + diff, z))
            miss_count += 1
        if (x, y, z + diff) not in cubes:
            misses.add((x, y, z + diff))
            miss_count += 1

submit(miss_count, "a", 18, 2022)


minx = min(c[0] for c in cubes) - 1
maxx = max(c[0] for c in cubes) + 1
miny = min(c[0] for c in cubes) - 1
maxy = max(c[0] for c in cubes) + 1
minz = min(c[2] for c in cubes) - 1
maxz = max(c[2] for c in cubes) + 1

start = tuple([minx, miny, minz])
to_visit = [start]
outside_seen = set()


def neighbors(c):
    x, y, z = c
    for dx, dy, dz in [
        [1, 0, 0],
        [-1, 0, 0],
        [0, 1, 0],
        [0, -1, 0],
        [0, 0, 1],
        [0, 0, -1],
    ]:
        yield (x + dx, y + dy, z + dz)


while len(to_visit) > 0:
    cur = to_visit.pop()

    outside_seen.add(cur)
    for n in neighbors(cur):
        x, y, z = n
        if x < minx or x > maxx or y < miny or y > maxy or z < miny or z > maxz:
            continue
        if n in outside_seen or n in cubes:
            continue
        to_visit.append(n)

hits_count = 0
for cube in outside_seen:
    for neighbor in neighbors(cube):
        if neighbor in cubes:
            hits_count += 1

submit(hits_count, "b", 18, 2022)
