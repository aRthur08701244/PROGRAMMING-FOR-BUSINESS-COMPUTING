counter = 0
strlist = []
while True:
    put = input()
    if put != "LINESTOP":
        strlist.append(put)
        if counter == 1:
            break
    else:
        counter = 1

for i in range(len(strlist)):
    strlist[i] = strlist[i].split(',')
    for j in range(len(strlist[i])):
        strlist[i][j] = float(strlist[i][j])

xshift = strlist[len(strlist) - 1][0]
yshift = strlist[len(strlist) - 1][1]

del strlist[len(strlist) - 1]

def plotshift(strlist):

    for i in range(len(strlist)):
        for j in range(len(strlist[i])):
            if (j == 0) or (j == 2):
                strlist[i][j] += xshift
            elif (j == 1) or (j == 3):
                strlist[i][j] += yshift

    return strlist

def printlines(linelist):
    for i, aline in enumerate(linelist):
        print("Line%d: %0.3f %0.3f %0.3f %0.3f" % (i, aline[0], aline[1], aline[2], aline[3]))

printlines(plotshift(strlist))
