# 使用split將第一個input拆分開接著宣告變數存值
input_1 = input().split(',')
step_count, total_weight = int(input_1[0]), int(input_1[1])
# 使用split將第二個input拆分開接著用兩個list存值
input_2 = input().split(',')
step_list = input_2[:step_count]
price_list = input_2[step_count:]

# 初始化變數
final_price = final_weight = 0
last_step = new_step = 0
accumulate_weight = accumulate_price = 0

for index in range(step_count):
    new_step = int(step_list[index])
    price = int(price_list[index])

    interval = new_step - last_step
    # remain_weight > 0 則代表還沒滿足購買數量
    if remain_weight > 0:
        '''
        如果區間小於remain_weight則代表在此區間仍不會超過所需購買量，
        總金額直接加上這段區間的價格乘以區間長度
        '''
        if interval < remain_weight: 
            final_price += interval * price
            remain_weight -= interval

            accumulate_weight += interval
        '''
        如果區間大於remain_weight則代表在此區間就可以滿足購買量，
        總金額直接加上這段區間的價格乘以區間長度，接著繼續檢查
        是否會有更便宜的購買量
        '''
        else:
            # 計算剛好滿足最低購買時的價格
            final_price += remain_weight * price
            accumulate_weight += remain_weight
            final_weight = accumulate_weight

            # 計算目前這個區間若是繼續購買總價格是否會變低，若變低則採用新的購買量
            accumulate_price = final_price + (interval-remain_weight)*price
            accumulate_weight += (interval - remain_weight)
            remain_weight = remain_weight - interval
            if accumulate_price <= final_price:
                final_price = accumulate_price
                final_weight = accumulate_weight

    # 已經滿足最低購買量之後的區間，如果新的總價格小於等於原本的總價格，則採用新的購買量
    else:
        accumulate_price += interval * price
        accumulate_weight += interval
        if accumulate_price <= final_price:
            final_price = accumulate_price
            final_weight = accumulate_weight
    last_step = new_step
print(final_weight, final_price, sep=",")
