# 使用split將第一個input拆分開接著宣告變數存值
input_1 = input().split(',')
step_count, total_weight = int(input_1[0]), int(input_1[1])
# 使用split將第二個input拆分開接著用兩個list存值
input_2 = input().split(',')
step_list = input_2[:step_count]
price_list = input_2[step_count:]

# 初始化變數
total_price = 0
last_step = 0
new_step = 0

for index in range(step_count):
    new_step = int(step_list[index])
    price = int(price_list[index])
    # 每一輪迴圈中都計算新的區間
    interval = new_step - last_step
    # 如果total_weight > 0 則代表還沒滿足購買數量
    if total_weight > 0:
        '''
        如果區間小於等於total_weight則代表在此區間仍不會超過所需購買量，
        總金額直接加上這段區間的價格乘以區間長度
        '''
        if interval <= total_weight:
            total_price += interval * price
            total_weight = total_weight - interval
        '''
        如果區間大於total_weight則代表在這個區間就可以滿足購買量，
        總金額加上剩餘的購買量乘以此區間價格
        '''
        else:
            total_price += total_weight * price
            total_weight = total_weight - new_step
    # 在下一輪之前將這一輪的step存下
    last_step = new_step

print(total_price)
