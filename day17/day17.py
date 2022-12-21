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
    data = f.read()

pattern = data.strip()


tower = {(x, 0) for x in range(7)}
height = 0
p = 0


def get_jet(p, pattern):
    p = p % len(pattern)
    return pattern[p]


def get_shape(p, y):
    shapes = [
        [(2, y), (3, y), (4, y), (5, y)],
        [(3, y), (2, y + 1), (3, y + 1), (4, y + 1), (3, y + 2)],
        [(2, y), (3, y), (4, y), (4, y + 1), (4, y + 2)],
        [(2, y), (2, y + 1), (2, y + 2), (2, y + 3)],
        [(2, y), (3, y), (2, y + 1), (3, y + 1)],
    ]
    p = p % len(shapes)
    return shapes[p]


def move_right(shape):
    shape = [(s[0] + 1, s[1]) for s in shape]
    return shape


def move_left(shape):
    shape = [(s[0] - 1, s[1]) for s in shape]
    return shape


def move_down(shape):
    shape = [(s[0], s[1] - 1) for s in shape]
    return shape


def move_up(shape):
    shape = [(s[0], s[1] + 1) for s in shape]
    return shape


def pp(x):
    print(x, end="")


def pt(shape=set()):
    h = 0
    if len(shape) > 0:
        h = max(p[1] for p in shape)
    h += 4
    for y in range(height + h, 0, -1):
        pp("|")
        for x in range(7):
            if (x, y) in shape:
                pp("@")
            elif (x, y) in tower:
                pp("#")
            else:
                pp(".")
        print("|")
    print("+-------+")


jets = 0
for i in range(2022):
    shape = get_shape(p, height + 4)
    p += 1
    while True:
        # pt(shape)
        jet = get_jet(jets, pattern)
        jets += 1
        if jet == ">":
            if not any(p[0] == 6 for p in shape) and not any(
                (p[0] + 1, p[1]) in tower for p in shape
            ):
                # print("move right")
                shape = move_right(shape)

        elif jet == "<":
            if not any(p[0] == 0 for p in shape) and not any(
                (p[0] - 1, p[1]) in tower for p in shape
            ):
                # print("move left")
                shape = move_left(shape)
        else:
            raise (f"didnt expect {jet}")
        shape = move_down(shape)
        # see if we entered the tower
        if any(p in tower for p in shape):
            # oops, move up
            # print("-------")
            # print(f"{shape} in {tower}")
            shape = move_up(shape)
            tower = tower.union(set(shape))
            height = max(p[1] for p in tower)
            break
    # pt()

    # print(f"Tower: {tower}")

submit(height, "a", 17, 2022)
