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

forest = list(data)
forest = [r.replace("\n", "") for r in forest]


def solve1(forest):
    forelen = len(forest)
    rowlen = len(forest[0])
    viscount = 0
    maxscore = 0
    for i in range(forelen):
        rowlen = len(forest[i])
        for j in range(rowlen):
            k = forest[i][j]

            # look up
            visup = True
            upcount = 0
            for ih in range(i - 1, -1, -1):
                if forest[ih][j] >= k:
                    upcount = i - ih
                    visup = False
                    break
            if visup and i > 0:
                upcount = i

            # lookdown
            visdown = True
            downcount = 0
            for ih in range(i + 1, forelen):
                if forest[ih][j] >= k:
                    visdown = False
                    downcount = ih - i
                    break
            if visdown and i < forelen - 1:
                downcount = forelen - i - 1

            # lookleft
            visleft = True
            leftcount = 0
            for jh in range(j - 1, -1, -1):
                if forest[i][jh] >= k:
                    visleft = False
                    leftcount = j - jh
                    break
            if visleft and j > 0:
                leftcount = j

            # lookright
            visright = True
            rightcount = 0
            for jh in range(j + 1, rowlen):
                if forest[i][jh] >= k:
                    visright = False
                    rightcount = jh - j
                    break
            if visright and j < rowlen - 1:
                rightcount = rowlen - j - 1

            if visup or visdown or visleft or visright:
                viscount += 1
            score = upcount * downcount * rightcount * leftcount
            if score > maxscore:
                maxscore = score

    return [maxscore, viscount]


score, count = solve1(forest)
submit(count, "a", 8, 2022)
submit(score, "b", 8, 2022)
