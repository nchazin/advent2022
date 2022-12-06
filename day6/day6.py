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
