current_number = int(input())
result_string = ''

# 重複計算三次
for iteration_count in range(1, 4):
    units_digit = current_number % 10
    tens_digit = current_number // 10 % 10
    hundreds_digit = current_number // 100 % 10

    # 比較大小
    if hundreds_digit >= tens_digit:

        if tens_digit >= units_digit:  # 百位數大於等於十位數大於等於個位數
            max_number = hundreds_digit
            median_number = tens_digit
            min_number = units_digit

        elif units_digit >= hundreds_digit:  # 個位數大於等於百位數大於等於十位數
            max_number = units_digit
            median_number = hundreds_digit
            min_number = tens_digit

        else:  # 百位數大於等於個位數大於等於十位數
            max_number = hundreds_digit
            median_number = units_digit
            min_number = tens_digit
    else:
        if units_digit >= tens_digit:  # 個位數大於等於十位數大於等於百位數
            max_number = units_digit
            median_number = tens_digit
            min_number = hundreds_digit

        elif hundreds_digit >= units_digit:  # 十位數大於等於百位數大於等於個位數
            max_number = tens_digit
            median_number = hundreds_digit
            min_number = units_digit

        else:  # 十位數大於等於個位數大於等於百位數
            max_number = tens_digit
            median_number = units_digit
            min_number = hundreds_digit

    number_from_max_to_min = ((max_number*100) + (median_number*10) +
                              (min_number*1))
    number_from_min_to_max = ((min_number*100) + (median_number*10) +
                              (max_number*1))
    current_number = number_from_max_to_min - number_from_min_to_max

    if iteration_count == 3:
        print(current_number)
    else:
        print(current_number, end=",")
