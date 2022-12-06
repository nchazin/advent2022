import sys
import aocd


set4 = set()
list4 = list()
with open(sys.argv[1]) as f:
    data = f.read()

for i in range(4, len(data)):
    if data[i] not in data[i-4:i] and len(set(data[i-4:i])) ==4:
        print(i)
        #aocd.submit(i,  part="a", day=6, year=2022)
        break

print('--------')

for i in range(14, len(data)):
    if len(set(data[i-14:i])) ==14:
        print(data[i-14:i])
        print(set(data[i-14:i+1]))
        print(i)
        aocd.submit(i,  part="b", day=6, year=2022)