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

cp_copy = copy.copy(cp)
cp_sorted = copy.copy(cp)
cp_sorted.sort(reverse=True)

qualified = []

for i in range(n):
    for k in range(n):
        if cp_sorted[i] == cp_copy[k]:
            qualified.append(k)
            cp_copy[k] = -1

for i in range(n):
    for k in range(i + 1, n):
        if (cp[qualified[i]] == cp[qualified[k]]) & (weight[qualified[i]] > weight[qualified[k]]):
            tem = qualified[i]
            qualified[i] = qualified[k]
            qualified[k] = tem

for i in range(len(qualified)):
    print(qualified[i])

