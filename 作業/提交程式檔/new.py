from tkinter import*
import pandas as pd
from tkinter import PhotoImage 

#介面: 遊戲開始
bridge_game = Toplevel()
bridge_game.title('澳門線下賭場－橋牌')  # 標題
bridge_game.resizable(0, 0)  # (0, 0) or (False, False) 代表不能縮放
bridge_game.geometry('600x500+400+200')  # 大小 寬X高 win.minsize(width=400, height=200)
bridge_game.config(bg='pink')  # background
# win.attributes("-alpha", 0.5) 1~0 1是完全不透明
# win.attributes("-topmost", 1) 置頂

# btn = Button(text="Click me", bg="skyblue")
# btn.config(bg="skyblue")
# btn.config(width=10, height=5)
# btn.pack() place() grid()

# photo = PhotoImage(file='backgroundpng.png')
# btn.config(image=photo)

# lb = Label(bg="black", fg="white", text="this is label")
# lb.pack()
# en = Entry()
# en.pack()

# 

#四人遊玩版本: fourgame()
def fourpgame():
    bridge_game.destroy()
    bridge = Tk()  # 建立主視窗 bridge.mainloop 常駐主視窗
    bridge.geometry("749x499")
    
    playernamefour = Label(bridge, text="請輸入玩家",font=30)
    playernamefour.pack(pady=30)

    onep = Entry(bridge)
    twop = Entry(bridge)
    threep = Entry(bridge)
    fourp = Entry(bridge)
    label1 = Label(bridge, text='玩家一')
    label2 = Label(bridge, text='玩家二')
    label3 = Label(bridge, text='玩家三')
    label4 = Label(bridge, text='玩家四')
    
    label1.pack()  # 封裝、放置、 布局
    onep.pack()
    label2.pack()
    twop.pack()
    label3.pack()
    threep.pack()
    label4.pack()
    fourp.pack()
    
    #遊戲開始
    def startfourgame():
        onep.focus_set()
        twop.focus_set()
        threep.focus_set()
        fourp.focus_set()
        
        firstp = onep.get()
        secondp = twop.get()
        thirdp = threep.get()
        fourthp = fourp.get()
        bridge.destroy()
        
        from random import shuffle 
        import numpy as np
        import pandas as pd
    

        #發牌
        while True:
            allcards = ['♣A','♣2','♣3','♣4','♣5','♣6','♣7','♣8','♣9','♣10','♣J','♣Q','♣K',
                    '♦A','♦2','♦3','♦4','♦5','♦6','♦7','♦8','♦9','♦10','♦J','♦Q','♦K',
                    '♥A','♥2','♥3','♥4','♥5','♥6','♥7','♥8','♥9','♥10','♥J','♥Q','♥K',
                    '♠A','♠2','♠3','♠4','♠5','♠6','♠7','♠8','♠9','♠10','♠J','♠Q','♠K']
            shuffle(allcards)
            player_1 = allcards[0:13]
            player_2 = allcards[13:26]
            player_3 = allcards[26:39]
            player_4 = allcards[39:52]
            player_1.sort()
            player_2.sort()
            player_3.sort()
            player_4.sort()
            ps1=0
            ps2=0
            ps3=0
            ps4=0
            record_1 = player_1[0:13]
            record_2 = player_2[0:13]
            record_3 = player_3[0:13]
            record_4 = player_4[0:13]
            
            for ba in range(13): #倒牌
                if player_1[ba][1]=='K':
                    ps1+=3
                elif player_1[ba][1]=='A':
                    ps1+=4
                elif player_1[ba][1]=='Q':
                    ps1+=2
                elif player_1[ba][1]=='J':
                    ps1+=1

            for ab in range(13):
                if player_2[ab][1]=='K':
                    ps2+=3
                elif player_2[ab][1]=='A':
                    ps2+=4
                elif player_2[ab][1]=='Q':
                    ps2+=2
                elif player_2[ab][1]=='J':
                    ps2+=1

            for ac in range(13):
                if player_3[ac][1]=='K':
                    ps3+=3
                elif player_3[ac][1]=='A':
                    ps3+=4
                elif player_3[ac][1]=='Q':
                    ps3+=2
                elif player_3[ac][1]=='J':
                    ps3+=1

            for ad in range(13):
                if player_4[ad][1]=='K':
                    ps4+=3
                elif player_4[ad][1]=='A':
                    ps4+=4
                elif player_4[ad][1]=='Q':
                    ps4+=2
                elif player_4[ad][1]=='J':
                    ps4+=1
            if ps1>=20 or ps1<4:
                continue
            elif ps2>=20 or ps2<4:
                continue
            elif ps3>=20 or ps3<4:
                continue
            elif ps4>=20 or ps4<4:
                continue
            else:
                break
        a=str(player_1)+('\n'+firstp)
        b=str(player_2)+('\n'+secondp)
        c=str(player_3)+('\n'+thirdp)
        d=str(player_4)+('\n'+fourthp)

        cardslist=['',a,'',b,'',c,'',d,'']
        cardlist=[player_1,player_2,player_3,player_4]
        
        
        #介面: 賭桌
        fourgame = Toplevel()
        photo = PhotoImage(file='C:\\Users\\kmes8\\OneDrive\\桌面\\商管程\\期末報告\\background.png')  # win.iconbitmap(".ico")
        imageLabel=Label(fourgame,image=photo,compound='center')
        imageLabel.pack()
        
        fourgame.geometry('1000x600')
        fourgame.resizable(0,0)
        instruction=Label(fourgame,text='你們好，歡迎來到橋牌遊戲，'+firstp+'與'+thirdp+'同隊；'+secondp+'與'+fourthp+'同隊')
        instruction.place(x=360,y=200)
        fourcards=Label(fourgame,text=cardslist[0])
        fourcards.place(x=308,y=160)
        
        
        #喊牌階段
        def go():
            nonlocal firstp
            nonlocal secondp
            nonlocal thirdp
            nonlocal fourthp
            fourcards.config(text=cardslist[1])
            del cardslist[0]
            if len(cardslist)==1:
                instruction.config(text='喊牌階段 ('+firstp+'開始):\n花色請使用：♠ ♥ ♣ ♦\n     請輸入數字與花色\n (♠ 輸入S，♥ 輸入H，♣ 輸入C，♦ 輸入D)，例如S3\nok後給下位玩家')
                cardslist.append('')
            if (d in cardslist)==False:
                fourcards.destroy()
                pEnter=Entry(fourgame)
                pEnter.place(x=425,y=380)
                commander_record = []
                suit='♣'
                num='1'
                suitdef_commander='♣0'
                ct = 0
                players_order=[]
                suitsdef=['♣0','♣1','♦1','♥1','♠1', #可擴充 no king 玩法 #未來亦可擴充至花橋喊法
                          '♣2','♦2','♥2','♠2',
                          '♣3','♦3','♥3','♠3',
                          '♣4','♦4','♥4','♠4',
                          '♣5','♦5','♥5','♠5',
                          '♣6','♦6','♥6','♠6',
                          '♣7','♦7','♥7','♠7']
                kingLabel=Label(fourgame,text='現在王牌為')
                kingLabel.place(x=468,y=150)

                playerlist=[firstp,secondp,thirdp,fourthp]
                cardabcd=[str(player_1),str(player_2),str(player_3),str(player_4)]
                k=0
                kingplayer=Label(fourgame, text=('現在喊中玩家為:'))
                kingplayer.place(x=0,y=100)
                kingcard=Label(fourgame, text=('玩家手牌:',cardabcd[k]))
                kingcard.place(x=280,y=300)
                commandername=Label(fourgame, text=('現在喊牌玩家為:',playerlist[k]))
                commandername.place(x='0', y='50') 
                
                def ok():
                    nonlocal suitdef_commander
                    nonlocal ct
                    global num
                    global suit
                    nonlocal playerlist
                    nonlocal k
                    nonlocal cardabcd
                    nonlocal record_1
                    nonlocal record_2
                    nonlocal record_3
                    nonlocal record_4
                    global commander_record
                    nonlocal firstp
                    nonlocal secondp
                    nonlocal thirdp
                    nonlocal fourthp
                    #nonlocal times
                    instruction.config(text='喊牌階段 ('+firstp+'開始):\n花色請使用：♠ ♥ ♣ ♦\n     請輸入數字與花色\n (♠ 輸入S，♥ 輸入H，♣ 輸入C，♦ 輸入D)，例如S3\nok後給下位玩家')
                    
                    pEnter.focus_set()
                    #yell.config(text=yellcard[(times+1)])
                    command_1=pEnter.get()

                    if command_1[0]=='S':
                        command_1=command_1.replace('S','♠')
                    elif command_1[0]=='H':
                        command_1=command_1.replace('H','♥')
                    elif command_1[0]=='D':
                        command_1=command_1.replace('D','♦')
                    elif command_1[0]=='C':
                        command_1=command_1.replace('C','♣')
                        
                    pEnter.delete(0,"end")
                
                    try: #防呆
                        if (command_1 in suitsdef)==False and command_1 != 'Pass' and command_1 != 'pass':
                            raise ValueError
                        elif command_1 == 'pass' or command_1 == 'Pass':
                            ct += 1
                            #times+=1
                            players_order.append(command_1)
                            if k==3:
                                k=0
                            else:
                                k+=1
                            commandername.config(text=('現在喊牌玩家為:',playerlist[k]))
                            kingcard.config(text=('玩家手牌:',cardabcd[k]))

                             
                        elif suitsdef.index(command_1) <= suitsdef.index(suitdef_commander):
                            raise ValueError
                        else:
                            num = command_1[1]
                            suit = command_1[0]
                            suitdef_commander = command_1
                            players_order.append(command_1)
                            kingLabel.config(text='現在王牌為'+players_order[-1])
                            kingplayer.config(text=('現在喊中玩家為:',playerlist[k]))
                            ct = 0
                            #times+=1
                            if k==3:
                                k=0
                            else:
                                k+=1
                            commandername.config(text=('現在喊牌玩家為:',playerlist[k]))
                            kingcard.config(text=('玩家手牌:',cardabcd[k]))

                                
                    except ValueError:
                        instruction.config(text='  請輸入有效值 (Pass/pass/(花色+數字))目前花色為:'+suitdef_commander)
                        
                    if ct == 3:
                        commandername.destroy()
                        kingplayer.destroy()
                        kingcard.destroy()
                        if len(players_order)%4 ==0:
                            commander= firstp
                            commander_record = record_1
                        elif len(players_order)%4 ==1:
                            commander = secondp
                            commander_record = record_2
                        elif len(players_order)%4 ==2:
                            commander = thirdp
                            commander_record = record_3
                        elif len(players_order)%4 ==3:
                            commander = fourthp
                            commander_record = record_4
                        
                        if eval(num)>=4: #若大於等於4 則為喊中先發
                            winner=commander
                        else:
                            winnernumber=playerlist.index(commander)
                            winner=playerlist[winnernumber-1]
                        
                        number=eval(num) #確認磴數
                        if commander == firstp or commander == thirdp:
                            player_1_3_required = str(6+number)
                            player_2_4_required = str(8-number)
                            
                        elif commander == secondp or commander == fourthp:
                            player_1_3_required = str(8-number)
                            player_2_4_required = str(6+number)
                        
                        instruction.config(text='喊中的玩家為:      '+commander+'\n王牌:      '+suitdef_commander+'\n由'+winner+'開始出牌      '+'\n'+firstp+'與'+thirdp+'，你們所需吃的磴數為'+'------->  '+player_1_3_required+'\n'+secondp+'與'+fourthp+'，你們所需吃的磴數為'+'------->  '+player_2_4_required)
                        btn4pstart.config(text='開始遊戲')
                        winnerLabel=Label(fourgame,text='由'+winner+'出牌')

                        winnerLabel.place(x=458,y=300)
                        cardLabel=Label(fourgame,text='')
                        #cardLabel.pack()
                        cardLabel.place(x=313,y=350)
                        roundcard=[] #每局出的牌
                        roundcard2=[]
                        count_1=0
                        count_2=0
                        newlist=[]
                        pEnter.place_forget()
                        
                        #出牌階段:
                        def start():
                            nonlocal winner
                            nonlocal roundcard
                            nonlocal roundcard2
                            nonlocal count_1
                            nonlocal count_2
                            nonlocal newlist
                            nonlocal player_1
                            nonlocal player_2
                            nonlocal player_3
                            nonlocal player_4
                            global E6
                            nonlocal firstp
                            nonlocal secondp
                            nonlocal thirdp
                            nonlocal fourthp
                            
                            pEnter.place(x=425,y=380)
                            pEnter.delete(0,'end')
                            btn4pstart.config(text='ok')
                            
                            if count_1==eval(player_1_3_required):
                                fourgame.destroy()
                                win=Tk()
                                youwin=Label(win,text=firstp+'and'+thirdp+' win')
                                if commander == firstp or commander == thirdp:
                                    E6 = True
                                else:
                                    E6 = False
                                youwin.pack()
                                win.mainloop()
                            elif count_2==eval(player_2_4_required):
                                fourgame.destroy()
                                win2=Tk()
                                yourwin=Label(win2,text=secondp+'and'+fourthp+ 'win')
                                if commander == secondp or commander == fourthp:
                                    E6 = True
                                else:
                                    E6 = False
                                yourwin.pack()
                                win2.mainloop()
                            #判斷每局勝負及下局出牌順序
                            if len(roundcard)==4:
                                for i in range(4):
                                    if roundcard[i][1]=='K':
                                        roundcard[i]=roundcard[i].replace('K','13')
                                    if roundcard[i][1]=='Q':
                                        roundcard[i]=roundcard[i].replace('Q','12')
                                    if roundcard[i][1]=='J':
                                        roundcard[i]=roundcard[i].replace('J','11')
                                    if roundcard[i][1]=='A':
                                        roundcard[i]=roundcard[i].replace('A','14')
                                for i in range(4):
                                    if len(roundcard[i])==3 and roundcard[i][0]==suit:
                                        aa=eval(roundcard[i][1:3])
                                        aa=aa*100
                                        newlist.append(aa)
                                    if len(roundcard[i])==3 and roundcard[i][0]!=suit:
                                        aa=eval(roundcard[i][1:3])
                                        newlist.append(aa)
                                    if len(roundcard[i])==2 and roundcard[i][0]==suit:
                                        aa=eval(roundcard[i][1])
                                        aa=aa*100
                                        newlist.append(aa)
                                    if len(roundcard[i])==2 and roundcard[i][0]!=suit:
                                        aa=eval(roundcard[i][1])
                                        newlist.append(aa)
                                
                                    
                                if max(newlist)==newlist[0]:
                                    if (roundcard2[0] in player_1)==True:
                                        winner = firstp
                                        count_1+=1
                                    if (roundcard2[0] in player_2)==True:
                                        winner = secondp
                                        count_2+=1
                                    if (roundcard2[0] in player_3)==True:
                                        winner = thirdp
                                        count_1+=1
                                    if (roundcard2[0] in player_4)==True:
                                        winner = fourthp
                                        count_2+=1
                                          
                                if max(newlist)==newlist[1]:
                                    if (roundcard2[1] in player_1)==True:
                                        winner = firstp
                                        count_1+=1
                                    if (roundcard2[1] in player_2)==True:
                                        count_2+=1
                                        winner = secondp
                                    if (roundcard2[1] in player_3)==True:
                                        count_1+=1
                                        winner = thirdp
                                    if (roundcard2[1] in player_4)==True:
                                        count_2+=1
                                        winner = fourthp
                                          
                                if max(newlist)==newlist[2]:
                                    if (roundcard2[2] in player_1)==True:
                                        count_1+=1
                                        winner = firstp
                                    if (roundcard2[2] in player_2)==True:
                                        count_2+=1
                                        winner = secondp
                                    if (roundcard2[2] in player_3)==True:
                                        count_1+=1
                                        winner = thirdp
                                    if (roundcard2[2] in player_4)==True:
                                        count_2+=1
                                        winner = fourthp
                                          
                                if max(newlist)==newlist[3]:
                                    if (roundcard2[3] in player_1)==True:
                                        count_1+=1
                                        winner = firstp
                                    if (roundcard2[3] in player_2)==True:
                                        count_2+=1
                                        winner = secondp
                                    if (roundcard2[3] in player_3)==True:
                                        count_1+=1
                                        winner = thirdp
                                    if (roundcard2[3] in player_4)==True:
                                        count_2+=1
                                        winner = fourthp
                                
                                
                                if (roundcard2[0] in player_1)==True:
                                    delete1=player_1.index(roundcard2[0])
                                    del player_1[delete1]
                                if (roundcard2[0] in player_2)==True:
                                    delete2=player_2.index(roundcard2[0])
                                    del player_2[delete2]
                                if (roundcard2[0] in player_3)==True:
                                    delete3=player_3.index(roundcard2[0])
                                    del player_3[delete3]
                                if (roundcard2[0] in player_4)==True:
                                    delete4=player_4.index(roundcard2[0])
                                    del player_4[delete4]
                                          
                                if (roundcard2[1] in player_1)==True:
                                    delete5=player_1.index(roundcard2[1])
                                    del player_1[delete5]
                                if (roundcard2[1] in player_2)==True:
                                    delete6=player_2.index(roundcard2[1])
                                    del player_2[delete6]
                                if (roundcard2[1] in player_3)==True:
                                    delete7=player_3.index(roundcard2[1])
                                    del player_3[delete7]
                                if (roundcard2[1] in player_4)==True:
                                    delete8=player_4.index(roundcard2[1])
                                    del player_4[delete8]
                                          
                                if (roundcard2[2] in player_1)==True:
                                    delete9=player_1.index(roundcard2[2])
                                    del player_1[delete9]
                                if (roundcard2[2] in player_2)==True:
                                    delete10=player_2.index(roundcard2[2])
                                    del player_2[delete10]
                                if (roundcard2[2] in player_3)==True:
                                    delete11=player_3.index(roundcard2[2])
                                    del player_3[delete11]
                                if (roundcard2[2] in player_4)==True:
                                    delete12=player_4.index(roundcard2[2])
                                    del player_4[delete12]
                                    
                                if (roundcard2[3] in player_1)==True:
                                    delete13=player_1.index(roundcard2[3])
                                    del player_1[delete13]
                                if (roundcard2[3] in player_2)==True:
                                    delete14=player_2.index(roundcard2[3])
                                    del player_2[delete14]
                                if (roundcard2[3] in player_3)==True:
                                    delete15=player_3.index(roundcard2[3])
                                    del player_3[delete15]
                                if (roundcard2[3] in player_4)==True:
                                    delete16=player_4.index(roundcard2[3])
                                    del player_4[delete16]
                                          
                                roundcard=[]
                                roundcard2=[]
                                newlist=[]
                                instruction.config(text=firstp+'和'+thirdp+'現在磴數------->  '+str(count_1)+'\n'+secondp+ '和' +fourthp+ '現在磴數------->  '+str(count_2))
                                pEnter.place_forget()
                                winnerLabel.config(text='由'+winner+'出牌')
                                kingLabel.config(text='')
                                btn4pstart.config(text='next round',command=start)
                                cardLabel.config(text='手牌為:')
                                
                                
                            elif winner==firstp:
                                cardLabel.config(text='手牌為:'+str(player_1))
                                winnerLabel.config(text='由'+winner+'出牌')
                                instruction.place_forget()
                                instruction.config(text=firstp+'和'+thirdp+'現在磴數------->  '+str(count_1)+'\n'+secondp+ '和' +fourthp+ '現在磴數------->  '+str(count_2))
                                instruction.place(x=444,y=200)
                                
                                #轉換符號
                                def decide():
                                    nonlocal roundcard
                                    nonlocal player_1
                                    nonlocal winner
                                    nonlocal roundcard2
                                    pEnter.focus_set()
                                    cards = pEnter.get()
                                    if cards[0]=='S':
                                        card=cards.replace('S','♠')
                                    elif cards[0]=='H':
                                        card=cards.replace('H','♥')
                                    elif cards[0]=='D':
                                        card=cards.replace('D','♦')
                                    elif cards[0]=='C':
                                        card=cards.replace('C','♣')
                                        
                                    if (card in player_1)==False:
                                        instruction.config(text='------------提示：請輸入目前所剩手牌------------')
                                        pEnter.place_forget()
                                        btn4pstart.config(command=start)
                                    else:
                                        roundcard.append(card)
                                        roundcard2.append(card)
                                        kingLabel.config(text='這局出的牌:'+str(roundcard))
                                        winner = fourthp
                                        pEnter.place_forget()
                                        btn4pstart.config(command=start)
                                        cardLabel.config(text='手牌為:')
                                        btn4pstart.config(text='請交給'+fourthp)
                                    
                                btn4pstart.config(command=decide)
                                
                            elif winner==secondp:
                                cardLabel.config(text='手牌為:'+str(player_2))
                                winnerLabel.config(text='由'+winner+'出牌')
                                instruction.place_forget()
                                instruction.config(text=firstp+'和'+thirdp+'現在磴數------->  '+str(count_1)+'\n'+secondp+ '和' +fourthp+ '現在磴數------->  '+str(count_2))
                                instruction.place(x=444,y=200)
                                
                                def decide():
                                    nonlocal roundcard
                                    nonlocal player_2
                                    nonlocal winner
                                    nonlocal roundcard2
                                    pEnter.focus_set()
                                    cards = pEnter.get()
                                    if cards[0]=='S':
                                        card=cards.replace('S','♠')
                                    elif cards[0]=='H':
                                        card=cards.replace('H','♥')
                                    elif cards[0]=='D':
                                        card=cards.replace('D','♦')
                                    elif cards[0]=='C':
                                        card=cards.replace('C','♣')
                                        
                                    if (card in player_2)==False:
                                        instruction.config(text='------------提示：請輸入目前所剩手牌------------')
                                        pEnter.place_forget()
                                        btn4pstart.config(command=start)
                                    else:
                                        roundcard.append(card)
                                        roundcard2.append(card)
                                        kingLabel.config(text='這局出的牌:'+str(roundcard))
                                        winner = firstp
                                        pEnter.place_forget()
                                        btn4pstart.config(command=start)
                                        cardLabel.config(text='手牌為:')
                                        btn4pstart.config(text='請交給'+firstp)
                                    
                                btn4pstart.config(command=decide)
                            
                            elif winner==thirdp:
                                cardLabel.config(text='手牌為:'+str(player_3))
                                winnerLabel.config(text='由'+winner+'出牌')
                                instruction.place_forget()
                                instruction.config(text=firstp+'和'+thirdp+'現在磴數------->  '+str(count_1)+'\n'+secondp+ '和' +fourthp+ '現在磴數------->  '+str(count_2))
                                instruction.place(x=444,y=200)
                                def decide():
                                    nonlocal roundcard
                                    nonlocal player_3
                                    nonlocal winner
                                    nonlocal roundcard2
                                    pEnter.focus_set()
                                    cards = pEnter.get()
                                    if cards[0]=='S':
                                        card=cards.replace('S','♠')
                                    elif cards[0]=='H':
                                        card=cards.replace('H','♥')
                                    elif cards[0]=='D':
                                        card=cards.replace('D','♦')
                                    elif cards[0]=='C':
                                        card=cards.replace('C','♣')
                                        
                                    if (card in player_3)==False:
                                        instruction.config(text='------------提示：請輸入目前所剩手牌------------')
                                        pEnter.place_forget()
                                        btn4pstart.config(command=start)
                                    else:
                                        roundcard.append(card)
                                        roundcard2.append(card)
                                        kingLabel.config(text='這局出的牌:'+str(roundcard))
                                        winner = secondp
                                        pEnter.place_forget()
                                        btn4pstart.config(command=start)
                                        cardLabel.config(text='手牌為:')
                                        btn4pstart.config(text='請交給'+secondp)
                                    
                                btn4pstart.config(command=decide)
                                
                            elif winner==fourthp:
                                cardLabel.config(text='手牌為:'+str(player_4))
                                winnerLabel.config(text='由'+winner+'出牌')
                                instruction.place_forget()
                                instruction.config(text=firstp+'和'+thirdp+'現在磴數------->  '+str(count_1)+'\n'+secondp+ '和' +fourthp+ '現在磴數------->  '+str(count_2))
                                instruction.place(x=444,y=200)
                                
                                def decide():
                                    nonlocal roundcard
                                    nonlocal player_4
                                    nonlocal winner
                                    nonlocal roundcard2
                                    pEnter.focus_set()
                                    cards = pEnter.get()
                                    if cards[0]=='S':
                                        card=cards.replace('S','♠')
                                    elif cards[0]=='H':
                                        card=cards.replace('H','♥')
                                    elif cards[0]=='D':
                                        card=cards.replace('D','♦')
                                    elif cards[0]=='C':
                                        card=cards.replace('C','♣')
                                        
                                    if (card in player_4)==False:
                                        instruction.config(text='------------提示：請輸入目前所剩手牌------------')
                                        pEnter.place_forget()
                                        btn4pstart.config(command=start)
                                    else:
                                        roundcard.append(card)
                                        roundcard2.append(card)
                                        kingLabel.config(text='這局出的牌:'+str(roundcard))
                                        winner = thirdp
                                        pEnter.place_forget()
                                        btn4pstart.config(command=start)
                                        cardLabel.config(text='手牌為:')
                                        btn4pstart.config(text='請交給'+thirdp)
                                    
                                btn4pstart.config(command=decide)
                        
                        btn4pstart.config(command=start)
            
                btn4pstart.config(command=ok)
                
        btn4pstart=Button(fourgame,text='ok',command=go)#換下一位
        btn4pstart.place(x='500', y='490')
        fourgame.mainloop()

    btn = Button(bridge,text='OK',command=startfourgame)
    btn.pack()
    
    bridge.mainloop()
    
