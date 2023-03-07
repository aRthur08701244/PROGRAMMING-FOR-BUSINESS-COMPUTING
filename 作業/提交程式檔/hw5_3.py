strlist_1 = []
strlist_2 = []
while True:
    put = input()
    if put != "RECORDSTOP":
        strlist_1.append(put)
    else:
        break
while True:
    put = input()
    if put != "FUNCTIONSTOP":
        strlist_2.append(put)
    else:
        break

for i in range(len(strlist_1)):
    strlist_1[i] = strlist_1[i].split(',')
    for j in range(len(strlist_1[i])):
        if j != 0:
            strlist_1[i][j] = int(strlist_1[i][j])

for i in range(len(strlist_2)):
    strlist_2[i] = strlist_2[i].split()
    for j in range(len(strlist_2[i])):
        if j == 1:
            strlist_2[i][j] = strlist_2[i][j].split(',')
            for m in range(len(strlist_2[i][j])):
                strlist_2[i][j][m] = int(strlist_2[i][j][m])


def player_avg(seasons, player_number, records=strlist_1):
    h = 0
    ab = 0
    for i in range(len(seasons)):
        for j in range(len(records)):
            if (records[j][2] == seasons[i]) & (records[j][1] == int(player_number)):
                h += records[j][4]
                ab += records[j][3]

    return h/ab


def team_avg(seasons, team_name, records=strlist_1):
    h = 0
    ab = 0
    for i in range(len(seasons)):
        for j in range(len(records)):
            if (records[j][2] == seasons[i]) & (records[j][0] == team_name):
                h += records[j][4]
                ab += records[j][3]

    return h/ab


def best_player(seasons, records=strlist_1):
    best_player = []
    h_ab = 0
    for i in range(len(seasons)):
        best_player.append(0)
        for j in range(len(records)):
            if (records[j][2] == seasons[i]) & ((records[j][4] / records[j][3]) > h_ab):
                best_player[i] = records[j][1]
                h_ab = records[j][4] / records[j][3]
            elif (records[j][2] == seasons[i]) & ((records[j][4] / records[j][3]) == h_ab) & (records[j][1] < best_player[i]):
                best_player[i] = records[j][i]
                h_ab = records[j][4] / records[j][3]

    return best_player


def best_team(seasons, records=strlist_1):
    best_team = []
    h_ab = 0
    candidate = []
    for i in range(len(seasons)):
        best_team.append(0)
        candidate.append([])
        for j in range(len(records)):
            if records[j][2] == seasons[i]:
                whether_to_add_a_new_row = True

                for m in range(len(candidate[i])):
                    if records[j][0] == candidate[i][m][0]:
                        candidate[i][m][3] += records[j][3]
                        candidate[i][m][4] += records[j][4]
                        whether_to_add_a_new_row = False
                        break

                if whether_to_add_a_new_row == True:
                    candidate[i].append(records[j])

        for j in range(len(candidate[i])):
            if (candidate[i][j][4] / candidate[i][j][3]) > h_ab:
                best_team[i] = candidate[i][j][0]
                h_ab = candidate[i][j][4] / candidate[i][j][3]
            elif ((candidate[i][j][4] / candidate[i][j][3]) == h_ab) & (ord(candidate[i][j][0]) < ord(best_team[i])):
                best_team[i] = candidate[i][j][0]
                h_ab = candidate[i][j][4] / candidate[i][j][3]

    return best_team


def chop(avg):
    avg = int(avg*100) / 100
    return avg if avg > 0 else 0

for i in range(len(strlist_2)):
    if strlist_2[i][0] == '1':
        print(chop(player_avg(strlist_2[i][1], strlist_2[i][2])))
    elif strlist_2[i][0] == '2':
        print(chop(team_avg(strlist_2[i][1], strlist_2[i][2])))
    elif strlist_2[i][0] == '3':
        for j in range(len(best_player(strlist_2[i][1]))):
            if j == len(best_player(strlist_2[i][1])) - 1:
                print(best_player(strlist_2[i][1])[j])
            else:
                print(str(best_player(strlist_2[i][1])[j]) + ',', end='')

    elif strlist_2[i][0] == '4':
        for j in range(len(best_team(strlist_2[i][1]))):
            if j == len(best_team(strlist_2[i][1])) - 1:
                print(best_team(strlist_2[i][1])[j])
            else:
                print(str(best_team(strlist_2[i][1])[j]) + ',', end='')
