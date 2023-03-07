# HW6_1 字串比對
# obtain keyword from input
keyword = input()

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
        i = s.find(key, i+1)  # 指定開始尋找的索引值為i+1，因為要找出所有關鍵字
    return allpos


# 以**標註關鍵字
def highlight_str(fullstr, key1_len, key1_pos, winlen=7):
    ind0 = max(0, key1_pos - winlen)  # 前7個字的起始index，若不足七個字元，有多少字元就印出多少字元
    # key1_pos
    ind1 = key1_pos + key1_len  # 關鍵字終點index
    ind2 = ind1 + winlen  # 後7個字的終點index，不足7個就只會印出剩下的

    msg = "%s**%s**%s" % (fullstr[ind0:key1_pos], fullstr[key1_pos:ind1],
                          fullstr[ind1:ind2])
    return msg


posall = findall(keyword, strall)

if len(posall) == 0:
    print("NO_MATCH")
else:
    for apos in posall:
        print(highlight_str(strall, len(keyword), apos))
