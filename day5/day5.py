import sys
import math

with open(sys.argv[1]) as f:
    data = f.readlines()


def make_stacks():
    stacksize = 0
    stacks = []

    # setup the stacks
    for line in data:
        line = line.strip("\n")
        if line.find("[") == -1:
            stacks = [list(reversed(s)) for s in stacks]
            break
        if stacksize == 0:
            stacksize = math.ceil(len(line) / 4.0)
            for s in range(stacksize):
                stacks.append(list())
        for item in range(stacksize):
            index = item * 4
            crate = line[index + 1]
            if crate != " ":
                stacks[item].append(crate)
    return stacks


stacks = make_stacks()

# find the instructiosn and do them
in_commands = False
for line in data:
    line = line.strip("\n")
    if line == "":
        in_commands = True
        continue
    if in_commands:
        parts = line.split(" ")
        count = int(parts[1])
        mfrom = int(parts[3])
        mto = int(parts[5])
        for i in range(count):
            c = stacks[mfrom - 1].pop()
            stacks[mto - 1].append(c)


def print_stacks(stacks):
    print(''.join(stack[-1]for stack in stacks))


print_stacks(stacks)


stacks = make_stacks()

in_commands = False
for line in data:
    line = line.strip("\n")
    if line == "":
        in_commands = True
        continue
    if in_commands:
        parts = line.split(" ")
        count = int(parts[1])
        mfrom = int(parts[3])
        mto = int(parts[5])
        to_add = []
        for i in range(count):
            c = stacks[mfrom - 1].pop()
            to_add.append(c)
        to_add.reverse()
        for c in to_add:
            stacks[mto - 1].append(c)

print_stacks(stacks)
