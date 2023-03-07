from tkinter import*

# 處理隨機數生成
import random

# Tk視窗參數設定
win = Tk()
win.title("Random X,Y Generator")
# win.geometry(長x寬 +X +Y)
win.geometry("400x220+800+400")
win.config(bg="#323232")

#////////////////////////////////////#

title_text = Label(text="Random X,Y Generator", fg="skyblue", bg="#323232")
# obj.config(font="字型 大小")
title_text.config(font="微軟正黑體 15")
title_text.pack()