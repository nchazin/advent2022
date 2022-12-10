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


counter_values = [0, 1]
for line in data:
    parts = line.strip().split(" ")
    if len(parts) == 1:
        counter_values.append(counter_values[-1])
    else:
        arg = int(parts[1])
        counter_values.append(counter_values[-1])
        counter_values.append(counter_values[-1] + arg)

check = 20
signal = 0
while check < len(counter_values):
    signal += check * counter_values[check]
    check += 40


submit(signal, "a", 10, 2022)

rowval = 0
for i in range(1, len(counter_values) - 1):
    if rowval >= 40:
        rowval = 0
    sprite_center = counter_values[i]
    if sprite_center - 1 <= rowval <= sprite_center + +1:
        print("#", end="")
    else:
        print(".", end="")
    if i % 40 == 0:
        print("")
    rowval += 1
