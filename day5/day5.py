import sys
import math

with open(sys.argv[1]) as f:
    data = f.readlines()

stacksize = 0
stacks = []

#setup the stacks
for line in data:
    line = line.strip('\n')
    if line.find('[') == -1:
        stacks = [list(reversed(s)) for s in stacks]
        break
    if stacksize== 0:
        stacksize = math.ceil(len(line)/4.0)
        for s in range(stacksize):
            stacks.append(list())
    for item in range(stacksize):
        index = item*4
        crate = line[index+1]
        if crate != ' ':
            stacks[item].append(crate)

print(stacks)

#find the instructiosn and do them    
in_commands = False
for line in data:
    line = line.strip('\n')
    if line == '':
        in_commands = True
        continue
    if in_commands:
        parts = line.split(' ')
        count = int(parts[1])
        mfrom = int(parts[3])
        mto = int(parts[5])
        print(f"Move {count} from {mfrom} to {mto}")
        for i in range(count):
            c = stacks[mfrom-1].pop()
            stacks[mto-1].append(c)

print(stacks)
for x in stacks:
    print(x[-1], end="")    
print()
    
      
