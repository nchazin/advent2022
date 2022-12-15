import sys
import aocd

from math import inf, floor

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
print(sys.argv)
if len(sys.argv) > 2:
    checkline = int(sys.argv[2])
else:
    checkline = 10

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


sweeps = set()
for sensor in sensors:
    based = sensor.md
    s = sensor.sensor
    straightd = abs(s[1] - checkline)
    w = based * 2 + 1
    w -= 2 * straightd
    if w > 0:
        w = floor(w / 2)
        for x in range(s[0] - w, s[0] + w + 1):
            sweeps.add((x, checkline))


for sensor in sensors:
    if sensor.beacon in sweeps:
        sweeps.remove(sensor.beacon)
submit(len(sweeps), "a", 15, 2022)
