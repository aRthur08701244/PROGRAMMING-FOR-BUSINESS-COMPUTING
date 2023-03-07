# "C:\Users\kmes8\OneDrive\桌面\商管程\作業\提交程式檔\news_title.txt"
# "C:\Users\kmes8\OneDrive\桌面\商管程\作業\提交程式檔\news_dict.txt"
# "C:\Users\kmes8\OneDrive\桌面\商管程\作業\提交程式檔\company_category.txt"
import operator

# input the position of file
fn1 = input()
fn2 = input()
fn3 = input()
interest = input().split(',')
k = interest[0]  # kind
q = int(interest[1])  # quantity
r = interest[2].split(':')  # rate_list

for i in range(len(r)):
    r[i] = int(r[i])

# open the file
title = open(fn1, "r", encoding="utf-8")
n_dict = open(fn2, "r", encoding="utf-8")
category = open(fn3, "r", encoding="utf-8")

news_title = []
news_dict = dict()
company_category = dict()

# split title, n_dict, and category to list or dictionary
for i in title:
    i = i.strip()
    news_title.append(i)

for i in n_dict:
    i = i.split(' ')
    news_dict[i[0]] = int(i[1].strip())

for i in category:
    i = i.split(' ')
    if i[1].strip() not in company_category:
        company_category[i[1].strip()] = [i[0]]
    else:
        company_category[i[1].strip()].append(i[0])

interest_company_list = []
if k in company_category:
    interest_company_list = company_category[k]

# create a dictionary with key interesting company and value the score it get
company_score = dict()

for i in news_title:  # search from each title
    for j in interest_company_list:  # count every score of the interesting company
        if i.count(j) > 0:  # if the interesting company is in the news_title
            for m in news_dict:  # verify every news_dict(keyword)
                if i.count(m) > 0:  # if the keyword is in the news_title
                    if j not in company_score:  # if the company_score hasn't the key that names j
                        company_score[j] = i.count(m) * news_dict[m]
                    else:
                        company_score[j] = company_score[j] + i.count(m) * news_dict[m]


company_score = sorted(company_score.items(), key=operator.itemgetter(1, 0), reverse=True)

# calculate how many to buy
if len(interest_company_list) > 0:
    rate_total = int()

    if len(company_score) >= len(r):
        for i in r:
            rate_total += i
        n_round = q // rate_total
        round_remain = q % rate_total

        num_to_buy = []

        for i in range(len(r)):
            num = n_round * r[i]
            if round_remain > r[i]:
                num += r[i]
                round_remain -= r[i]
            else:
                num += round_remain
                round_remain = 0
            num_to_buy.append(num)
    else:
        for i in range(len(company_score)):
            rate_total += r[i]
        n_round = q // rate_total
        round_remain = q % rate_total

        num_to_buy = []

        for i in range(len(company_score)):
            num = n_round * r[i]
            if round_remain > r[i]:
                print(num, r[i])
                num += r[i]
                round_remain -= r[i]
            else:
                num += round_remain
                round_remain = 0
            num_to_buy.append(num)

    for i in range(len(num_to_buy)):
        if num_to_buy[i] > 0:
            print(company_score[i][0] + "購買" + str(num_to_buy[i]) + "張")
else:
    print("NO_MATCH")

title.close()
n_dict.close()
category.close()
