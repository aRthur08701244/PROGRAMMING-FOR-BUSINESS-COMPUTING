n = int(input())
x = int(input())
t = list()
r = list()
ran = int()

for i in range(n):
    t.append(int(input()))
    r.append(int(input()))

for i in range(n):
    if x <= t[i]:
        ran = i
        break

cost = int()
mini = t[n - 1]*r[0]

if ran == 0:
    cost = x*r[0]

else:
    for i in range(0, ran + 1):
        if i == 0:
            cost = t[0]*r[0]
        elif i == ran:
            cost = cost + (x - t[i - 1])*r[i]
        else:
            cost = cost + (t[i] - t[i - 1])*r[i]

if cost < mini:
    mini = cost

print(mini)