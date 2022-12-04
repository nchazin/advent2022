import sys

with open(sys.argv[1]) as f:
    data = f.readlines()

contained = 0

overlap = 0

for pairs in data:
    pairs = pairs.strip()
    sections = pairs.split(",")
    s1, f1 = map(int, sections[0].split("-"))
    s2, f2 = map(int, sections[1].split("-"))

    if (s1 >= s2 and f1 <= f2) or (s1 <= s2 and f1 >= f2):
        contained += 1

    if f1 >= s2 and s1 <= f2:
        overlap += 1

print(contained)
print(overlap)
