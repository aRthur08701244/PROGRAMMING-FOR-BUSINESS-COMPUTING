# 定義 printlines 函數
def printlines(linelist):
    for i, aline in enumerate(linelist):
        print("Line%d: %0.3f %0.3f %0.3f %0.3f" %
              (i, aline[0], aline[1], aline[2], aline[3]))


# 定義 plotshift 函數
def plotshift(linelist, xshift=0, yshift=0):
    outlist = []

    # 將 linelist 中所有 line 的 x, y 分別加上移動的量
    for line in linelist:
        newline = [line[0]+xshift, line[1]+yshift,
                   line[2]+xshift, line[3]+yshift]
        outlist.append(newline)

    return outlist


# 讀取輸入
intype = "lines"
lines_all = []
while True:
    input_content = input()

    # 若輸入為 LINESTOP，則把 intype 設為 shift
    if input_content == "LINESTOP":
        intype = "shift"
        continue
    input_content = input_content.split(",")
    tmp = []
    for num in input_content:
        tmp.append(float(num))

    # 如果 intype 是 lines 代表輸入是線段，存入 lines_all
    if intype == "lines":
        lines_all.append(tmp)
    # 如果 intype 非 lines 則代表輸入是偏移量，用 shift 紀錄
    else:
        shift = tmp
        break

# 將線段以及偏移量傳入 plotshift 函數，最後使用 printlines 印出
fig2 = plotshift(lines_all, shift[0], shift[1])
printlines(fig2)
