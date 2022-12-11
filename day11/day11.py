import sys
import aocd
from typing import Callable, List, Any
from math import floor


if len(sys.argv) > 1 and sys.argv[1] == "submit":
    SUBMIT = True
else:
    SUBMIT = False


def submit(val, part, day, year):
    if SUBMIT:
        aocd.submit(val, part=part, day=day, year=year)
    else:
        print(f"Not submiting {val} for 12/{day}/{year} part {part}")


class Monkey:
    def __init__(
        self,
        monkeys: List[Any],
        items: List[int],
        worrying: Callable,
        deciding: Callable,
        truetarget: int,
        falsetarget: int,
    ):
        self.monkeys = monkeys
        self.items = items
        self.worrying = worrying
        self.deciding = deciding
        self.truetarget = truetarget
        self.falsetarget = falsetarget
        self.inspected = 0

    def turn(self, divide=True, modulo=1):
        while len(self.items) > 0:
            item = self.items.pop(0)
            item = self.worrying(item)
            if divide:
                item = floor(item / 3)
            else:
                item = item % modulo
            if self.deciding(item):
                self.monkeys[self.truetarget].throw(item)
            else:
                self.monkeys[self.falsetarget].throw(item)
            self.inspected += 1

    def throw(self, item):
        self.items.append(item)


def make_test_monkeys():
    test_monkeys = []
    test_monkeys.append(
        Monkey(
            test_monkeys, [79, 98], (lambda x: x * 19), (lambda x: x % 23 == 0), 2, 3
        )
    )
    test_monkeys.append(
        Monkey(
            test_monkeys, [54, 65, 75, 74], lambda x: x + 6, lambda x: x % 19 == 0, 2, 0
        )
    )
    test_monkeys.append(
        Monkey(test_monkeys, [79, 60, 97], lambda x: x * x, lambda x: x % 13 == 0, 1, 3)
    )
    test_monkeys.append(
        Monkey(test_monkeys, [74], lambda x: x + 3, lambda x: x % 17 == 0, 0, 1)
    )
    return test_monkeys


def make_monkeys():
    monkeys = []
    monkeys.append(
        Monkey(
            monkeys,
            [89, 95, 92, 64, 87, 68],
            (lambda x: x * 11),
            (lambda x: x % 2 == 0),
            7,
            4,
        )
    )
    monkeys.append(
        Monkey(monkeys, [87, 67], (lambda x: x + 1), (lambda x: x % 13 == 0), 3, 6)
    )
    monkeys.append(
        Monkey(
            monkeys,
            [95, 79, 92, 82, 60],
            (lambda x: x + 6),
            (lambda x: x % 3 == 0),
            1,
            6,
        )
    )
    monkeys.append(
        Monkey(monkeys, [67, 97, 56], (lambda x: x * x), (lambda x: x % 17 == 0), 7, 0)
    )
    monkeys.append(
        Monkey(
            monkeys,
            [80, 68, 87, 94, 61, 59, 50, 68],
            (lambda x: x * 7),
            (lambda x: x % 19 == 0),
            5,
            2,
        )
    )
    monkeys.append(
        Monkey(
            monkeys, [73, 51, 76, 59], (lambda x: x + 8), (lambda x: x % 7 == 0), 2, 1
        )
    )
    monkeys.append(
        Monkey(monkeys, [92], (lambda x: x + 5), (lambda x: x % 11 == 0), 3, 0)
    )
    monkeys.append(
        Monkey(
            monkeys,
            [99, 76, 78, 76, 79, 90, 89],
            (lambda x: x + 7),
            (lambda x: x % 5 == 0),
            4,
            5,
        )
    )
    return monkeys


test_monkeys = make_test_monkeys()


def play(rounds, monkeys, divide=True, modulo=1):
    for round in range(rounds):
        for i, monkey in enumerate(monkeys):
            monkey.turn(divide, modulo)

    business = []
    for monkey in monkeys:
        business.append(monkey.inspected)

    business.sort()
    return business[-1] * business[-2]


print(play(20, test_monkeys))


monkeys = make_monkeys()
submit(play(20, monkeys), "a", 11, 2022)

test_monkeys = make_test_monkeys()
modulo = 23 * 19 * 13 * 17
print(play(10000, test_monkeys, False, modulo))

modulo = 2 * 13 * 3 * 17 * 19 * 7 * 11 * 5
monkeys = make_monkeys()
submit(play(10000, monkeys, False, modulo), "b", 11, 2022)
