# "C:\Users\kmes8\OneDrive\桌面\商管程\作業\提交程式檔\u.item"
# "C:\Users\kmes8\OneDrive\桌面\商管程\作業\提交程式檔\u.genre"
# input the position of file
fn1 = input()
fn2 = input()
movie_id = input()

# open the file
item = open(fn1, "r", encoding="ISO-8859-1")
genre = open(fn2, "r", encoding="ISO-8859-1")

item_list = []
genre_list = []

# split the item and genre to list
for i in item:
    i = i.strip()
    i = i.split('|')
    item_list.append(i)

for i in genre:
    i = i.strip('\n')
    if i == "":
        continue
    i = i.split('|')
    genre_list.append(i)

movie_genre_list = []
movie_name = str()

# search the useful information that we need
for i in item_list:
    if i[0] == movie_id:
        movie_name = i[1]
        for j in range(5, 24):
            if i[j] == '1':
                movie_genre_list.append(genre_list[j - 5][0])


movie_genre_str = ', '.join(movie_genre_list)

if movie_name == "":
    print("No movie found.")
else:
    print(movie_name + ': ' + movie_genre_str)

item.close()
genre.close()
