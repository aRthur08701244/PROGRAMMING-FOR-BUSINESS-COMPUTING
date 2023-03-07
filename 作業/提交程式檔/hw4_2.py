import copy

firststr = input()
secondstr = input()
thirdstr = input()
firststr = firststr.split(',')
weight = secondstr.split(',')
utility = thirdstr.split(',')

n = int(firststr[0])  # num of item
B = int(firststr[1])  # weight boundary

cp = []  # the cp value respectively
cp_sorted = []  # the cp value sorted
order = []  # the order to be considered
pickup = []  # whether to pack in bag

for i in range(n):
    weight[i] = int(weight[i])
    utility[i] = int(utility[i])
    cp.append(utility[i] / weight[i])
    order.append(0)
    pickup.append(0)

cp_sorted = copy.copy(cp)
cp_sorted.sort(reverse=True)

for i in range(n):
    for k in range(n):
        if cp_sorted[i] == cp[k]:
            order[k] = i

total_w = int()

for i in range(n):
    for k in range(n):
        if order[k] == i:
            situ = k  # the situation where the most valued thing located
    if (total_w + weight[situ]) <= B:
        total_w += weight[situ]
        pickup[situ] = 1

num_item = int()

for i in range(n):
    if pickup[i] == 1:
        num_item += 1

for i in range(n):
    if (pickup[i] == 1) & (num_item != 1):
        print(i + 1, end=",")
        num_item -= 1
    elif (pickup[i] == 1) & (num_item == 1):
        print(i + 1, end="")
