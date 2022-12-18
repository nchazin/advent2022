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

misses = 0
for cube in cubes:
    x, y, z = cube
    for diff in [+1, -1]:
        if (x + diff, y, z) not in cubes:
            misses += 1
        if (x, y + diff, z) not in cubes:
            misses += 1
        if (x, y, z + diff) not in cubes:
            misses += 1

submit(misses, "a", 18, 2022)
