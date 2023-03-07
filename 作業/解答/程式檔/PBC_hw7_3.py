# 3.

# 將句子斷句
def split_sentence(sentence):
    for word in dictionary_list[0]:
        candidate_word = []
        if word in sentence:  # 當前輸入的句子找到字了
            candidate_word.append([sentence.find(word), word])
            for word_ in dictionary_list[0]:
                if word_ in sentence and len(word) == len(word_):
                    candidate_word.append([sentence.find(word_), word_])
            word = sorted(candidate_word)[0][1]
            index = sentence.find(word)
            if index > 0:  # 確保丟入的不是空字串
                split_sentence(sentence[:index])  # 句子的前半繼續去斷詞
            temp.append(sentence[index: index+len(word)])  # 找到的詞加進去 temp
            if index+len(word) < len(sentence):
                split_sentence(sentence[index+len(word):])  # 句子的後半繼續去斷詞
            break
        else:
            # 如果確定當前的這個句子裡面沒有任何可以斷的詞了
            # 就把他加進去 temp
            sentenc_no_word_in_dict = True
            for word in dictionary_list[0]:
                if word in sentence:
                    sentenc_no_word_in_dict = False
            if sentenc_no_word_in_dict:
                temp.append(sentence)
                break
                    
news_title_path = input()
news_dict_path = input()
company_category_path = input()
category_stock_ratio = input()

sentence_list = []  # 裝新聞標題的list
dictionary_list = [[], []]  # 裝辭典的list
company2category_dict = {}  # 裝公司的dict
category2company_dict = {}  # 裝公司的dict

# 讀檔案
with open(news_title_path, 'r', encoding='utf-8') as dataset:
    for data in dataset:
        sentence = data.rstrip("\n").replace(' ', '')  # 移除空格
        sentence_list.append(sentence)
# 讀檔案
with open(news_dict_path, 'r', encoding='utf-8') as dataset:
    dictionary_length_list = []
    temp_dict = {}
    for data in dataset:
        data = data.rstrip("\n").split(' ')  # 依照空格切割出 d & w
        dictionary_length_list.append([len(data[0]), data[0]])
        temp_dict[data[0]] = int(data[1])  # '漲': 1  長度為一
    dictionary_length_list.sort(reverse=True)  # 依照長到短排序
    for word_length in dictionary_length_list:
        dictionary_list[0].append(word_length[1])  # 儲存關鍵字
        dictionary_list[1].append(temp_dict[word_length[1]])  # 關鍵字權重


# 讀檔案
with open(company_category_path, 'r', encoding='utf-8') as dataset:
    for data in dataset:
        data = data.rstrip("\n").split(' ')  # 依照空格切割出 d & w
        company2category_dict[data[0]] = data[1]  # '台積電': 半導體股
        if data[1] in category2company_dict.keys():
            category2company_dict[data[1]].append(data[0])
        else:
            category2company_dict[data[1]] = [data[0]]

# 處理產業類別、購買的總張數、購買的比率
temp_ = category_stock_ratio.split(',')
category = temp_[0]
stock_to_buy = temp_[1]
ratio = temp_[2]


stock_to_buy = int(stock_to_buy)
ratio = [int(i) for i in ratio.split(":")]

company_score_dict = {}  # 紀錄公司以及他目前的總分
# 斷句
for sentence in sentence_list:
    temp = []
    split_sentence(sentence)
    # temp會長這樣 ['台積電' 甩尾拉高', '台股5日線', '失而復得', '漲', '39點收12917點']
    # 計算分數
    score = 0
    for i in temp:
        if i in dictionary_list[0]:
            index = dictionary_list[0].index(i)
            score += dictionary_list[1][index]

    # 找公司並且加上分數
    sentence_company_list = []  # 這句sentence中有哪些公司
    for company in company2category_dict.keys():
        if company in sentence:
            sentence_company_list.append(company)
    for company in sentence_company_list:
        if company in company_score_dict.keys():
            company_score_dict[company] += score  # 這些公司都要加上這句話的分數
        else:
            company_score_dict[company] = score

# 計算排名
company_order = []
if category not in category2company_dict.keys():
    print("NO_MATCH")  # no match 的情況
else:
    for company in category2company_dict[category]:
        company_order.append([company_score_dict[company], company])
    company_order = [i[1] for i in sorted(company_order, reverse=True)]

    # 計算購買張數
    if len(ratio) > len(company_order):
        ratio = ratio[:len(company_order)]  # 比率長度超過候選公司家數
    pack = stock_to_buy // sum(ratio)  # 商數
    remainder = stock_to_buy % sum(ratio)  # 餘數
    remainder_list = []  # ex. 4:2:1 餘5 會變成 [4,1,0]的list，表示各買幾張股票
    for i in ratio:
        if remainder > i:
            remainder_list.append(i)
            remainder -= i
        elif remainder > 0:
            remainder_list.append(remainder)
            remainder -= remainder
        else:
            remainder_list.append(0)
    tickets_total_order_list = []  # 依照排序後的各ticket要購買的總張數 ex.[8,3,1]
    for i in range(len(ratio)):
        tickets_total_order_list.append(ratio[i]*pack + remainder_list[i])

    # 印出解答
    for i in range(len(tickets_total_order_list)):
        if tickets_total_order_list[i] > 0:  # 購買0張不要印
            print(company_order[i] + "購買" + str(
                tickets_total_order_list[i]) + "張")