#二人遊玩版本: twogame()
###尚未開發完成###

def twopgame():
    bridge_game.destroy()
    bridge2=Tk()

    bridge2.geometry("749x499")
    
    playernametwo = Label(bridge2, text = "請輸入玩家",font=30)
    playernametwo.pack(pady=30)

    p1 = Entry(bridge2)
    p2 = Entry(bridge2)
    label1_2=Label(bridge2, text="玩家一")
    label2_2=Label(bridge2, text="玩家二")
    
   
    pfirst = p1.get()
    psecond = p2.get()
    
    
    label1_2.pack()
    p1.pack()
    label2_2.pack()
    p2.pack()
    
    def starttwogame():
        bridge2.destroy()
        twogame = Tk()
        def nextplayer():
            namelist=[pfirst,'PCone',psecond,'PCtwo']
            n=0
            if n<999:
                namelabel.config(text=namelist[n+1])
                n+=1
        namelabel=Label(twogame,text=pfirst)#玩家名
        namelabel.pack()
        btn2pstart=Button(twogame,text='換人')#換下一位
        btn2pstart.pack()
        
        twogame.mainloop()
        
    btn2 = Button(bridge2,text='OK',command=starttwogame)
    btn2.pack()
    
    bridge2.mainloop()
    
photoone=PhotoImage(file='下陷.png')
imageLabel1=Label(bridge_game,image=photoone,compound='center')
imageLabel1.pack()

