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
    VISCOUNT = 0
    MAXSCORE = 0
    for i in range(forelen):
        rowlen = len(forest[i])
        for j in range(rowlen):
            k = forest[i][j]

            # look up
            VISUP = True
            UPCOUNT = 0
            for ih in range(i - 1, -1, -1):
                if forest[ih][j] >= k:
                    UPCOUNT = i - ih
                    VISUP = False
                    break
            if VISUP and i > 0:
                UPCOUNT = i

            # lookdown
            VISDOWN = True
            DOWNCOUNT = 0
            for ih in range(i + 1, forelen):
                if forest[ih][j] >= k:
                    VISDOWN = False
                    DOWNCOUNT = ih - i
                    break
            if VISDOWN and i < forelen - 1:
                DOWNCOUNT = forelen - i - 1

            # lookleft
            VISLEFT = True
            LEFTCOUNT = 0
            for jh in range(j - 1, -1, -1):
                if forest[i][jh] >= k:
                    VISLEFT = False
                    LEFTCOUNT = j - jh
                    break
            if VISLEFT and j > 0:
                LEFTCOUNT = j

            # lookright
            VISRIGHT = True
            RIGHTCOUNT = 0
            for jh in range(j + 1, rowlen):
                if forest[i][jh] >= k:
                    VISRIGHT = False
                    RIGHTCOUNT = jh - j
                    break
            if VISRIGHT and j < rowlen - 1:
                RIGHTCOUNT = rowlen - j - 1

            if VISUP or VISDOWN or VISLEFT or VISRIGHT:
                VISCOUNT += 1
            score = UPCOUNT * DOWNCOUNT * RIGHTCOUNT * LEFTCOUNT
            if score > MAXSCORE:
                MAXSCORE = score

    return [MAXSCORE, VISCOUNT]


score, count = solve1(forest)
submit(count, "a", 8, 2022)
submit(score, "b", 8, 2022)
