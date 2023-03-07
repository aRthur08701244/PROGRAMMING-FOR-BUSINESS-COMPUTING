total_amount = int(input())   # 所需要購買的總公斤數
threshold_1 = int(input())     # 第一個級距的上限門檻
range_price_1 = int(input())  # 第一個級距的價位
threshold_2 = int(input())     # 第二個級距的上限門檻
range_price_2 = int(input())  # 第二個級距的價位
threshold_3 = int(input())     # 第三個級距的上限門檻
range_price_3 = int(input())  # 第三個級距的價位

expense = 0
amount_to_buy = total_amount  # 尚未購買的公斤數

if amount_to_buy > threshold_2:
    amount_to_buy_in_range_3 = amount_to_buy - threshold_2  # 落在第三級距的公斤數
    expense += amount_to_buy_in_range_3 * range_price_3
    amount_to_buy -= amount_to_buy_in_range_3

if amount_to_buy > threshold_1:
    amount_to_buy_in_range_2 = amount_to_buy - threshold_1  # 落在第二級距的公斤數
    expense += amount_to_buy_in_range_2 * range_price_2
    amount_to_buy -= amount_to_buy_in_range_2

amount_to_buy_in_range_1 = amount_to_buy
expense += amount_to_buy_in_range_1 * range_price_1

print(expense)
