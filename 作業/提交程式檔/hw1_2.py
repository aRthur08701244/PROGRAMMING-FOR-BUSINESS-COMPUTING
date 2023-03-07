x1 = int(input())
p1 = int(input())
x2 = int(input())
p2 = int(input())
t = int(input())
b = int(input())

money_total = x1*p1 + x2*p2
money_remain = t - money_total
ticket_total = x1 + x2
ticket_remain = b - ticket_total


if money_total <= t:
    if ticket_total <= b:
        print(str(ticket_remain) + "," + "$" + str(money_remain))
    else:
        print("-1" + "," + "$" + str(money_remain))
else:
    if ticket_total <= b:
        print(str(ticket_remain) + "," + "-2")
    else:
        print("-1" + "," + "-2")