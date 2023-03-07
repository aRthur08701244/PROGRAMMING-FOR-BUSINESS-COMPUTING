day_count = int(input())  # 輸入睡眠時間的天數
num_sleeptime_greater_than_seven = 0  # 睡眠時間超過 7 小時的天數
total_sleep_time = 0  # 總睡眠時間

# 讀取 n 天的睡眠時間
for i in range(day_count):
    sleep_time = float(input())
    if sleep_time > 7:
        num_sleeptime_greater_than_seven += 1  # 紀錄睡眠時間超過 7 小時的天數
    total_sleep_time += sleep_time

avg_sleep_time = total_sleep_time / day_count  # 平均睡眠時間

# 決定三種面膜所需的數量

# 只要睡眠時間超過 7 小時就用檸檬美白面膜
lemon_mask = num_sleeptime_greater_than_seven
num_sleeptime_less_and_equal_to_seven = (day_count -
                                         num_sleeptime_greater_than_seven)
if avg_sleep_time <= 6:  # 平均睡眠小於等於 6 小時
    # 有幾天睡眠時間小於 7 小時就安排幾張蜜糖修復面膜
    honey_mask = num_sleeptime_less_and_equal_to_seven
    egg_mask = 0
else:
    # 有幾天睡眠時間小於 7 小時就安排幾張蛋白保濕面膜
    egg_mask = num_sleeptime_less_and_equal_to_seven
    honey_mask = 0

# 計算所需材料
lemon = lemon_mask * 1.5
oil = (lemon_mask*4) + (honey_mask*9)
honey = (honey_mask*18) + (egg_mask*6)
egg = egg_mask * 2

# 檸檬購買整數顆
if not (lemon % 1 == 0):
    lemon = (lemon // 1) + 1

# 雞蛋盒裝不拆售（一盒三顆）
if not (egg % 3 == 0):
    egg_box = (egg // 3) + 1
else:
    egg_box = egg // 3

# 雞蛋五顆以上打九折
if lemon >= 5:
    lemon = lemon * 0.9

money = (lemon*7) + (oil*0.6) + (honey*1.2) + (egg_box*25)
money = int(money)  # 無條件捨去且以整數表達

print(money)
