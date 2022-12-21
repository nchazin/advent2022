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

value = 0


class Monkey:
    def __init__(self, name, val=None, left=None, right=None, operator=None):
        self.name = name
        self.left = left
        self.right = right
        self._val = val
        self.operator = operator

    def solve(self, value):
        if self.operator == "?":
            return value
        if self._val is not None:
            return self._val
        v, find_node = self.resolve()
        if v == None and find_node == None:
            return self.val
        match self.operator:
            case "+":
                return find_node.solve(value - v)
            case "-":
                if find_node == self.right:
                    ret = find_node.solve(v - value)

                else:
                    ret = find_node.solve(v + value)
                return ret

            case "*":
                return find_node.solve(value / v)
            case "/":
                # value  = left / right
                if find_node == self.right:
                    ret = find_node.solve(v / value)
                else:
                    ret = find_node.solve(value * v)

                return ret

    def resolve(self):
        value = None
        find_node = None
        matches = 0
        try:
            a = self.left.val
            b = self.right.val
        except Exception as E:
            pass
        try:
            value = self.left.val
            find_node = self.right
            matches += 1
        except Exception as E:
            pass
        try:
            value = self.right.val
            find_node = self.left
            matches += 1
        except:
            pass
        if matches > 1:
            return None, None
        return value, find_node

    def mprint(self, h):
        print(" " * h * 4, self.name, self._val, self.operator)
        if self.left is not None:
            self.left.mprint(h + 1)
        if self.right is not None:
            self.right.mprint(h + 1)

    @property
    def val(self):
        if self._val is not None:
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
            case "=":
                value, find_node = self.resolve()
                return find_node.solve(value)
            case "?":
                raise Exception(self.name, " Does not compute!")


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

# part2
monkeyd["root"].operator = "="
monkeyd["humn"].operator = "?"
monkeyd["humn"]._val = None

submit(int(monkeyd["root"].val), "b", 21, 2022)
