import sys
import aocd


if len(sys.argv) > 2 and sys.argv[2] == "submit":
    SUBMIT = True
else:
    SUBMIT = False


def submit(val, part, day, year):
    if SUBMIT:
        aocd.submit(val, part=part, day=day, year=year)


with open(sys.argv[1]) as f:
    data = f.readlines()

forest = list(data)
forest = [r.replace("\n","") for r in forest]
#print(forest)


def solve1(forest):
    forelen = len(forest)
    rowlen = len(forest[0])
    VISCOUNT = 0
    MAXSCORE = 0
    for i in range(forelen):
        rowlen = len(forest[i])
        for j in range(rowlen):
            k = forest[i][j]

            #look up
            VISUP = True
            UPCOUNT = 0
            for ih in range(i-1,-1,-1):
                if forest[ih][j] >= k:
                    UPCOUNT = i-ih
                    VISUP = False
                    break
            #if VISUP:
            #    UPCOUNT = i
            #print(f"{i}, {j}, {k}, {VISUP}")

            #lookdown
            VISDOWN = True
            DOWNCOUNT = 0
            for ih in range(i+1,forelen):
                if forest[ih][j] >= k:
                    VISDOWN = False
                    DOWNCOUNT = ih-i
                    break
            #if VISDOWN:
            #    DOWNCOUNT = forelen - 1
            #print(f"{i}, {j}, {k}, {VISDOWN}")

            #lookleft
            VISLEFT = True
            LEFTCOUNT = 0
            for jh in range(j-1,-1,-1):
                if forest[i][jh] >= k:
                    VISLEFT = False
                    LEFTCOUNT = j-jh
                    break
            #print(f"{i}, {j}, {k}, {VISLEFT}")
            #if VISLEFT:
            #    VISCOUNT = j

            #lookright
            VISRIGHT= True
            RIGHTCOUNT = 0
            for jh in range(j+1, rowlen):
                if forest[i][jh] >= k:
                    VISRIGHT = False
                    RIGHTCOUNT = jh - j
                    break
            #print(f"{i}, {j}, {k}, {VISLEFT}")
            #if VISRIGHT:
            #    RIGHTCOUNT = rowlen - j

            if VISUP or VISDOWN or VISLEFT or VISRIGHT:
                VISCOUNT += 1
            score = UPCOUNT * DOWNCOUNT * RIGHTCOUNT * LEFTCOUNT
            #print ("--------------------")
            #print(f"{UPCOUNT} {DOWNCOUNT} {RIGHTCOUNT} {LEFTCOUNT}")
            #print(f"{i} {j} {k} {score}")
            #print ("--------------------")
            if score > MAXSCORE:
                MAXSCORE = score

    print(MAXSCORE)
    return(VISCOUNT)


result = solve1(forest)
print(">",  result)
submit(result, 'a', 8, 2022)