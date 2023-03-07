# input
pm_concentration = int(input())  # PM2.5濃度
temperature = int(input())  # 氣溫
dew_point = int(input())  # 露點溫度
threshold = float(input())  # 赴約臨界值

# 計算空汙影響赴約意願
air_pollution_will = 0.5  # 起始赴約意願值為0.5
if pm_concentration <= 35:  # PM2.5濃度小於等於35
    air_pollution_will += (100-pm_concentration) * 0.005
else:  # PM2.5濃度大於35
    air_pollution_will += (45-pm_concentration) * 0.02
# 如果值大於1或小於0，則為1或0
if air_pollution_will > 1:
    air_pollution_will = 1
if air_pollution_will < 0:
    air_pollution_will = 0

# 計算相對溼度影響赴約意願
humidity_will = 0.5  # 起始赴約意願值為0.5
relative_humidity = 100 - 5*(temperature-dew_point)  # 計算相對溼度
if relative_humidity <= 30:  # 相對溼度小於等於30
    humidity_will *= (110-relative_humidity) / 60
else:  # 相對溼度大於30
    humidity_will *= (90-relative_humidity) / 45
# 如果機率大於1或小於0，則為1或0
if humidity_will > 1:
    humidity_will = 1
if humidity_will < 0:
    humidity_will = 0

# 比較兩個赴約意願值，選擇較小者作為最終赴約意願值
if air_pollution_will <= humidity_will:
    date_will = air_pollution_will
else:
    date_will = humidity_will

# 輸出赴約意願值，依照規定輸出至小數點後第二位
print('{:.2f}'.format(date_will))
# 輸出是否赴約
if date_will >= threshold:
    print("Let's go together.")
else:
    print("I wouldn't go out with you.")
