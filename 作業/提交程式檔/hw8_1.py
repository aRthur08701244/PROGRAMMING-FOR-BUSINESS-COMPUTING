import operator

class Card:
    def __init__(self, suit, rank): 
        self.suit = suit
        self.rank = rank

rank_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']

firststr = input().split(',')
secondstr = input().split(',')
for i in range(len(secondstr)):
    if secondstr[i] == 'A':
        secondstr[i] = '1'
    elif secondstr[i] == 'J':
        secondstr[i] = '11'
    elif secondstr[i] == 'Q':
        secondstr[i] = '12'
    elif secondstr[i] == 'K':
        secondstr[i] = '13'

cardlist = ["first_card", "second_card", "third_card", "fourth_card", "fif_card"]

for i in range(len(cardlist)):
    cardlist[i] = Card(firststr[i], secondstr[i])

cardlist = sorted(cardlist, key=operator.attrgetter("rank"))

#for i in cardlist:
#    print(i.rank)

def g(cardlist):
    bl = bool()
    for i in range(len(cardlist) - 1):
        if cardlist[i].suit == cardlist[i + 1].suit:
            if i == (len(cardlist) - 2):
                for j in range(1, len(cardlist)):
                    if cardlist[j - 1].rank == rank_list[rank_list.index(cardlist[j].rank) - 1]:
                        if j == (len(cardlist) - 1):
                            bl = True
                    else:
                        break
        else:
            break

    return bl

def f(cardlist):
    bl = bool()
    for i in range(1, 14):
        if secondstr.count(str(i)) == 4:
            bl = True
            break
    return bl

def e(cardlist):
    bl = bool()
    for i in range(1, 14):
        if secondstr.count(str(i)) == 3:
            for j in range(1, 14):
                if j == i:
                    continue
                else:
                    if secondstr.count(str(j)) == 2:
                        bl = True
    return bl

def d(cardlist):
    bl = bool()
    for j in range(1, len(cardlist)):
        if cardlist[j - 1].rank == rank_list[rank_list.index(cardlist[j].rank) - 1]:
            if j == (len(cardlist) - 1):
                bl = True
        else:
            break

    return bl

def c(cardlist):
    bl = bool()
    for i in range(len(cardlist) - 1):
        if cardlist[i].suit == cardlist[i + 1].suit:
            if i == (len(cardlist) - 2):
                bl = True
        else:
            break

    return bl

def b(cardlist):
    bl = bool()
    for i in range(1, 14):
        if secondstr.count(str(i)) >= 2:
            bl = True
            break
    return bl

def a(cardlist):
    bl = bool()
    for i in cardlist:
        if i.rank == '1':
            bl = True
    return bl

point = 0

if g(cardlist) == True:
    point = 100
elif f(cardlist) == True:
    if secondstr.count('1') == 1:
        point = 21
    else:
        point = 20
elif e(cardlist) == True:
    point = 10
elif d(cardlist) == True:
    point = 5
elif c(cardlist) == True:
    point = 3
elif b(cardlist) == True:
    for i in range(1, 14):
        if secondstr.count(str(i)) >= 2:
            point = 2
            for j in range(1, 14):
                if j == i:
                    continue
                else:
                    if secondstr.count(str(j)) == 2:
                        point += 2
    if secondstr.count('1') == 1:
        point += 1
elif a(cardlist) == True:
    point = secondstr.count('1')


print(point)