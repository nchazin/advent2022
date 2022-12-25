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

stoi_digit = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2,
}

itos_numeral = {
    4: "-",  # -1
    3: "=",  # -2
    2: "2",
    1: "1",
    0: "0",
}


def stoi(s):
    value = 0
    power = 0
    for i in range(len(s) - 1, -1, -1):
        digit = s[i]
        value += stoi_digit[digit] * (5**power)
        power += 1
    return value


def itos(d):
    if d == 0:
        return ""

    a = d % 5
    b = d // 5
    if a > 2:
        b += 1

    return itos(b) + itos_numeral[a]


def snafu2int(s):
    tot = 0

    for d in s:
        tot = tot * 5 + numeral[d]

    return tot


total = sum(stoi(line.rstrip()) for line in data)
value = itos(total)
submit(itos(total), "a", 25, 2022)
