# let's do it a bad way

dataFile = open("2-in.txt", "r")

map = {
    "A X": 0 + 3,
    "B X": 0 + 1,
    "C X": 0 + 2,
    "A Y": 3 + 1,
    "B Y": 3 + 2,
    "C Y": 3 + 3,
    "A Z": 6 + 2,
    "B Z": 6 + 3,
    "C Z": 6 + 1
}

score = 0
for line in dataFile:
    line = line.strip()
    score = score + map[line]

print(score)