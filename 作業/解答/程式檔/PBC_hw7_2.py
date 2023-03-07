movie_data_fn = input().strip()  # u.item 路徑
genre_fn = input().strip()  # u.genre 路徑
qm_id = input().strip()  # 電影ID


genre_id2name = {}  # 存類別ID與類別名稱的dictionary
with open(genre_fn, 'r', encoding='ISO-8859-1') as f:
    for aline in f:
        aline = aline.strip().split('|')
        if len(aline) < 2:
            continue
        genre_id2name[aline[1]] = aline[0]

found = False  # 是否有找到該部電影
with open(movie_data_fn, 'r', encoding='ISO-8859-1') as f:
    for aline in f:
        aline = aline.strip().split('|')
        if aline[0] == qm_id:
            found = True
            break

if found:
    genre_list = []  # 存放該部電影的所有類別
    for i in range(len((aline[5:]))):
        if aline[5:][i] == '1':
            genre_list.append(genre_id2name[str(i)])

    genre_str = ", ".join(genre_list)
    moviename = aline[1]
    print("{}: {}".format(moviename, genre_str))
else:
    print("No movie found.")
