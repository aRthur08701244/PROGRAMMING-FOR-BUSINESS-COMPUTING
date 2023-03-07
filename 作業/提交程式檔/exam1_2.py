n = int(input())

firststr = input()

firststr = firststr.split(',')

x = []

for i in range(n):
    x.append(int(firststr[i]))

y = []

for i in range(n - 1):
    if (x[i] - x[i + 1]) >= 0:
        y.append(x[i] - x[i + 1])
    else:
        y.append(0)

mn = y[0]

for i in range(n - 1):
    if y[i] < mn:
        mn = y[i]

print(mn)