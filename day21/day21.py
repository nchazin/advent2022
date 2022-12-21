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
    monkeys = f.readlines()


class Monkey:
    def __init__(self, name, val=None, left=None, right=None, operator=None):
        self.name = name
        self.left = left
        self.right = right
        self._val = val
        self.operator = operator

    @property
    def val(self):
        if self._val:
            print(f"")
            return self._val
        match self.operator:
            case "+":
                return self.left.val + self.right.val
            case "-":
                return self.left.val - self.right.val
            case "*":
                return self.left.val * self.right.val
            case "/":
                return self.left.val / self.right.val


monkeyd = dict()
for monkey in monkeys:
    p = monkey.strip().split(" ")

    name = p[0].split(":")[0]
    m = Monkey(name)
    if len(p) == 2:
        m._val = int(p[1])
    else:
        op1 = p[1]
        operator = p[2]
        op2 = p[3]
        m.operator = operator
        m.left = op1
        m.right = op2
    monkeyd[name] = m

for name, monkey in monkeyd.items():
    if monkey.left is not None:
        monkey.left = monkeyd[monkey.left]
    if monkey.right is not None:
        monkey.right = monkeyd[monkey.right]

submit(int(monkeyd["root"].val), "a", 21, 2022)

sys.exit(1)


monkey_nums = dict()
for i in range(1000):
    for monkey in monkeys:
        p = monkey.strip().split(" ")

        name = p[0].split(":")[0]
        if len(p) == 2:
            monkey_nums[name] = int(p[1])
        else:
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


monkey_nums = dict()
for i in range(1000):
    for monkey in monkeys:
        p = monkey.strip().split(" ")

        name = p[0].split(":")[0]
        if name == "humn":
            continue
        if len(p) == 2:
            monkey_nums[name] = int(p[1])
        else:
            op1 = p[1]
            operand = p[2]
            op2 = p[3]
            if name == "root":
                import pprint

                if op1 in monkey_nums:
                    print(f"{op2} -> {monkey_nums[op2]}")
                    pprint.pprint(monkey_nums)
                    sys.exit(1)
                if op2 in monkey_nums:
                    print(f"{op2} -> {monkey_nums[op2]}")
                    pprint.pprint(monkey_nums)
                    sys.exit(1)

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
