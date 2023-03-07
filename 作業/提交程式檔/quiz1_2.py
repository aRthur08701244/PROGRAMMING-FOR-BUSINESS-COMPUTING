# input
first_input = input()
second_input = input()

# split the str
first_lst = first_input.split(',')
lst_customer = second_input.split(',')

# transform the lst_customer
for i in range(len(lst_customer)):
    lst_customer[i] = int(lst_customer[i])

meal_p1 = int(first_lst[0])
drink_p2 = int(first_lst[1])
discount = int(first_lst[2])
num_customer = int(first_lst[3])

# set the variable
num_meal = int()
num_drink = int()
num_discount = int()
price = int()

for i in range(num_customer):
    if lst_customer[i] == 1:
        num_meal += 1
    elif lst_customer[i] == 2:
        num_drink += 1
    elif lst_customer[i] == 3:
        num_meal += 1
        num_drink += 1
        num_discount += 1

# calculate the cost
price = num_meal*meal_p1 + num_drink*drink_p2 - num_discount*discount

if int(price) < 0:
    price = 0

# print them out
print(str(num_meal) + ',' + str(num_drink) + ',' + str(price))
