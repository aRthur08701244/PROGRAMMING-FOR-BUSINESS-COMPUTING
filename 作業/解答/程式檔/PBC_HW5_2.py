import math


# 定義 printlines 函數
def printlines(linelist):
    for i, aline in enumerate(linelist):
        print("Line%d: %0.3f %0.3f %0.3f %0.3f" % (i, aline[0],
              aline[1], aline[2], aline[3]))


# 定義 rotate 函數
def rotate(lines, degree=90):
    theta = degree / 360 * math.pi * 2
    newlines = []

    # 將 lines 當中所有 line 都依照公式旋轉
    for line in lines:
        x1 = line[0]
        y1 = line[1]
        x2 = line[2]
        y2 = line[3]
        x1new = x1*math.cos(theta) - y1*math.sin(theta)
        y1new = x1*math.sin(theta) + y1*math.cos(theta)
        x2new = x2*math.cos(theta) - y2*math.sin(theta)
        y2new = x2*math.sin(theta) + y2*math.cos(theta)
        newlines.append([x1new, y1new, x2new, y2new])
    return newlines


# 讀取輸入
intype = "lines"
lines_all = []
while True:
    input_content = input()

    # 若輸入為 LINESTOP，則把 intype 設為 rotate
    if input_content == "LINESTOP":
        intype = "rotate"
        continue

    input_content = input_content.split(",")
    tmp = []
    for num in input_content:
        tmp.append(float(num))

    # 如果 intype 是 lines 代表輸入是線段，存入 lines_all
    if intype == "lines":
        lines_all.append(tmp)

    # 如果 intype 非 lines 則代表輸入是旋轉角度，用 degree 紀錄
    else:
        degree = tmp[0]
        break

# 將線段以及旋轉角度傳入 rotate 函數，最後使用 printlines 印出
fig2 = rotate(lines_all, degree)
printlines(fig2)
