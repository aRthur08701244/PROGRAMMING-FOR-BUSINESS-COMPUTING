strlist = []
while True:
    strin = input()
    
    if strin == "INPUTSTOP":
        break

    if strin.count('\"') % 2 == 0:
        counter = 0
        for i in range(len(strin)):
            if (strin[i] == '\"') & (counter % 2 == 0):
                strin = strin[:i] + '「' + strin[i + 1:]
                counter += 1
            elif (strin[i] == '\"') & (counter % 2 == 1):
                strin = strin[:i] + '」' + strin[i + 1:]
                counter += 1

    else:
        counter = 0
        n_round = strin.count('\"')
        for i in range(len(strin)):
            if counter == n_round - 1:
                break
            if (strin[i] == '\"') & (counter % 2 == 0):
                strin = strin[:i] + '「' + strin[i + 1:]
                counter += 1
            elif (strin[i] == '\"') & (counter % 2 == 1):
                strin = strin[:i] + '」' + strin[i + 1:]
                counter += 1

    strin = ' '.join(strin.split())
    strin.strip()
    for i in range(len(strin)):
        if i > (len(strin) - 1):
            break
        if (strin[i] == ',') or (strin[i] == ':') or (strin[i] == '.'):
            if i > 0:
                if i != len(strin) - 1:
                    if strin[i - 1] == ' ':
                        strin = strin[:i - 1] + strin[i:]
                    elif strin[i + 1] != ' ':
                        strin = strin[:i + 1] + ' ' + strin[i + 1:]
                else:
                    if strin[i - 1] == ' ':
                        strin = strin[:i - 1] + strin[i:]
            else:
                if i != len(strin) - 1:
                    if strin[i + 1] != ' ':
                        strin = strin[:i + 1] + ' ' + strin[i + 1:]

    strin.strip()

    strlist.append(strin)

for i in strlist:
    print(i)
