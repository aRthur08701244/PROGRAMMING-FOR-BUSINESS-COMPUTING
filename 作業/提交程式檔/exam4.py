firststr = input()
firststr = firststr.split(',')
n = int(firststr[0])
m = int(firststr[1])
r = int(firststr[2])
p = []

for i in range(m + 1):
    curstr = input()
    curstr = curstr.split(',')
    p.append(curstr)

    for k in range(n + 1):
        p[i][k] = int(p[i][k])


popmax = int()
for i in range(n + 1):
    for j in range(m + 1):
        qualified = []
        for x in range(n + 1):
            for y in range(m + 1):
                if (abs(x - i) + abs(y - j)) <= r:
                    qualified.append([x,y])
        pop = int()
        for k in range(len(qualified)):
            pop += p[qualified[k][0]][qualified[k][1]]

        if pop > popmax:
            popmax = pop

print(popmax)