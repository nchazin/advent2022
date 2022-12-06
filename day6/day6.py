import sys
import aocd


with open(sys.argv[1]) as f:
    data = f.read()


def finder(data, buflen):
    for i in range(buflen, len(data)):
        if len(set(data[i - buflen : i])) == buflen:
            return i


s1 = finder(data, 4)
print(s1)
aocd.submit(s1, part="a", day=6, year=2022)
s2 = finder(data, 14)
print(s2)
aocd.submit(s2, part="b", day=6, year=2022)

for i in range(4, len(data)):
    if len(set(data[i - 4 : i])) == 4:
        print(i)
        aocd.submit(i, part="a", day=6, year=2022)
        break

for i in range(14, len(data)):
    if len(set(data[i - 14 : i])) == 14:
        print(i)
        aocd.submit(i, part="b", day=6, year=2022)
        break
