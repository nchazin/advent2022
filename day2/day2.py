import sys

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
WIN = "win"
LOSE = "lose"
DRAW = "draw"

types = {"A": ROCK, "B": PAPER, "C": SCISSORS, "X": ROCK, "Y": PAPER, "Z": SCISSORS}

scores = {ROCK: 1, PAPER: 2, SCISSORS: 3, WIN: 6, LOSE: 0, DRAW: 3}
outcomes = {"X": LOSE, "Y": DRAW, "Z": WIN}

beats = {ROCK: SCISSORS, PAPER: ROCK, SCISSORS: PAPER}
loses = {SCISSORS: ROCK, ROCK: PAPER, PAPER: SCISSORS}


with open(sys.argv[1]) as f:
    data = f.readlines()

myscore = 0

for line in data:
    score = 0
    them, mine = line.strip().split(" ")
    them = types[them]
    mine = types[mine]
    score = scores[mine]
    if beats[them] == mine:
        pass
    elif beats[mine] == them:
        score += 6
    else:
        score += 3

    myscore += score

print(myscore)

myscore = 0

for line in data:
    score = 0
    them, outcome = line.strip().split(" ")
    them = types[them]
    outcome = outcomes[outcome]
    score += scores[outcome]

    if outcome == WIN:
        mine = loses[them]
    elif outcome == LOSE:
        mine = beats[them]
    else:
        mine = them
    score += scores[mine]
    myscore += score

print(myscore)
