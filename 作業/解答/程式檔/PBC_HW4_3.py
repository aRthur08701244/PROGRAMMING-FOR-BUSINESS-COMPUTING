# HW4_3
# 接收輸入
object_num_and_weight_limit = input().split(',')
object_num = int(object_num_and_weight_limit[0])
weight_limit = int(object_num_and_weight_limit[1])

weights_list = input().split(',')
value_list = input().split(',')

''' 第一種演算法 '''
# 設定CP值list
cp_value_list = []

for i in range(object_num):
    weights_list[i] = int(weights_list[i])
    value_list[i] = int(value_list[i])
    # 計算CP值
    cp_value_list.append(value_list[i] / weights_list[i])

# 複製一份cp_value_list
cp_value_list_copy = []
for i in range(len(cp_value_list)):
    cp_value_list_copy.append(cp_value_list[i])

# 重量、編號、CP值的二維list，順序必須是重量、編號、CP值
# 這樣之後的排序可以讓順序自動是先重量後編號；不過這邊一樣是根據CP值做排序
weight_index_cp = []
for i in range(object_num):
    cur_max_index = i
    for j in range(object_num):
        if cp_value_list_copy[j] > cp_value_list_copy[cur_max_index]:
            cur_max_index = j
    # 當下最大的重量、編號、CP值
    cur_max_list = [weights_list[cur_max_index],
                    cur_max_index, cp_value_list_copy[cur_max_index]]
    weight_index_cp.append(cur_max_list)

    # 把cp_value_list內的CP值改成-1，這樣下一輪才會挑到第二大值、第三大值...直到全部排序完
    cp_value_list_copy[cur_max_index] = -1

cp_sort_index = []
for k in range(len(weight_index_cp)):
    cp_sort_index.append(weight_index_cp[k][1])


# 處理CP值重複情況(讓輕的會在前面，編號小的放前面)
for i in range(len(weight_index_cp)):
    if cp_value_list.count(cp_value_list[i]) > 1:  # 代表有重複
        # 上一個的效用一樣，代表前面已經處理過，跳過
        if i > 0:
            last_index = i - 1
            if weight_index_cp[i][2] == weight_index_cp[last_index][2]:
                continue

        # 概念上就是分成三個list，list1是重複的CP值以前的所有index；
        # list2是預備裝重新排序的重複的CP值index；
        # list3 = 重複的CP值以後的所有index
        # 將要排序的部分(calculate_area)重新排序後裝回list2，就完成了
        after_index = i+cp_value_list.count(cp_value_list[cp_sort_index[i]])
        equal_num = cp_value_list.count(cp_value_list[cp_sort_index[i]])

        list1 = cp_sort_index[:i]
        list2 = []
        list3 = cp_sort_index[after_index:]

        # calculate_area = cp_sort_index[i:(i+equal_num)]
        # 直接對weight_index_cp排序
        calculate_area = sorted(weight_index_cp[i:(i + equal_num)])
        # 把編號，也就是第二項塞進list2中
        for x in calculate_area:
            list2.append(x[1])

        cp_sort_index = list1 + list2 + list3

# 根據CP值index的順序，依序檢查是否超過背包重量限制，將index記錄在result_1中、
total_value_1 = 0
total_weights_1 = 0
result_1 = []

for i in cp_sort_index:
    cur_weights = total_weights_1 + weights_list[i]
    if cur_weights <= weight_limit:
        total_weights_1 += weights_list[i]
        total_value_1 += value_list[i]
        result_1.append(i)

result_1 = sorted(result_1)
# print(result_1, total_value_1)

''' 第二種演算法 '''
# 複製一份value_list
value_list_copy = []
for i in range(len(value_list)):
    value_list_copy.append(value_list[i])


# 重量、編號、效用的二維list，順序必須是重量、編號、效用
# 這樣之後的排序可以讓順序自動是先重量後編號；不過這邊一樣是根據效用做排序
weight_index_value = []
for i in range(object_num):
    cur_max_index = i
    for j in range(object_num):
        if value_list_copy[j] > value_list_copy[cur_max_index]:
            cur_max_index = j
    # 當下最大的重量、編號、效用
    cur_max_list = [weights_list[cur_max_index],
                    cur_max_index, value_list_copy[cur_max_index]]
    weight_index_value.append(cur_max_list)

    # 把value_list_copy內的效用改成-1，這樣下一輪才會挑到第二大值、第三大值...直到全部排序完
    value_list_copy[cur_max_index] = -1

value_sort_index = []
for k in range(len(weight_index_value)):
    value_sort_index.append(weight_index_value[k][1])

# 處理效用重複情況(讓輕的會在前面，編號小的放前面)
for i in range(len(weight_index_value)):
    if value_list.count(value_list[i]) > 1:  # 代表有重複
        # 上一個的效用一樣，代表前面已經處理過，跳過
        if i > 0:
            last_index = i - 1
            if weight_index_value[i][2] == weight_index_value[last_index][2]:
                continue

        # 概念上就是分成三個list，list1是重複的效用以前的所有index；
        # list2是預備裝重新排序的重複的效用index；
        # list3 = 重複的效用以後的所有index
        # 將要排序的部分(calculate_area)重新排序後裝回list2，就完成了
        after_index = i + value_list.count(value_list[value_sort_index[i]])
        equal_num = value_list.count(value_list[value_sort_index[i]])

        list1 = value_sort_index[:i]
        list2 = []
        list3 = value_sort_index[after_index:]

        # 直接對weight_index_value排序
        calculate_area = sorted(weight_index_value[i:(i+equal_num)])
        # 把編號，也就是第二項塞進list2中
        for x in calculate_area:
            list2.append(x[1])

        value_sort_index = list1 + list2 + list3

# 根據效用index的順序，依序檢查是否超過背包重量限制，將index記錄在result_2中
total_value_2 = 0
total_weights_2 = 0
result_2 = []

for i in value_sort_index:
    cur_weights = total_weights_2 + weights_list[i]
    if cur_weights <= weight_limit:
        total_weights_2 += weights_list[i]
        total_value_2 += value_list[i]
        result_2.append(i)
result_2 = sorted(result_2)
# print(result_2, total_value_2)

# 比較兩種演算法的總效用，兩者相同時用第二題的的演算法
if total_value_1 >= total_value_2:
    result = result_1
else:
    result = result_2


# 將result由小到大排序，印出結果。由於輸出格式是從1開始算，故輸出的結果須再加1
for i in range(len(result)):
    if i == len(result) - 1:
        print(result[i] + 1)
    else:
        print(result[i] + 1, end=',')
