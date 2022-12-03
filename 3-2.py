import util

dataFile = open("3-in.txt", "r")

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0


# first pass, split into groups of 3 and strip duplicates

groups = []

i = 0
for line in dataFile:
    line = line.strip()
    #remove duplicate chars from line
    line = util.removeDuplicates(line)
    if i % 3 == 0:
        groups.append([line])
    else:
        groups[-1].append(line)
    i += 1

print(groups)

# second pass, find the common chars in each group of 3

for group in groups:
    common01 = util.findCommonChars(group[0], group[1])
    #common01 to string
    common01 = "".join(common01)
    common012 = util.findCommonChars(common01, group[2])
    #common012 to string
    common012 = "".join(common012)
    print(common012)
    total += alphabet.index(common012[0]) + 1

print(total)