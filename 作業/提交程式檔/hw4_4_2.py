firststr = input()
secondstr = input()
thirdstr = input()


firststr = firststr.split(',')
weight = secondstr.split(',')
utility = thirdstr.split(',')

n = int(firststr[0])
B = int(firststr[1])
h = int(firststr[2])

for i in range(n):
    weight[i] = int(weight[i])
    utility[i] = int(utility[i])

covar_matrix = []
for i in range(n):
    covar_matrix.append(input())
    covar_matrix[i] = covar_matrix[i].split(',')
    for k in range(len(covar_matrix[i])):
        covar_matrix[i][k] = int(covar_matrix[i][k])

pickup = []  # i.e.[0, 1, 0, 1]
for i in range(n):
    pickup.append(0)

cur_item = -1  # current item
cur_u = int()  # current item's utility


for i in range(n):
    if ((utility[i] - h*covar_matrix[i][i]) > cur_u) & (weight[i] <= B):
        cur_u = utility[i] - h*covar_matrix[i][i]
        cur_item = i


if cur_item == -1:
    print(0)
else:  #  more round
    pickup[cur_item] = 1
    B -= weight[cur_item]


    cur_item_2 = -1  # 2nd item
    cur_u_2 = int()  # 2nd item's utility

    for i in range (n):
        if pickup[i] == 1:
            continue
        elif ((utility[i] - h*covar_matrix[i][i] - h*covar_matrix[i][cur_item]*2) > cur_u_2) & (weight[i] <= B):
            cur_item_2 = i
            cur_u_2 = utility[i] - h*covar_matrix[i][i] - h*covar_matrix[i][cur_item]*2
        elif ((utility[i] - h*covar_matrix[i][i] - h*covar_matrix[i][cur_item]*2) == cur_u_2) & (weight[i] <= B) & (weight[i] < weight[cur_item_2]):
            cur_item_2 = i
            cur_u_2 = utility[i] - h*covar_matrix[i][i] - h*covar_matrix[i][cur_item]*2

    if cur_item_2 >= 0:
        pickup[cur_item_2] = 1
        B -= weight[cur_item_2]

        cur_item_3 = -1
        cur_u_3 = int()

        for i in range(n):
            if pickup[i] == 1:
                continue
            elif((utility[i] - h*covar_matrix[i][i] - h*covar_matrix[i][cur_item]*2 - h*covar_matrix[i][cur_item_2]*2 - h*covar_matrix[cur_item][cur_item_2]) > cur_u_3) & (weight[i] <= B):
                cur_item_3 = i
                cur_u_3 = utility[i] - h*covar_matrix[i][i] - h*covar_matrix[i][cur_item]*2 - h*covar_matrix[i][cur_item_2]*2 - h*covar_matrix[cur_item][cur_item_2]
            elif((utility[i] - h*covar_matrix[i][i] - h*covar_matrix[i][cur_item]*2 - h*covar_matrix[i][cur_item_2]*2 - h*covar_matrix[cur_item][cur_item_2]) == cur_u_3) & (weight[i] <= B) & (weight[i] < weight[cur_item_3]):
                cur_item_3 = i
                cur_u_3 = utility[i] - h*covar_matrix[i][i] - h*covar_matrix[i][cur_item]*2 - h*covar_matrix[i][cur_item_2]*2 - h*covar_matrix[cur_item][cur_item_2]

        if cur_item_3 >= 0:
            pickup[cur_item_3] = 1
            B -= weight[cur_item_3]


    num_item = sum(pickup)

    for i in range(n):
        if (pickup[i] == 1) & (num_item != 1):
            print(i + 1, end=",")
            num_item -= 1
        elif (pickup[i] == 1) & (num_item == 1):
            print(i + 1, end="")