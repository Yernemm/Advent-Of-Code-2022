
dataFile = open("1-1-input.txt", "r")

runningTotal = 0
runningMax = 0

#put datafile into a 2D list, each row is separated by a new line
for line in dataFile:
    l = line.split()
    if(len(l) > 0):
        runningTotal += int(l[0])
    else:
        runningMax = max(runningMax, runningTotal)
        runningTotal = 0

print(runningMax)