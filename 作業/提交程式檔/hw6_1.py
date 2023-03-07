keyword = input()  # input the keyword
strlist = input()  # input strings
while True:
    put = input()
    if put != "INPUT_END":
        strlist += ' ' + put
    else:
        break

strlist = strlist.strip()  # strip the strings

total_test = bool()  # represent whether there is any keyewrd in the whole string
for j in range(len(strlist) - len(keyword) + 1):
    test = bool()  # represent whether there is probability that the jth letter of the whole string is contained in the keyword
    if keyword[0] == strlist[j]:  # if the jth letter is consistent with the first letter of the keyword

        if len(keyword) > 1:  # compare the following letter with the keyword
            for k in range(len(keyword) - 1):
                if keyword[k + 1] == strlist[j + k + 1]:
                    test = True
                    total_test = True
                else:
                    test = False
                    break

        elif len(keyword) == 1:
            test = True
            total_test = True

    if test == True:  # if the word in the string is keyword, print it out
        if (j >= 7) & (len(strlist) - j - len(keyword) >= 7):  # x(j-7)xxxxxx  j...(j+len(keyword)-1)  xxxxxxx(j+len(keyword)+6) -> (j-7 >= 0) & (j+len(keyword)+6 <= len(strlist)-1)
            if len(keyword) == 1:
                for m in range(j - 7, j + 7 + len(keyword)):
                    if m == j:
                        print("**" + strlist[m] + "**", end='')
                    else:
                        print(strlist[m], end='')
                print()
            else:
                for m in range(j - 7, j + 7 + len(keyword)):
                    if m == j:
                        print("**" + strlist[m], end='')
                    elif m == j + len(keyword) - 1:
                        print(strlist[m] + "**", end='')
                    else:
                        print(strlist[m], end='')
                print()
        elif (j < 7) & (len(strlist) - j - len(keyword) >= 7):  # j-7 < 0
            if len(keyword) == 1:
                for m in range(0, j + 7 + len(keyword)):
                    if m == j:
                        print("**" + strlist[m] + "**", end='')
                    else:
                        print(strlist[m], end='')
                print()
            else:
                for m in range(0, j + 7 + len(keyword)):
                    if m == j:
                        print("**" + strlist[m], end='')
                    elif m == j + len(keyword) - 1:
                        print(strlist[m] + "**", end='')
                    else:
                        print(strlist[m], end='')
                print()
        elif (j >= 7) & (len(strlist) - j - len(keyword) < 7):  # j+len(keyword)+6 > len(strlist)-1
            if len(keyword) == 1:
                for m in range(j - 7, len(strlist)):
                    if m == j:
                        print("**" + strlist[m] + "**", end='')
                    else:
                        print(strlist[m], end='')
                print()
            else:
                for m in range(j - 7, len(strlist)):
                    if m == j:
                        print("**" + strlist[m], end='')
                    elif m == j + len(keyword) - 1:
                        print(strlist[m] + "**", end='')
                    else:
                        print(strlist[m], end='')
                print()
        elif (j < 7) & (len(strlist) - j - len(keyword) < 7):  # j-7 < 0 # j+len(keyword)+6 > len(strlist)-1
            if len(keyword) == 1:
                for m in range(0, len(strlist)):
                    if m == j:
                        print("**" + strlist[m] + "**", end='')
                    else:
                        print(strlist[m], end='')
                print()
            else:
                for m in range(0, len(strlist)):
                    if m == j:
                        print("**" + strlist[m], end='')
                    elif m == j + len(keyword) - 1:
                        print(strlist[m] + "**", end='')
                    else:
                        print(strlist[m], end='')
                print()

if total_test == False:  # there is no keyword in the whole string
    print("NO_MATCH")