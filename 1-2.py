dataFile = open("1-input.txt", "r")

totals = []
runningTotal = 0

for line in dataFile:
    l = line.split()
    if(len(l) > 0):
        runningTotal += (int(l[0]))
    else:
        totals.append(runningTotal)
        runningTotal = 0
totals.append(runningTotal)

totals = sorted(totals)
print(totals)
print(totals[-1])

maxN = 3
maxSum = 0
for i in range(maxN):
    maxSum += totals[-(i+1)]

print(maxSum)
