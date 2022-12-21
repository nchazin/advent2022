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


monkey_nums = dict()

with open(sys.argv[1]) as f:
    monkeys = f.readlines()

for i in range(1000):
    for monkey in monkeys:
        p = monkey.strip().split(" ")

        name = p[0].split(":")[0]
        if len(p) == 2:
            monkey_nums[name] = int(p[1])
        else:
            print(p)
            op1 = p[1]
            operand = p[2]
            op2 = p[3]
            if op1 in monkey_nums and op2 in monkey_nums:
                match operand:
                    case "+":
                        monkey_nums[name] = monkey_nums[op1] + monkey_nums[op2]
                    case "-":
                        monkey_nums[name] = monkey_nums[op1] - monkey_nums[op2]
                    case "/":
                        monkey_nums[name] = monkey_nums[op1] / monkey_nums[op2]
                    case "*":
                        monkey_nums[name] = monkey_nums[op1] * monkey_nums[op2]
    if "root" in monkey_nums:
        print(i)
        submit(int(monkey_nums["root"]), "a", 21, 2022)
        break
