import sys
import aocd
from collections import deque


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

q = deque()
for i, x in enumerate(data):
    q.append((i, int(x)))
print(f"starting: {q}")
for i in range(len(q)):
    # find the ith element
    while q[0][0] != i:
        q.rotate(-1)
    print(i)
    p, n = q.popleft()
    q.rotate(-1 * n)
    q.appendleft((p, n))
    # print(q)


final = deque([x[1] for x in q])
zero_i = final.index(0)

answer = sum((final[(zero_i + off) % len(q)] for off in (1000, 2000, 3000)))
print(answer)
submit(
    answer,
    "a",
    20,
    2020,
)
