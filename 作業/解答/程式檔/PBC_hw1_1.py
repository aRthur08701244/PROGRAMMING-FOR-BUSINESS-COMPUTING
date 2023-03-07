# input
adult_num = int(input())  # 全票數量
adult_price = int(input())  # 全票價格
student_num = int(input())  # 學生票數量
student_price = int(input())  # 學生票價格
money = int(input())  # 擁有的鈔票面額

ttl_price = student_price*student_num + adult_price*adult_num  # 所需要付的金額
if money >= ttl_price:  # 夠付
    remaining = money - ttl_price  # 要找回的錢
    print("$"+str(remaining))
else:  # 不夠付
    print(-1)
