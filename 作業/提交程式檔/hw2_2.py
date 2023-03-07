x = int(input())
t1 = int(input())
r1 = int(input())
t2 = int(input())
r2 = int(input())
t3 = int(input())
r3 = int(input())
cost = int()
mini = t3*r1

for i in range(x, t3 + 1):
    if i <= t1:
        cost = i*r1
    elif t1 < i <= t2:
        cost = t1*r1 + (i - t1)*r2
    else:
        cost = t1*r1 + (t2 - t1)*r2 + (i - t2)*r3

    if cost < mini:
        mini = cost

print(mini)