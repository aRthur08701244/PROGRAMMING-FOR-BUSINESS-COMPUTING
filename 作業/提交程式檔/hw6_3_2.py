def insert_slash(string, index):
    return string[:index] + '/' + string[index:]

company = input().split(',')
keyword = input().split(',')
keyword.sort(key=len, reverse=True)
strlist = []

while True:
    put = input()
    if put != "INPUT_END":
        put = put.replace(' ', '')
        strlist.append(put)
    else:
        break

for i in range(len(strlist)):
    count = 0
    com_ver = []  # company verification
    for j in range(len(company)):
        com_ver.append(strlist[i].find(company[j]))
    for j in range(len(strlist[i])):  # print out the qualified company
        for k in range(len(com_ver)):
            if j == com_ver[k]:
                if count == len(com_ver) - com_ver.count(-1) - 1:
                    print(company[k] + ';', end='')
                else:
                    print(company[k] + ',', end='')
                count += 1

    for j in range(len(keyword)):  # print out the string
        if (strlist[i].find(keyword[j]) != -1):
            if (strlist[i].find(keyword[j]) == 0):  # the keyword is on the first word
                if strlist[i][strlist[i].find(keyword[j]) + len(keyword[j])] != '/':
                    strlist[i] = insert_slash(strlist[i], strlist[i].find(keyword[j]))
                    strlist[i] = insert_slash(strlist[i], int(strlist[i].find(keyword[j]) + len(keyword[j])))

            else:
                if (strlist[i].find(keyword[j]) + len(keyword[j])) > (len(strlist[i]) - 1):
                    if (strlist[i][strlist[i].find(keyword[j]) - 1] != '/'):
                        strlist[i] = insert_slash(strlist[i], strlist[i].find(keyword[j]))
                        strlist[i] = insert_slash(strlist[i], int(strlist[i].find(keyword[j]) + len(keyword[j])))
                else:
                    if (strlist[i][strlist[i].find(keyword[j]) - 1] != '/') & (strlist[i][strlist[i].find(keyword[j]) + len(keyword[j])] != '/'):
                        strlist[i] = insert_slash(strlist[i], strlist[i].find(keyword[j]))
                        strlist[i] = insert_slash(strlist[i], int(strlist[i].find(keyword[j]) + len(keyword[j])))

    if count != 0:
        strlist[i] = strlist[i].strip('/')
        print(strlist[i])

    if count == 0:
        print("NO_MATCH")