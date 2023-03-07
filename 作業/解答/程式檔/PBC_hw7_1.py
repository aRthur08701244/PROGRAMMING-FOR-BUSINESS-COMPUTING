import operator

# 回傳一個list，紀錄 query 出現在句子中的哪幾個地方
def findall(key, s):
    allpos = []
    i = s.find(key)
    while i != -1:  # 一句話中可能會出現不只一次 key
        allpos.append(i)
        i = s.find(key, i+1)
    return allpos  # 回傳一個list，紀錄 query 出現在句子中的哪幾個地方
    
filepath = input().strip()
query = input().strip()

allsent = []  # 用來存所有的句子

with open(filepath, 'r', encoding='utf-8') as dataset:  # 讀檔
    for line in dataset:
        line = line.strip('\n')
        q, a = line.split('\t')
        # qa_pairs.append([q,a])
        allsent.append(q.strip(' '))
        allsent.append(a.strip(' '))
# print("資料筆數:",len(allsent))


result = []
nextchar = {}
prevchar = {}
for asent in allsent:
    iall = findall(query, asent)
    for i in iall:
        if i >= 0:
            result.append(asent)
            if (i + len(query)) < len(asent):  # 紀錄後面一個字
                tmp1 = asent[i+len(query)]
                try:
                    nextchar[tmp1] += 1
                except KeyError:
                    nextchar[tmp1] = 1
            if i > 0:  # 紀錄前面一個字
                tmp1 = asent[i-1]
                try:
                    prevchar[tmp1] += 1
                except KeyError:
                    prevchar[tmp1] = 1


sorted_nextchar = sorted(nextchar.items(), key=operator.itemgetter(1, 0),
                         reverse=True)  # 分別以頻率、字的內碼由大到小排序
sorted_prevchar = sorted(prevchar.items(), key=operator.itemgetter(1, 0),
                         reverse=True)

print("熱門前一個字:")
for aelem in sorted_prevchar[0:10]:
    print(aelem[0] + "---" + query)

print("熱門下一個字:")
for aelem in sorted_nextchar[0:10]:
    print(query + "---" + aelem[0])
