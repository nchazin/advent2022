import sys
import aocd

from math import inf, floor
from functools import cmp_to_key

import re


if len(sys.argv) > 3 and sys.argv[3] == "submit":
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

if len(sys.argv) > 2:
    checkline = 2000000
    rows_to_check = 4000001
else:
    checkline = 10
    rows_to_check = 21

beacons = set()
sensors = set()


class Sensor:
    def __init__(self, sx, sy, bx, by):
        self.sx = int(sx)
        self.sy = int(sy)
        self.bx = int(bx)
        self.by = int(by)
        self.md = Sensor.manhattan(self.sensor, self.beacon)

    @staticmethod
    def manhattan(a, b):
        return sum(abs(val1 - val2) for val1, val2 in zip(a, b))

    def __repr__(self):
        return f"Sensor x:{self.sx} y:{self.sy} - Beacon x:{self.bx} y:{self.by}  MD {self.md}\n"

    @property
    def sensor(self):
        return (self.sx, self.sy)

    @property
    def beacon(self):
        return (self.bx, self.by)


sensors = list()
input_line = re.compile(
    r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
)
for line in data:
    result = input_line.match(line)
    v = result.groups()
    sensors.append(Sensor(*(result.groups())))


print(f"checking line {checkline}")


def merge(a, b):
    return (min(a[0], b[0]), max(a[1], b[1]))


def mergeable(a, b):
    return _mergeable(a, b) or _mergeable(b, a)


def _mergeable(a, b):
    return (a[0] >= b[0] and a[0] <= b[1]) or a[1] == b[0] - 1


def compare_sweeps(a, b):
    if a[0] < b[0]:
        return -1
    elif a[0] > b[0]:
        return 1
    else:
        return 0


def mergeall(sweeps):
    old_len = len(sweeps)
    new_len = 0
    while new_len != old_len:
        old_len = len(sweeps)
        newsweeps = set()
        sweepsl = sorted(list(sweeps), key=cmp_to_key(compare_sweeps))
        i = 0
        while i < len(sweepsl) - 1:
            a = sweepsl[i]
            b = sweepsl[i + 1]
            if mergeable(a, b):
                newsweep = merge(a, b)
                newsweeps.add(newsweep)
                i += 2
            else:
                newsweeps.add(a)
                i += 1
            if i == len(sweepsl) - 1:
                newsweeps.add(sweepsl[i])

        if len(newsweeps) > 0:
            sweeps = newsweeps
        new_len = len(sweeps)
    return sweeps


def sensor_sweep(checkline):
    sweeps = []
    for sensor in sensors:
        md = sensor.md
        s = sensor.sensor
        dy = abs(s[1] - checkline)
        if dy > md:
            continue
        dx = md - dy
        sweeps.append((s[0] - dx, s[0] + dx))
    sweeps.sort()
    minx, maxx = sweeps[0]
    for sweep in sweeps[1:]:
        if sweep[0] < minx - 1 and sweep[1] < minx - 1:
            print(minx - 1, ",", i)
            return minx - 1
        if sweep[0] > maxx + 1 and sweep[1] > maxx + 1:
            print(maxx + 1, ",", i)
            return maxx + 1
        minx = min(minx, sweep[0])
        maxx = max(maxx, sweep[1])
    return sweeps


sweeps = mergeall(sensor_sweep(checkline))


submit(sum(x[1] - x[0] for x in sweeps), "a", 15, 2022)

for i in range(rows_to_check):
    sweeps = sensor_sweep(i)
    if type(sweeps) != list:
        submit(sweeps * 4000000 + i, "b", 15, 2022)
        break
