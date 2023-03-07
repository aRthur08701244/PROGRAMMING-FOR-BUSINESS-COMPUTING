# HW4_1 背包問題-1
# 接收輸入
object_num_and_weight_limit = input().split(',')
object_num = int(object_num_and_weight_limit[0])
weight_limit = int(object_num_and_weight_limit[1])

weights_list = input().split(',')
value_list = input().split(',')
object_list = input().split(',')

# 設定總重量與總效用
total_weights = 0
total_value = 0


for i in range(object_num):
    weights_list[i] = int(weights_list[i])
    value_list[i] = int(value_list[i])
    object_list[i] = int(object_list[i])
    # 計算重量與效用
    total_weights += weights_list[i] * object_list[i]
    total_value += value_list[i] * object_list[i]

# 檢查是否超過背包重量限制，輸出結果
if total_weights <= weight_limit:
    print(total_weights, total_value, sep=',')
else:
    print(-1)
