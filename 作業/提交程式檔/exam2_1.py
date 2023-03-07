def printlines(linelist):
    for i, aline in enumerate(linelist):
        print("Line%d: %0.3f %0.3f %0.3f %0.3f" %(i, aline[0], aline[1], aline[2], aline[3]))
def plotmirrior(linelist, horv="h", loc=0):
    if horv == 'h':
        for i in range(len(linelist)):
            for j in range(len(linelist[i])):
                if (j == 1) or (j == 3):
                    linelist[i][j] = loc + (loc - linelist[i][j])
    if horv == 'v':
        for i in range(len(linelist)):
            for j in range(len(linelist[i])):
                if (j == 0) or (j == 2):
                    linelist[i][j] = loc + (loc - linelist[i][j])

    
    return linelist

lines = []

while True:
    strin = input()
    if strin == "LINESTOP":
        break
    strin = strin.split(',')
    for i in range(len(strin)):
        strin[i] = int(strin[i])
    lines.append(strin)
str2 = input().split(',')
horv = str2[0]
loc = float(str2[1])

fig = plotmirrior(lines, horv, loc)
printlines(fig)