button_1 = Button(bridge_game,text='2 players',font=('Bahnschrift Condensed',20),bg='blue',fg='white')
button_2 = Button(bridge_game,text='4 players',font=('Bahnschrift Condensed',20),bg='blue',fg='white')
button_2.config(command=fourpgame)  # button執行function
button_1.config(command=twopgame)

label.pack(pady=40)
button_1.place(x=150,y=400)
button_2.place(x=350,y=400)
bridge_game.mainloop()

#覆盤分析
def analyze_1():
    cl = 0
    di = 0
    he = 0
    sp = 0
    bignum = 0
    for qa in range(len(commander_record)):
        if commander_record[qa][0] == '♣':
            cl += 1
        elif commander_record[qa][0] == '♦': 
            di += 1
        elif commander_record[qa][0] == '♥': 
            he += 1
        elif commander_record[qa][0] == '♠': 
            sp += 1
        if commander_record[qa][1] == ('A'or 'K' or 'Q' or 'J'):
            bignum += 1
    E1 = cl
    E2 = di
    E3 = he
    E4 = sp
    E5 = suit+num
    E7 = bignum
    return([E1,E2,E3,E4,E5,E6])
pd.read_csv('any_1test')
gr_1 = analyze_1()
series = [{'梅花':gr_1[0],'方塊':gr_1[1],'愛心':gr_1[2],'黑桃':gr_1[3],'喊牌':gr_1[4],'勝負':gr_1[5]}]
df_1 = df_1.append(series)
df_1.to_csv('any_2test.csv',index = False)
df_1