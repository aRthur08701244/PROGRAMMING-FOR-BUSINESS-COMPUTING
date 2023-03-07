# input
meal_p1 = int(input())
drink_p2 = int(input())
discount = int(input())
cost = int()

# calculate the cost
cost = meal_p1 + drink_p2 - discount

if cost < 0:
    cost = 0

# print it out
print(cost)
