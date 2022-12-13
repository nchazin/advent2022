import sys
from functools import cmp_to_key

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
    data = f.read()


pairs = [
    [eval(p[0]), eval(p[1])]
    for p in [p.strip().split("\n") for p in data.split("\n\n")]
]


def compare(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return -1
        elif l > r:
            return 1
        else:
            return 0

    else:
        return compare_lists(l, r)


def compare_lists(l, r):
    if isinstance(l, int):
        l = [l]

    if isinstance(r, int):
        r = [r]

    for lp, rp in zip(l, r):
        if (c := compare(lp, rp)) != 0:
            return c

    if len(l) < len(r):
        return -1
    elif len(l) > len(r):
        return 1
    else:
        return 0


indices = [i + 1 for i, p in enumerate(pairs) if compare(p[0], p[1]) < 0]
submit(sum(indices), "a", 13, 2022)

markers = [[[2]], [[6]]]
packets = [item for pair in pairs for item in pair]

sorted_markers = sorted(packets + markers, key=cmp_to_key(compare))

product = 1
for marker in markers:
    product *= sorted_markers.index(marker) + 1

submit(product, "b", 13, 2022)
