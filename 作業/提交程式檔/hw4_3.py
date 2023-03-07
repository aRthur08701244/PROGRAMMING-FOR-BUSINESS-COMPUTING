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
order_1 = []  # the order to be considered
pickup_1 = []  # whether to pack in bag

for i in range(n):
    weight[i] = int(weight[i])
    utility[i] = int(utility[i])
    cp.append(utility[i] / weight[i])
    pickup_1.append(0)

cp_copy = copy.copy(cp)
cp_sorted = copy.copy(cp)
cp_sorted.sort(reverse=True)

qualified_1 = []

for i in range(n):
    for k in range(n):
        if cp_sorted[i] == cp_copy[k]:
            qualified_1.append(k)
            cp_copy[k] = -1

for i in range(n):
    for k in range(i + 1, n):
        if (cp[qualified_1[i]] == cp[qualified_1[k]]) & (weight[qualified_1[i]] > weight[qualified_1[k]]):
            tem = qualified_1[i]
            qualified_1[i] = qualified_1[k]
            qualified_1[k] = tem

total_w_1 = int()
total_u_1 = int()

for i in range(n):
    if (total_w_1 + weight[qualified_1[i]]) <= B:
        total_w_1 += weight[qualified_1[i]]
        total_u_1 += utility[qualified_1[i]]
        pickup_1[qualified_1[i]] = 1

# 2nd

order_2 = []
pickup_2 = []

for i in range(n):
    pickup_2.append(0)

utility_copy = copy.copy(utility)
utility_sorted = copy.copy(utility)
utility_sorted.sort(reverse=True)

qualified_2 = []

for i in range(n):
    for k in range(n):
        if utility_sorted[i] == utility_copy[k]:
            qualified_2.append(k)
            utility_copy[k] = -1

for i in range(n):
    for k in range(i + 1, n):
        if (utility[qualified_2[i]] == utility[qualified_2[k]]) & (weight[qualified_2[i]] > weight[qualified_2[k]]):
            tem = qualified_2[i]
            qualified_2[i] = qualified_2[k]
            qualified_2[k] = tem

total_w_2 = int()
total_u_2 = int()

for i in range(n):
    if (total_w_2 + weight[qualified_2[i]]) <= B:
        total_w_2 += weight[qualified_2[i]]
        total_u_2 += utility[qualified_2[i]]
        pickup_2[qualified_2[i]] = 1

pickup = []
if total_u_1 >= total_u_2:
    pickup = pickup_1
else:
    pickup = pickup_2

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
