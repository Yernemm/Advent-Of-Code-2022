# let's do it a bad way

dataFile = open("2-in.txt", "r")

map = {
    "A X": 1 + 3,
    "B X": 1 + 0,
    "C X": 1 + 6,
    "A Y": 2 + 6,
    "B Y": 2 + 3,
    "C Y": 2 + 0,
    "A Z": 3 + 0,
    "B Z": 3 + 6,
    "C Z": 3 + 3
}

score = 0
for line in dataFile:
    line = line.strip()
    score = score + map[line]

print(score)