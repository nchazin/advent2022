import sys
import aocd
from heapq import heappop, heappush
from collections import defaultdict
from functools import cache


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


class Valve:
    def __init__(self, name, flow, neighbors):
        self.name = name
        self.flow = flow
        self.neighbors = neighbors
        self.on = False

    def __repr__(self):
        return f"{self.name}: {self.flow} -> {self.neighbors}\n"


valves = dict()

for line in data:
    parts = line.strip().split(" ")
    name = parts[1]
    flow_rate = int(parts[4].split("=")[1].strip(";"))
    neighbors = [v.strip(",") for v in parts[9:]]
    valves[name] = Valve(name, flow_rate, neighbors)

max_answer = 0
answers_too_far = 0
total_calls = 0

g_visited = defaultdict(int)


@cache
def move(cur_node, prev_node, cur_total, cur_flow_enabled, valves_on, visited, tick):
    global max_answer, total_calls, answers_too_far
    # if tick >= 30 or tick == 1:
    #   print(f"{tick} {cur_node} {cur_flow_enabled} {valves_on}")
    new_total = cur_total + cur_flow_enabled
    total_calls += 1
    if total_calls % 1000 == 0:
        print(f"calls: {total_calls}")

    if tick >= 31:
        if tick == 31:
            if new_total > max_answer:
                max_answer = new_total
            else:
                answers_too_far = max(answers_too_far, new_total)
        return
    valve = valves[cur_node]
    # move without turning on
    for n in valve.neighbors:
        if n == prev_node and len(valve.neighbors) > 1:
            continue
        move(
            n,
            cur_node,
            new_total,
            cur_flow_enabled,
            valves_on,
            visited + [cur_node],
            tick + 1,
        )

    if cur_node not in valves_on and cur_flow_enabled + valve.flow > cur_flow_enabled:
        # print(
        #    f"tick: {tick} turning on {cur_node}/{valve.flow} - {valves_on} new flow: {cur_flow_enabled + valve.flow},"
        # )
        new_total += cur_flow_enabled
        # turn on the valve
        for n in valve.neighbors:
            # break quick loops but allow culdesacs
            if n == prev_node and len(valve.neighbors) > 1:
                continue
            move(
                n,
                cur_node,
                new_total,
                cur_flow_enabled + valve.flow,
                valves_on + [cur_node],
                visited + [cur_node],
                tick + 2,
            )
    # soak up the rest of the time
    # new_total += cur_flow_enabled * (30 - tick)
    # answers.add(new_total)
    # return


move("AA", None, 0, 0, [], [], 1)

# breakpoint()
print(max_answer)
print(answers_too_far)
