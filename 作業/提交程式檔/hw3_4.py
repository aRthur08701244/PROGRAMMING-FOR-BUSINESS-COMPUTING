n = int(input())
secondstr = input()
thirdstr = input()
fourthstr = input()

second = secondstr.split(',')
third = thirdstr.split(',')
fourth = fourthstr.split(',')

dis_item = []
for i in range(len(second)):
    dis_item.append(int(second[i]))

price = []
for i in range(len(third)):
    price.append(int(third[i]))

amount = []
for i in range(len(fourth)):
    amount.append(int(fourth[i]))

amount_dis_item = []
for i in range(len(dis_item)):
    cur = dis_item[i]
    amount_dis_item.append(amount[cur - 1])

e_dis_count = int()

while True:  
    e_bool = True

    for i in range(len(amount_dis_item)):
        if amount_dis_item[i] >= 5:
            e_bool = True
        else:
            e_bool = False
            break

    if e_bool == True:
        e_dis_count += 1
        for i in range(len(amount_dis_item)):
            amount_dis_item[i] -= 5
    else:
        break

n_dis_count = int()
while True:  
    n_bool = True

    for i in range(len(amount_dis_item)):
        if amount_dis_item[i] >= 1:
            n_bool = True
        else:
            n_bool = False
            break

    if n_bool == True:
        n_dis_count += 1
        for i in range(len(amount_dis_item)):
            amount_dis_item[i] -= 1
    else:
        break

total_discount = int()
for i in range(len(dis_item)):
    total_discount += 0.2*5*e_dis_count*price[dis_item[i] - 1] + 0.1*n_dis_count*price[dis_item[i] -1]

original_price = int()
for i in range(n):
    original_price += price[i]*amount[i]

if (total_discount // 1000) > 0:
    print(str(int(original_price - total_discount)) + ',' + str(int(total_discount // 1000)))
else:
    print("So sad. I messed up.")
