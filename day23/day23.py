import sys
import aocd
from collections import deque, defaultdict


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


class Elf:
    north = [(-1, -1), (0, -1), (1, -1)]
    south = [(-1, 1), (0, 1), (1, 1)]
    east = [(1, -1), (1, 0), (1, 1)]
    west = [(-1, -1), (-1, 0), (-1, 1)]

    def __init__(self, id, x, y, elves):
        self.id = id
        self.last_move = None
        self.dir = deque(["N", "S", "W", "E"])
        self.x = x
        self.y = y
        self.elves = elves

    @property
    def neighbors(self):
        north = [[-1, -1], [0, -1], [1, -1]]
        south = [[-1, 1], [0, 1], [1, 1]]
        east = [[1, -1], [1, 0], [1, 1]]
        west = [[-1, -1], [-1, 0], [-1, 1]]

        neighbors = set()
        for dx, dy in north + south + east + west:
            if self.elves.get((dx + self.x, dy + self.y)) is not None:
                neighbors.add((dx, dy))
        return neighbors

    def consider_move(self, all_moves):
        self.last_move = None
        if len(self.neighbors) == 0:
            return None
        else:
            for dir in self.dir:
                match dir:
                    case "N":
                        if len(self.neighbors.intersection(self.north)) == 0:
                            self.last_move = (self.x, self.y - 1)
                            all_moves[self.last_move] += 1
                            break
                    case "S":
                        if len(self.neighbors.intersection(self.south)) == 0:
                            self.last_move = (self.x, self.y + 1)
                            all_moves[self.last_move] += 1
                            break
                    case "E":
                        if len(self.neighbors.intersection(self.east)) == 0:
                            self.last_move = (self.x + 1, self.y)
                            all_moves[self.last_move] += 1
                            break
                    case "W":
                        if len(self.neighbors.intersection(self.west)) == 0:
                            self.last_move = (self.x - 1, self.y)
                            all_moves[self.last_move] += 1
                            break

        return (self, self.last_move)

    def perform_move(self, all_moves):
        if self.last_move is not None and all_moves[self.last_move] == 1:
            del self.elves[(self.x, self.y)]
            self.x = self.last_move[0]

            self.y = self.last_move[1]
            self.elves[(self.x, self.y)] = self

    def shiftdir(self):
        self.dir.rotate(-1)


elves = dict()


def print_elves(elves):
    minx = min(p[0] for p in elves.keys())
    maxx = max(p[0] for p in elves.keys())
    miny = min(p[1] for p in elves.keys())
    maxy = max(p[1] for p in elves.keys())

    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            if elves.get((x, y)) is not None:
                print("#", end="")
            else:
                print(".", end="")
        print("")

    return (minx, maxx, miny, maxy)


id = 0
for y, line in enumerate(data):
    line = line.strip()
    for x, c in enumerate(line):
        if c == "#":
            e = Elf(id, x, y, elves)
            id += 1
            elves[(x, y)] = e


def run_round(elves):
    all_moves = defaultdict(int)
    elf_moves = list()
    for elf in elves.values():
        move = elf.consider_move(all_moves)
        if move is not None:
            elf_moves.append(move)

    for move in elf_moves:
        move[0].perform_move(all_moves)

    for elf in elves.values():
        elf.shiftdir()


for i in range(1, 11):
    print(f"Running round {i}")
    run_round(elves)
print("====================")
minx, maxx, miny, maxy = print_elves(elves)
submit((abs(maxx - minx) + 1) * (abs(maxy - miny) + 1) - len(elves), "a", 23, 2022)
