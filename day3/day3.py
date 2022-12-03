import sys


with open(sys.argv[1]) as f:
    data = f.readlines()


def make_compartments(items):
    mid = int(len(items) / 2)
    compartment1 = set(items[:mid])
    compartment2 = set(items[mid:])

    return [compartment1, compartment2]


def get_priority(item):
    if item > "Z":
        priority = ord(item) - ord("a") + 1
    else:
        priority = ord(item) - ord("A") + 27
    return priority


value = 0
for line in data:
    line = line.strip()
    c1, c2 = make_compartments(line)
    common = c1.intersection(c2).pop()
    value += get_priority(common)

print(value)

value = 0
for b in range(0, len(data), 3):
    b1 = set(data[b].strip())
    b2 = set(data[b + 1].strip())
    b3 = set(data[b + 2].strip())

    badge = b1.intersection(b2).intersection(b3).pop()
    value += get_priority(badge)

print(value)
