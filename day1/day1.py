import sys


with open(sys.argv[1]) as f:
    data = f.readlines()


elves = []
counter = 0
for line in data:
    line = line.strip()
    if line == '':
        elves.append(counter)
        counter = 0
    else:
        counter += int(line)

elves.append(counter)

print(elves)
elves.sort()
print(elves[-1])
    
    
