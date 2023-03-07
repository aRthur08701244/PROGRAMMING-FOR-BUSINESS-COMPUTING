range_count = int(input())  # 回合數
total_amount = int(input())  # 需要購買的量

expense = 0
previous_upper_bound = 0  # 紀錄當前級距的的下界

#  輸入 n 個 ti 以及 n 個 ri
for current_range in range(range_count):
    current_upper_bound = int(input())  # 作為此次級距的上界
    current_range_price = int(input())  # 此次級距的價位

    # 數量有超過下界且大於等於等於上界
    if (
        (total_amount > previous_upper_bound) and
        (total_amount >= current_upper_bound)
    ):
        amount_to_buy_in_current_range = (current_upper_bound -
                                          previous_upper_bound)

    # 數量有超過下界且小於上界
    elif ((total_amount > previous_upper_bound) and
          (total_amount < current_upper_bound)):
        amount_to_buy_in_current_range = total_amount - previous_upper_bound

    else:  # 數量小於等於下界
        amount_to_buy_in_current_range = 0

    expense += amount_to_buy_in_current_range * current_range_price
    previous_upper_bound = current_upper_bound

print(expense)
