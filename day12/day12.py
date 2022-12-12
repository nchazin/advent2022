import sys
import aocd
from collections import defaultdict, deque
import string
from math import inf


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
    data = f.read()


grid = data.split("\n")[:-1]
start = None
end = None


def get_adjacent(cur, imax, jmax):
    adjacent = []
    i = cur[0]
    j = cur[1]
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        newi = i + di
        newj = j + dj
        if 0 <= newi <= imax and 0 <= newj <= jmax:
            adjacent.append((newi, newj))
    return adjacent


def get_height(c):
    if c == "S":
        c = "a"
    elif c == "E":
        c = "z"

    return string.ascii_letters.find(c)


def path_find(grid, start, reverse=False):
    squares_to_visit = []
    end = ()
    imax = len(grid) - 1
    jmax = len(grid[0]) - 1
    total_squares = len(grid) * len(grid[0])
    for i, row in enumerate(grid):
        if (j := row.find("E")) >= 0:
            end = (i, j)

    square_distances = defaultdict(lambda: inf)
    square_distances[start] = 0
    visited_squares = set()

    squares_to_visit = deque()
    squares_to_visit.append((0, start))
    steps = 0
    while len(squares_to_visit) > 0 and len(visited_squares) < total_squares:
        visit = squares_to_visit.popleft()
        distance, cur = visit
        steps += 1
        adjacents = get_adjacent(cur, imax, jmax)

        if cur in visited_squares:
            continue

        cur_height = get_height(grid[cur[0]][cur[1]])

        for square in adjacents:
            square_height = get_height(grid[square[0]][square[1]])
            if not reverse:
                test = square_height <= cur_height + 1
            else:
                test = square_height >= cur_height - 1
            if square not in visited_squares and test:
                # lower the distance
                square_distance = min(
                    square_distances[square], square_distances[cur] + 1
                )
                square_distances[square] = square_distance
                squares_to_visit.append((square_distance, square))

        visited_squares.add(cur)
    return square_distances


start = None
for i, row in enumerate(grid):
    if (j := row.find("S")) >= 0:
        start = (i, j)
    if (j := row.find("E")) >= 0:
        end = (i, j)
submit(path_find(grid, start)[end], "a", 12, 2022)


possible_starts = []
for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c == "S" or c == "a":
            possible_starts.append((i, j))

pathlens = path_find(grid, end, reverse=True)

best = inf
for start in possible_starts:
    if pathlens[start] < best:
        best = pathlens[start]

submit(best, "b", 12, 2022)
