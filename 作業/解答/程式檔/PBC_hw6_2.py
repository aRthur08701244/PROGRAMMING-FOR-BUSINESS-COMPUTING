# HW6_2 雙關鍵字比對
# obtain keyword from STDIN
maxgap = int(input())
key1 = input()
key2 = input()

# obtain s from STDIN
lines_all = []
while True:
    tmp1 = input()
    tmp1 = tmp1.strip()  # 去除空格
    if tmp1 == "INPUT_END":
        break
    lines_all.append(tmp1)


strall = " ".join(lines_all)  # 回傳以" "連接lines_all所有元素的字串


# 尋找關鍵字的所有索引值
def findall(key, s):
    allpos = []
    i = s.find(key)
    while i != -1:
        allpos.append(i)
        # 指定開始尋找的索引值為i+1，可以不斷往下尋找關鍵字。因為要找出所有關鍵字
        i = s.find(key, i+1)
    return allpos


# 以**標註關鍵字
def outputstr(fullstr, key1_len, key2_len, key1_pos, key2_pos, winlen=7):
    ind0 = max(0, key1_pos - winlen)  # 前7個字的起始index，若不足七個字元，有多少字元就印出多少字元
    # key1_pos
    ind1 = key1_pos + key1_len  # 第一個關鍵字終點index
    # key2_pos
    ind2 = key2_pos + key2_len  # 第一個關鍵字終點index
    ind3 = ind2 + winlen  # 後7個字的終點index，不足7個就只會印出剩下的

    msg = fullstr[ind0:key1_pos] + "**" + fullstr[key1_pos:ind1] + "**" + \
        fullstr[ind1:key2_pos] + "**" + fullstr[key2_pos:ind2] + "**" + \
        fullstr[ind2:ind3]

    return msg


pos1 = findall(key1, strall)
pos2 = findall(key2, strall)


nmatch = 0

# 對兩關鍵字的所有位置印出符合條件的字串
for posa in pos1:
    for posb in pos2:
        posdiff = posb - posa - len(key1)
        if posdiff >= 0 and posdiff <= maxgap:
            nmatch += 1
            print(outputstr(strall, len(key1), len(key2), posa, posb))

if nmatch == 0:
    print("NO_MATCH")
