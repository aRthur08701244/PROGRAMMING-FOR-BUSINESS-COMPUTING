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
    if i == 0:
        if 0 < x <= t[i]:
            cost = x*r[0]
    else:
        if t[i-1] < x <= t[i]:
            ran = i

if ran != 0:
    for i in range(0, ran + 1):
        if i == 0:
            cost = t[0]*r[0]
        elif i == ran:
            cost = cost + (x - t[i - 1])*r[i]
        else:
            cost = cost + (t[i] - t[i - 1])*r[i]

print(cost)
