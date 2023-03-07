product_amount = int(input())
set_index_list = input().split(",")
price_list = input().split(",")
amount_list = input().split(",")
set_amount = 9999
total_money_original = 0
set_price = 0
# 計算整套套組的價格
for index in set_index_list:
    index = int(index)
    set_price += int(price_list[index-1])
    if int(amount_list[index-1]) < set_amount:
        set_amount = int(amount_list[index-1])
# 預先將組成套組的數量扣除
for index in set_index_list:
    index = int(index)
    amount_list[index-1] = int(amount_list[index-1]) - set_amount
total_money = 0
# 將沒有組成套組或是不在套組內的商品的金額加總
for index in range(product_amount):
    total_money += int(price_list[index]) * int(amount_list[index])
# 計算打折前的價格
total_money_original = total_money
total_money_original += set_amount * set_price
# 計算打折後的價格
total_money += (set_amount//5*set_price*5) * 0.8
total_money += (set_amount%5*set_price) * 0.9
# 計算折扣金額
discount = total_money_original - total_money
print(discount)
# 計算招募到的人數
if discount >= 1000:
    print(int(total_money), int(discount//1000), sep=",")
else:
    print("So sad. I messed up.")
