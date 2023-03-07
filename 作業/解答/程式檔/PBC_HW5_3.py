def chop(avg):
    avg = int(avg*100) / 100
    return avg if avg > 0 else 0


def player_avg(seasons, records, player_number):
    # 使用兩個變數來記錄球員的累計打擊數以及累計安打數
    ba_cumulated = 0
    h_cumulated = 0

    # 遍歷所有record，若球員號碼與球季都符合則累加打數以及安打數
    for record in records:
        if record[2] in seasons and record[1] == player_number:
            ba_cumulated += record[3]
            h_cumulated += record[4]

    # 如果累加打數不是 0，則計算打擊率並回傳
    if ba_cumulated != 0:
        avg = h_cumulated / ba_cumulated
        return chop(avg)
    # 如果累加打數是 0，則回傳 0
    else:
        return 0


def team_avg(seasons, records, team_name):
    # 使用兩個變數來記錄球員的累計打擊數以及累計安打數
    ba_cumulated = 0
    h_cumulated = 0
    # 遍歷所有record，若球隊代號與球季都符合則累加打數以及安打數
    for record in records:
        if record[2] in seasons and record[0] == team_name:
            ba_cumulated += record[3]
            h_cumulated += record[4]

    # 如果累加打數不是 0，則計算打擊率並回傳
    if ba_cumulated != 0:
        avg = h_cumulated / ba_cumulated
        return chop(avg)

    # 如果累加打數是 0，則回傳 0
    else:
        return 0


def best_player(seasons, records):
    # 使用兩個變數來記錄球隊的清單以及表現最好的球員清單
    team_list = []
    best_player_list = []

    # 遍歷所有球季
    for season in sorted(seasons):
        # 宣告空的 list 以及一個變數來紀錄打擊率最佳的球員清單以及最佳的打擊率
        best_avg_player = []
        best_avg = 0
        # 遍歷所有紀錄，並利用已經定義好的 player_avg 函數來計算各球季各球員的打擊率
        for record in records:
            if record[2] == season:
                avg = player_avg(seasons, [record], record[1])

                # 使用 best_avg_player 這個 list 來記錄打擊率最高的球員
                if avg > best_avg:
                    best_avg = avg
                    best_avg_player = []
                    best_avg_player.append(record)
                elif avg == best_avg:
                    best_avg_player.append(record)
        # 宣告空的 list 以及一個變數來紀錄打擊數最低的球員清單最低的打擊數
        best_ba_player = []
        min_ba = best_avg_player[0][3]

        # 遍歷 best_avg_player list 中的紀錄，取其中打數最少的紀錄
        for player in best_avg_player:
            if player[3] < min_ba:
                min_ba = player[3]
                best_ba_player.append(player[1])
            elif player[3] == min_ba:
                best_ba_player.append(player[1])

        # 依照球員號碼排序後的第一筆即為該球季表現最佳的球員
        best_ba_player.sort()
        best_player_list.append(best_ba_player[0])

    return best_player_list


def best_team(seasons, records):
    team_list = []
    # 遍歷所有 record 找到 records 中所有隊伍的代號
    for record in records:
        if record[0] not in team_list:
            team_list.append(record[0])
    team_list.sort()
    # 宣告一個空的 list 來紀錄表現最好的球隊
    best_team_list = []

    # 遍歷所有球季
    for season in sorted(seasons):
        # 宣告一個空的 list 以及一個變數來紀錄打擊率表現最好的球隊以及最佳的打擊率
        best_avg_team = []
        best_avg = 0

        # 遍歷所有球隊，並利用已經定義好的 team_avg 函數來計算各球季各球隊的打擊率
        for team in team_list:
            ba_cumulated = 0
            avg = team_avg([season], records, team)

            # 使用 best_avg_team 這個 list 來記錄打擊率最高的球隊
            if avg > best_avg:
                best_avg = avg
                best_avg_team = []

                # 累加該球隊在該球季的打數
                for record in records:
                    if record[0] == team and record[1] == season:
                        ba_cumulated += record[3]

                best_avg_team.append([team, ba_cumulated])
            elif avg == best_avg:

                # 累加該球隊在該球季的打數
                for record in records:
                    if record[0] == team and record[1] == season:
                        ba_cumulated += record[3]

                best_avg_team.append([team, ba_cumulated])

        # 用一個變數來存最小的累加打數
        min_ba_cumulated = best_avg_team[0][1]
        best_ba_team = []
        # 遍歷 best_avg_team list 中的紀錄，取其中打數最少的球隊
        for team in best_avg_team:
            if team[1] < min_ba_cumulated:
                min_ba_cumulated = team[1]
                best_ba_team.append(team[0])
            elif team[1] == min_ba_cumulated:
                best_ba_team.append(team[0])

        # 依照球隊代號排序後的第一筆即為該球季表現最佳的球隊
        best_ba_team.sort()
        best_team_list.append(best_ba_team[0])
    return best_team_list


records = []
record = ""
record = input()
# 如果輸入不是 RECORDSTOP 則繼續讀取輸入並存入 list
while record != "RECORDSTOP":
    record = record.split(",")
    records.append([record[0], int(record[1]), int(record[2]),
                    int(record[3]), int(record[4])])
    record = input()

action_to_do = ""
action_to_do = input()

# 如果輸入不是 FUNCTIONSTOP 則繼續讀取輸入並依據輸入來呼叫不同函數，並印出結果
while action_to_do != "FUNCTIONSTOP":
    parameter_list = action_to_do.split()
    if int(parameter_list[0]) == 1:
        seasons = parameter_list[1].split(",")
        for index in range(len(seasons)):
            seasons[index] = int(seasons[index])

        player_number = int(parameter_list[2])
        print(player_avg(seasons, records, player_number))

    elif int(parameter_list[0]) == 2:
        seasons = parameter_list[1].split(",")
        for index in range(len(seasons)):
            seasons[index] = int(seasons[index])

        team_name = parameter_list[2]
        print(team_avg(seasons, records, team_name))

    elif int(parameter_list[0]) == 3:
        seasons = parameter_list[1].split(",")
        for index in range(len(seasons)):
            seasons[index] = int(seasons[index])

        result = best_player(seasons, records)
        for index in range(len(result)-1):
            print(result[index], end=",")
        print(result[-1])

    elif int(parameter_list[0]) == 4:
        seasons = parameter_list[1].split(",")
        for index in range(len(seasons)):
            seasons[index] = int(seasons[index])

        result = best_team(seasons, records)
        for index in range(len(result)-1):
            print(result[index], end=",")
        print(result[-1])

    action_to_do = input()
