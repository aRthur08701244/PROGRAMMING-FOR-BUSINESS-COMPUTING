import operator


# define histogram
def histogram(seq, dictionary):
    for element in seq:
        if element not in dictionary:
            dictionary[element] = 1
        else:
            dictionary[element] += 1

# input file position
# "C:\Users\kmes8\OneDrive\桌面\商管程\作業\提交程式檔\Gossiping-QA-Dataset.txt"
fn = input()

# open file
gossip = open(fn, "r", encoding="utf-8")

# input keyword
keyword = input()

gossip_list = []

for_dict = dict()
back_dict = dict()

# split the file to list
for i in gossip:
    i = i.split('\t')
    gossip_list.append(i[0].strip())
    gossip_list.append(i[1].strip())

# record the forward and backward words of the key word
for i in gossip_list:
    while True:
        if i.find(keyword) == 0:
            if (i.find(keyword) + len(keyword)) < len(i):
                histogram(i[i.find(keyword) + len(keyword)], back_dict)
            i = i[:i.find(keyword)] + i[i.find(keyword) + len(keyword):]

        elif i.find(keyword) > 0:
            if (i.find(keyword) + len(keyword)) < len(i):
                histogram(i[i.find(keyword) - 1], for_dict)
                histogram(i[i.find(keyword) + len(keyword)], back_dict)
            else:
                histogram(i[i.find(keyword) - 1], for_dict)
            i = i[:i.find(keyword)] + i[i.find(keyword) + len(keyword):]

        elif keyword not in i:
            break

# sort the dictionary
for_sorted_items = sorted(for_dict.items(), key=(operator.itemgetter(1, 0)), reverse=True)

back_sorted_items = sorted(back_dict.items(), key=operator.itemgetter(1, 0), reverse=True)

# print the result
print("熱門前一個字:")

if len(for_sorted_items) >= 10:
    for i in range(10):
        print(for_sorted_items[i][0] + "---" + keyword)
else:
    for i in range(len(for_sorted_items)):
        print(for_sorted_items[i][0] + "---" + keyword)

print("熱門下一個字:")

if len(back_sorted_items) >= 10:
    for i in range(10):
        print(keyword + "---" + back_sorted_items[i][0])

else:
    for i in range(len(back_sorted_items)):
        print(keyword + "---" + back_sorted_items[i][0])

# close the file
gossip.close()
