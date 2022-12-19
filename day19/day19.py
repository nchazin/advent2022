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

blueprints = {}
for line in data:
    parts = line.split(" ")
    print(parts[1])
    id = int(parts[1][:-1])
    ore_cost = int(parts[6])
    try:
        clay_cost = int(parts[12])
    except:
        breakpoint()
    obsidian_cost = (int(parts[18]), int(parts[21]))
    geode_cost = (int(parts[27]), int(parts[30]))
    blueprints[id] = [ore_cost, clay_cost, obsidian_cost, geode_cost]

for id, blueprint in blueprints.items():
    print(f"{id} {blueprint}")


def sim(blueprint, maxt):
    # core, clay, obsidia, geode, orebot, cbot, obsbot, gbot min
    state = (0, 0, 0, 0, 1, 0, 0, 0, 0)

    states_seen = set()
    states = [state]
    geodes = 0
    skipped = 0
    max_ore = max(blueprint[0], blueprint[1], blueprint[2][0], blueprint[3][0])
    while len(states) > 0:
        o, c, ob, g, obt, cbt, obbt, gbt, t = states.pop()

        if t > maxt:
            continue

        # never have more than enough to buy a robot:
        if obt > max_ore:
            obt = max_ore
        if cbt > blueprint[2][1]:
            cbt = blueprint[2][1]
        if obbt > blueprint[3][1]:
            obbt = blueprint[3][1]
        # or too many robots to avoid end times
        if o > max_ore * (24 - t):
            o = max_ore * 24 - t
        if c > blueprint[2][1] * (24 - t):
            c = blueprint[2][1] * (24 - t)
        if ob > blueprint[3][1] * (24 - t):
            ob = blueprint[3][1] * (24 - t)

        capped_state = (o, c, ob, g, obt, cbt, obbt, gbt, t)

        geodes = max(geodes, g)

        if capped_state in states_seen:
            continue

        states_seen.add(capped_state)
        if len(states_seen) % 100000 == 0:
            print(len(states_seen))

        # no robots
        states.append(
            (o + obt, c + cbt, ob + obbt, g + gbt, obt, cbt, obbt, gbt, t + 1)
        )

        if o >= blueprint[0]:
            states.append(
                (
                    o + obt - blueprint[0],
                    c + cbt,
                    ob + obbt,
                    g + gbt,
                    obt + 1,
                    cbt,
                    obbt,
                    gbt,
                    t + 1,
                )
            )
        if o >= blueprint[1]:
            states.append(
                (
                    o + obt - blueprint[1],
                    c + cbt,
                    ob + obbt,
                    g + gbt,
                    obt,
                    cbt + 1,
                    obbt,
                    gbt,
                    t + 1,
                )
            )
        if o >= blueprint[2][0] and c >= blueprint[2][1]:
            states.append(
                (
                    o + obt - blueprint[2][0],
                    c + cbt - blueprint[2][1],
                    ob + obbt,
                    g + gbt,
                    obt,
                    cbt,
                    obbt + 1,
                    gbt,
                    t + 1,
                )
            )
        if o >= blueprint[3][0] and ob >= blueprint[3][1]:
            states.append(
                (
                    o + obt - blueprint[3][0],
                    c + cbt,
                    ob + obbt - blueprint[3][1],
                    g + gbt,
                    obt,
                    cbt,
                    obbt,
                    gbt + 1,
                    t + 1,
                )
            )

    return geodes


total = 0
for id, blueprint in blueprints.items():
    maxg = sim(blueprint, 24)
    score = id * maxg
    total += score

submit(total, "a", 19, 2022)
