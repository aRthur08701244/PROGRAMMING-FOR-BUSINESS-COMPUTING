# HW4_2
# 接收輸入
object_num_and_weight_limit = input().split(',')
object_num = int(object_num_and_weight_limit[0])
weight_limit = int(object_num_and_weight_limit[1])

weights_list = input().split(',')
value_list = input().split(',')

# 設定CP值list
cp_value_list = []


for i in range(object_num):
    weights_list[i] = int(weights_list[i])
    value_list[i] = int(value_list[i])
    # 計算CP值
    cp_value_list.append(value_list[i] / weights_list[i])


# 複製一份cp_value_list
cp_value_list_copy = cp_value_list.copy()

# CP值、index的二維list，讓index根據CP值做排序
cp_index = []
for i in range(object_num):
    cur_max_index = i
    for j in range(object_num):
        if cp_value_list_copy[j] > cp_value_list_copy[cur_max_index]:
            cur_max_index = j
    # 當下最大的重量、編號、CP值
    cur_max_list = [cp_value_list_copy[cur_max_index], cur_max_index]
    cp_index.append(cur_max_list)

    # 把cp_value_list內的CP值改成-1，這樣下一輪才會挑到第二大值、第三大值...直到全部排序完
    cp_value_list_copy[cur_max_index] = -1

# 取得CP值由大到小的"index"
cp_sort_index = []
for k in range(len(cp_index)):
    cp_sort_index.append(cp_index[k][1])


# 根據CP值index的順序，依序檢查是否超過背包重量限制，將index記錄在result中
total_weights = 0
result = []
for i in cp_sort_index:
    cur_weights = total_weights + weights_list[i]
    if cur_weights <= weight_limit:
        total_weights += weights_list[i]
        result.append(i)

# 將result由小到大排序，印出結果。由於輸出格式是從1開始算，故輸出的結果須再加1
result = sorted(result)
for i in range(len(result)):
    if i == len(result) - 1:
        print(result[i] + 1)
    else:
        print(result[i] + 1, end=',')
