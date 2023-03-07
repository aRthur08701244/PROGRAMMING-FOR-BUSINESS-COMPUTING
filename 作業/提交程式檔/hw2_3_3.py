n = int(input())
x = int(input())
bf = int()  # bound_forward
bb = int()  # bound_backward
t = int()
cost = int()

for i in range(n):
    bf = bb
    bb = int(input())
    t = int(input())
    if bf < x <= bb:
        cost = cost + (x - bf)*t
    elif x > bb:
        cost = cost + (bb - bf)*t
    else:
        cost = cost

print(cost)