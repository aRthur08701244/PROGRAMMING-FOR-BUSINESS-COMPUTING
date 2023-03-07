x1 = int(input())
p1 = int(input())
x2 = int(input())
p2 = int(input())
t = int(input())

total = x1*p1 + x2*p2
remain = t - total

if total <= t:
    print("$" + str(remain))
else:
    print("-1")