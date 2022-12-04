import sys

with open(sys.argv[1]) as f:
    data = f.readlines()

contained = 0


def make_sections(elf):
    s, f = elf.split("-")
    return set(range(int(s), int(f) + 1))


for pairs in data:
    pairs = pairs.strip()
    sections = pairs.split(",")
    assignments = [make_sections(s) for s in sections]
    common = assignments[0].intersection(assignments[1])
    if len(common) == min([len(a) for a in assignments]):
        contained += 1

print(contained)
