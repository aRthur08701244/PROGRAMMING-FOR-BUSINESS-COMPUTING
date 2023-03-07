# HW4_4
# 接收輸入
investnum_budget_risk = input().split(',')
funds_list = input().split(',')
reward_list = input().split(',')

investnum = int(investnum_budget_risk[0])
budget = int(investnum_budget_risk[1])
risk = int(investnum_budget_risk[2])


for i in range(investnum):
    funds_list[i] = int(funds_list[i])
    reward_list[i] = int(reward_list[i])

covariance_mat = []
for i in range(investnum):
    cov = input().split(',')
    for j in range(len(cov)):
        cov[j] = int(cov[j])
    covariance_mat.append(cov)

''' 演算法開始 '''
remain_money = budget
result = []

# 停止條件為剩下的資金不足以買任何投資標的 或 已買完所有投資標的 或 最大目標函數值<=0
while(len(result) != investnum):
    target_function_value_list = []

    for i in range(investnum):  # 演算法每次都看所有投資組合
        if i in result:
            target_function_value_list.append(0)
            continue
        target_function_value = reward_list[i] - risk*covariance_mat[i][i]
        for j in result:  # 看當下這個投資標的與之前選擇的
            target_function_value -= risk*(covariance_mat[i][j] +
                                           covariance_mat[j][i])

        target_function_value_list.append(target_function_value)

    # 判斷要選哪個投資標的
    for i in range(len(target_function_value_list)):  # 超過剩餘資金的目標函數設為0，就不會選到了
        if funds_list[i] > remain_money:
            target_function_value_list[i] = 0
    find_max = sorted(target_function_value_list)
    find_max.reverse()
    largest_target_value = find_max[0]

    # print(target_function_value_list)

    # 判斷跳出迴圈條件，最大目標函數值<=0，可跳出迴圈，因為目標函數值不會再變大了
    if largest_target_value <= 0:
        break

    # 選擇w最小的投資標的
    least_funds_index = target_function_value_list.index(largest_target_value)

    for i in range(len(target_function_value_list)):
        if target_function_value_list[i] == largest_target_value \
                and funds_list[i] < funds_list[least_funds_index]:
            least_funds_index = i

    result.append(least_funds_index)
    remain_money -= funds_list[least_funds_index]

    # 判斷跳出迴圈條件，剩下的資金不足以買任何投資標的
    remain_w = []
    for i in range(len(funds_list)):
        if i not in result:
            remain_w.append(funds_list[i])

    if len(result) == investnum:
        break
    if len(remain_w) > 0:
        min_remain_w = sorted(remain_w)[0]
        if remain_money < min_remain_w:
            break

# 輸出結果
result = sorted(result)

for i in range(len(result)):
    if i == len(result) - 1:
        print(result[i] + 1)
    else:
        print(result[i] + 1, end=',')
if len(result) == 0:
    print(0)
