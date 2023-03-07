w = int(input())
keyword_1 = input()  # input the keyword_1
keyword_2 = input()
strlist = input()  # input strings
while True:
    put = input()
    if put != "INPUT_END":
        strlist += ' ' + put
    else:
        break

strlist = strlist.strip()  # strip the strings

total_test = bool()  # represent whether there is any keyword_1 in the whole string

for j in range(len(strlist) - len(keyword_1) + 1):
    test_1 = bool()  # represent whether there is probability that the jth letter of the whole string is contained in the keyword_1
    if keyword_1[0] == strlist[j]:  # if the jth letter is consistent with the first letter of the keyword_1

        if len(keyword_1) > 1:  # compare the following letter with the keyword_1
            for k in range(len(keyword_1) - 1):
                if keyword_1[k + 1] == strlist[j + k + 1]:
                    test_1 = True
                else:
                    test_1 = False
                    break

        elif len(keyword_1) == 1:
            test_1 = True
    
    if test_1 == True:
        for i in range(j + len(keyword_1), j + len(keyword_1) + w + 1):
            test_2 = bool()
            if keyword_2[0] == strlist[i]:  # if the jth letter is consistent with the first letter of the keyword_1

                if len(keyword_2) > 1:  # compare the following letter with the keyword_1
                    for k in range(len(keyword_2) - 1):
                        if keyword_2[k + 1] == strlist[i + k + 1]:
                            test_2 = True
                        else:
                            test_2 = False
                            break
                elif len(keyword_2) == 1:
                    test_2 = True
            #print(test_2)
            if test_2 == True:  # if the word in the string is keyword_1, print it out
                #print(test_1, test_2)
                total_test = True
                if (j >= 7) & (len(strlist) - i - len(keyword_2) >= 7):  # x(j-7)xxxxxx  j...(j+len(keyword_1)-1)  xxxxxxx(j+len(keyword_1)+6) -> (j-7 >= 0) & (j+len(keyword_1)+6 <= len(strlist)-1)
                    if len(keyword_1) == 1:
                        if len(keyword_2) == 1:  # len(k1) = len(k2) = 1
                            for m in range(j - 7, i + 7 + len(keyword_2)):
                                if (m == j) or (m == i):
                                    print("**" + strlist[m] + "**", end='')
                                else:
                                    print(strlist[m], end='')
                            print()
                        else:  # len(k1) = 1, len(k2) != 1
                            for m in range(j - 7, i + 7 + len(keyword_2)):
                                if m == j:
                                    print("**" + strlist[m] + "**", end='')
                                elif m == i:
                                    print("**" + strlist[m], end='')
                                elif m == i + len(keyword_2) - 1:
                                    print(strlist[m] + "**", end='')
                                else:
                                    print(strlist[m], end='')
                            print()
                    else:
                        if len(keyword_2) == 1:  # len(k1) != 1, len(k2) = 1
                            for m in range(j - 7, i + 7 + len(keyword_2)):
                                if m == i:
                                    print("**" + strlist[m] + "**", end='')
                                elif m ==j:
                                    print("**" + strlist[m], end='')
                                elif m == j + len(keyword_1) - 1:
                                    print(strlist[m] + "**", end='')
                                else:
                                    print(strlist[m], end='')
                            print()
                        else:  # len(k1) != 1, len(k2) != 1
                            for m in range(j - 7, i + 7 + len(keyword_2)):
                                if m == j:
                                    print("**" + strlist[m], end='')
                                elif m == j + len(keyword_1) - 1:
                                    print(strlist[m] + "**", end='')
                                elif m == i:
                                    print("**" + strlist[m], end='')
                                elif m == i + len(keyword_2) - 1:
                                    print(strlist[m] + "**", end='')
                                else:
                                    print(strlist[m], end='')
                            print()

                elif (j < 7) & (len(strlist) - i - len(keyword_2) >= 7):  # j-7 < 0
                    if len(keyword_1) == 1:
                        if len(keyword_2) == 1:  # len(k1) = len(k2) = 1
                            for m in range(0, i + 7 + len(keyword_2)):
                                if (m == j) or (m == i):
                                    print("**" + strlist[m] + "**", end='')
                                else:
                                    print(strlist[m], end='')
                            print()
                        else:  # len(k1) = 1, len(k2) != 1
                            for m in range(0, i + 7 + len(keyword_2)):
                                if m == j:
                                    print("**" + strlist[m] + "**", end='')
                                elif m == i:
                                    print("**" + strlist[m], end='')
                                elif m == i + len(keyword_2) - 1:
                                    print(strlist[m] + "**", end='')
                                else:
                                    print(strlist[m], end='')
                            print()
                    else:
                        if len(keyword_2) == 1:  # len(k1) != 1, len(k2) = 1
                            for m in range(0, i + 7 + len(keyword_2)):
                                if m == i:
                                    print("**" + strlist[m] + "**", end='')
                                elif m ==j:
                                    print("**" + strlist[m], end='')
                                elif m == j + len(keyword_1) - 1:
                                    print(strlist[m] + "**", end='')
                                else:
                                    print(strlist[m], end='')
                            print()
                        else:  # len(k1) != 1, len(k2) != 1
                            for m in range(0, i + 7 + len(keyword_2)):
                                if m == j:
                                    print("**" + strlist[m], end='')
                                elif m == j + len(keyword_1) - 1:
                                    print(strlist[m] + "**", end='')
                                elif m == i:
                                    print("**" + strlist[m], end='')
                                elif m == i + len(keyword_2) - 1:
                                    print(strlist[m] + "**", end='')
                                else:
                                    print(strlist[m], end='')
                            print()
                elif (j >= 7) & (len(strlist) - i - len(keyword_2) < 7):  # j+len(keyword_1)+6 > len(strlist)-1
                    if len(keyword_1) == 1:
                        if len(keyword_2) == 1:  # len(k1) = len(k2) = 1
                            for m in range(j - 7, len(strlist)):
                                if (m == j) or (m == i):
                                    print("**" + strlist[m] + "**", end='')
                                else:
                                    print(strlist[m], end='')
                            print()
                        else:  # len(k1) = 1, len(k2) != 1
                            for m in range(j - 7, len(strlist)):
                                if m == j:
                                    print("**" + strlist[m] + "**", end='')
                                elif m == i:
                                    print("**" + strlist[m], end='')
                                elif m == i + len(keyword_2) - 1:
                                    print(strlist[m] + "**", end='')
                                else:
                                    print(strlist[m], end='')
                            print()
                    else:
                        if len(keyword_2) == 1:  # len(k1) != 1, len(k2) = 1
                            for m in range(j - 7, len(strlist)):
                                if m == i:
                                    print("**" + strlist[m] + "**", end='')
                                elif m ==j:
                                    print("**" + strlist[m], end='')
                                elif m == j + len(keyword_1) - 1:
                                    print(strlist[m] + "**", end='')
                                else:
                                    print(strlist[m], end='')
                            print()
                        else:  # len(k1) != 1, len(k2) != 1
                            for m in range(j - 7, len(strlist)):
                                if m == j:
                                    print("**" + strlist[m], end='')
                                elif m == j + len(keyword_1) - 1:
                                    print(strlist[m] + "**", end='')
                                elif m == i:
                                    print("**" + strlist[m], end='')
                                elif m == i + len(keyword_2) - 1:
                                    print(strlist[m] + "**", end='')
                                else:
                                    print(strlist[m], end='')
                            print()
                elif (j < 7) & (len(strlist) - i - len(keyword_2) < 7):  # j-7 < 0 # j+len(keyword_1)+6 > len(strlist)-1
                    if len(keyword_1) == 1:
                        if len(keyword_2) == 1:  # len(k1) = len(k2) = 1
                            for m in range(0, len(strlist)):
                                if (m == j) or (m == i):
                                    print("**" + strlist[m] + "**", end='')
                                else:
                                    print(strlist[m], end='')
                            print()
                        else:  # len(k1) = 1, len(k2) != 1
                            for m in range(0, len(strlist)):
                                if m == j:
                                    print("**" + strlist[m] + "**", end='')
                                elif m == i:
                                    print("**" + strlist[m], end='')
                                elif m == i + len(keyword_2) - 1:
                                    print(strlist[m] + "**", end='')
                                else:
                                    print(strlist[m], end='')
                            print()
                    else:
                        if len(keyword_2) == 1:  # len(k1) != 1, len(k2) = 1
                            for m in range(0, len(strlist)):
                                if m == i:
                                    print("**" + strlist[m] + "**", end='')
                                elif m ==j:
                                    print("**" + strlist[m], end='')
                                elif m == j + len(keyword_1) - 1:
                                    print(strlist[m] + "**", end='')
                                else:
                                    print(strlist[m], end='')
                            print()
                        else:  # len(k1) != 1, len(k2) != 1
                            for m in range(0, len(strlist)):
                                if m == j:
                                    print("**" + strlist[m], end='')
                                elif m == j + len(keyword_1) - 1:
                                    print(strlist[m] + "**", end='')
                                elif m == i:
                                    print("**" + strlist[m], end='')
                                elif m == i + len(keyword_2) - 1:
                                    print(strlist[m] + "**", end='')
                                else:
                                    print(strlist[m], end='')
                            print()

if total_test == False:  # there is no keyword_1 in the whole string
    print("NO_MATCH")
