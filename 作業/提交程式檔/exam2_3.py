fn = input()
order = input()

data = open(fn, 'r', encoding='cp950')



datalist = []
result = []
for i in range(15):
    datalist.append([])
    result.append([])


for i in data:
    i = i.strip()
    i = i.split(',')
    #print(i[0])
    for j in range(len(i)):
        #print(i[j])
        datalist[j].append(i[j])


if order == "TYPE":
    for i in range(len(datalist)):
        for j in range(len(datalist[i])):
            try:
                datalist[i][j] = float(datalist[i][j])
                result[i].append(1)
            except Exception:
                result[i].append(0)

summ = []
for i in range(len(result)):
    summ.append(sum(result[i]))

for i in range(len(summ)):
    if summ[i] == len(result[i]):
        final = "numerical"
    else:
        final = "categorical"
    print(str(i) + ': ' + final)
