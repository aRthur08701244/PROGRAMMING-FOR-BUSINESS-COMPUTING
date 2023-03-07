import math

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

angle = strlist[len(strlist) - 1]

del strlist[len(strlist) - 1]

cos = math.cos(math.radians(angle[0]))
sin = math.sin(math.radians(angle[0]))

strlist_2 = []
for i in range(len(strlist)):
    strlist_2.append([])
    for j in range(len(strlist[i])):
        strlist_2[i].append(0)

def rotate(strlist):

    for i in range(len(strlist)):
        for j in range(len(strlist[i])):
            if (j == 0) or (j == 2):
                strlist_2[i][j] = cos*strlist[i][j] - sin*strlist[i][j + 1]
            elif (j == 1) or (j == 3):
                strlist_2[i][j] = sin*strlist[i][j - 1] + cos*strlist[i][j]

    return strlist_2

def printlines(linelist):
    for i, aline in enumerate(linelist):
        print("Line%d: %0.3f %0.3f %0.3f %0.3f" % (i, aline[0], aline[1], aline[2], aline[3]))

printlines(rotate(strlist))
