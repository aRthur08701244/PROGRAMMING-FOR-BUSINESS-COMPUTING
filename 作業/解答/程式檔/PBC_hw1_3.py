# input
adult_num = int(input())  # 全票數量
adult_price = int(input())  # 全票價格
student_num = int(input())  # 學生票數量
student_price = int(input())  # 學生票價格
money = int(input())  # 擁有的鈔票面額
ticket_limit = int(input())  # 購票張數限制

output = ""  # 紀錄輸出內容

# 計算是否超過購票限制
ticket_num = adult_num + student_num  # 已購張數
if ticket_limit >= ticket_num:  # 未超過
    remaining_ticket = ticket_limit - ticket_num  # 尚可購買張數
    output += (str(remaining_ticket) + ",")

# 計算錢是否夠付
ttl_price = student_price*student_num + adult_price*adult_num  # 所需要付的金額
if money >= ttl_price:  # 夠付
    remaining_money = money - ttl_price  # 要找回的錢
    output += ("$" + str(remaining_money))

print(output)
