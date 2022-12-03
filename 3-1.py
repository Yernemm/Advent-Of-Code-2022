dataFile = open("3-in.txt", "r")

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0

for line in dataFile:
    line = line.strip()

    parts = [[],[]]
    parts[0] = line[:len(line)//2]
    parts[1] = line[len(line)//2:]
    
    #turns out I misunderstoon the problem
    #and this was not necessary
    #so I turned it into a set reduction algorithm
    #which was unnecessary but might as well

    #preprocess to only check for unique letters
    for i in range(len(parts)):
        part = parts[i]
        unique = ""
        duplicate = ""
        for c in part:
            if c not in unique and c not in duplicate:
                # not in either, make unique
                unique += c
            elif c in unique and c not in duplicate:
                # only in unique, make duplicate
                duplicate += c
                unique = unique.replace(c, "")
            else:
                # already in duplicate, do nothing
                pass
        
        parts[i] = unique + duplicate
    
    print(parts[0], parts[1])

    match = [x for x in parts[0] if x in parts[1]][0]
    print(match)

    #convert to values
    total += alphabet.index(match) + 1

print(total)
