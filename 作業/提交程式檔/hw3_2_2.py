firststr = input()
first = firststr.split(',')
secondstr = input()
second = secondstr.split(',')

n = int(first[0])
x = int(first[1])
t = list()
r = list()
ran = int()
cost = int()

for i in range(n):
    t.append(int(second[i]))
    r.append(int(second[i + n]))

mini_con = int()
mini = t[n-1]*1000000

for k in range(x, t[n-1] + 1):
    for i in range(n):
        if i == 0:
            if 0 < k <= t[i]:
                ran = 0
        else:
            if t[i-1] < k <= t[i]:
                ran = i

    if ran == 0:
        cost = k*r[0]

    else:
        for i in range(0, ran + 1):
            if i == 0:
                cost = t[0]*r[0]
            elif i == ran:
                cost = cost + (k - t[i - 1])*r[i]
            else:
                cost = cost + (t[i] - t[i - 1])*r[i]

    if cost <= mini:
        mini_con = k
        mini = cost

print(str(mini_con) + ',' + str(mini))
