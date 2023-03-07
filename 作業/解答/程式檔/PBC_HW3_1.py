number = int(input())
while True:
    # 如果number是個位數，則乘以1000補上三個0
    if number < 10:
        number = number * 1000
    # 如果number是十位數，則乘以100補上兩個0
    elif number < 100:
        number = number * 100
    # 如果number是百位數，則乘以10補上一個0
    elif number < 1000:
        number = number * 10
    digit_list = []
    # 將數字的每一個位數拆開放進list
    for digit in str(number):
        digit_list.append(int(digit))
    # 將位數由大牌到小以及由小排到大
    digit_list.sort()
    number = 0
    # 根據題目的公式計算結果
    # 從排序好的list的尾巴取最大值，開頭取最小值
    for index in range(4):
        number += (digit_list[-(index+1)]-digit_list[index])\
         * 10**(3-index)
    # 若此輪結果得出6174則終止迴圈
    if number == 6174:
        print(number)
        break
    # 若此輪結果不是6174則印出本輪結果，並進入下一輪迴圈
    else:
        print(number, end=',')