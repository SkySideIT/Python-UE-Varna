import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox

csv_file1 = "C:/Users/SkySide TV/Desktop/120448/app/data/Groups.csv"
csv_file2 = "C:/Users/SkySide TV/Desktop/120448/app/data/Sales.csv"
csv_file3 = "C:/Users/SkySide TV/Desktop/120448/app/data/Goods.csv"

global my_image

class App:
    def __init__(self, root):
        #setting title
        root.title("Аптека")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_303=tk.Label(root)
        GLabel_303["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_303["font"] = ft
        GLabel_303["fg"] = "#333333"
        GLabel_303["justify"] = "left"
        GLabel_303["text"] = ""
        GLabel_303.place(x=0,y=0,width=602,height=494)

        my_image = PhotoImage(file="C:/Users/SkySide TV/Desktop/120448/app/main.png")
        label = Label(root, image = my_image)
        label.place(x=60, y=100)
        
        GButton_86=tk.Button(root)
        GButton_86["bg"] = "#fad400"
        ft = tkFont.Font(family='Times',size=12)
        GButton_86["font"] = ft
        GButton_86["fg"] = "#000000"
        GButton_86["justify"] = "center"
        GButton_86["text"] = "Наличност"
        GButton_86.place(x=390,y=40,width=188,height=58)
        GButton_86["command"] = self.GButton_86_command

        GButton_291=tk.Button(root)
        GButton_291["bg"] = "#fad400"
        ft = tkFont.Font(family='Times',size=12)
        GButton_291["font"] = ft
        GButton_291["fg"] = "#000000"
        GButton_291["justify"] = "center"
        GButton_291["text"] = "Добавяне"
        GButton_291.place(x=390,y=110,width=186,height=62)
        GButton_291["command"] = self.GButton_291_command

        GButton_178=tk.Button(root)
        GButton_178["bg"] = "#fad400"
        ft = tkFont.Font(family='Times',size=12)
        GButton_178["font"] = ft
        GButton_178["fg"] = "#000000"
        GButton_178["justify"] = "center"
        GButton_178["text"] = "Търсене по дата "
        GButton_178.place(x=390,y=190,width=187,height=64)
        GButton_178["command"] = self.GButton_178_command

        GButton_287=tk.Button(root)
        GButton_287["bg"] = "#fad400"
        ft = tkFont.Font(family='Times',size=12)
        GButton_287["font"] = ft
        GButton_287["fg"] = "#000000"
        GButton_287["justify"] = "center"
        GButton_287["text"] = "Тъсене по цена"
        GButton_287.place(x=390,y=270,width=186,height=72)
        GButton_287["command"] = self.GButton_287_command

        GButton_571=tk.Button(root)
        GButton_571["bg"] = "#fad400"
        ft = tkFont.Font(family='Times',size=12)
        GButton_571["font"] = ft
        GButton_571["fg"] = "#000000"
        GButton_571["justify"] = "center"
        GButton_571["text"] = "Продажби"
        GButton_571.place(x=390,y=360,width=185,height=76)
        GButton_571["command"] = self.GButton_571_command

        GLabel_616=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_616["font"] = ft
        GLabel_616["fg"] = "#333333"
        GLabel_616["justify"] = "center"
        GLabel_616["text"] = "Лили Фарм"
        GLabel_616.place(x=30,y=20,width=241,height=34)

    def GButton_291_command(self):
        from csv_func import add
        add.add_show(csv_file3)


    def GButton_86_command(self):
        from csv_func import InStock
        file1=InStock.read(csv_file1)
        file2=InStock.read(csv_file2)
        file3=InStock.read(csv_file3)
        InStock.show_data(file1,file2,file3)



    def GButton_571_command(self):
        from csv_func import Sales
        file1=Sales.read(csv_file1)
        file2=Sales.read(csv_file2)
        file3=Sales.read(csv_file3)
        Sales.show_data(file1,file2,file3)


    def GButton_178_command(self):
        from csv_func import search_Date
        file1=search_Date.read(csv_file1)
        file2=search_Date.read(csv_file2)
        file3=search_Date.read(csv_file3)
        search_Date.show_data(file1,file2,file3)


    def GButton_287_command(self):
        from csv_func import search_Price
        file1=search_Price.read(csv_file1)
        file2=search_Price.read(csv_file2)
        file3=search_Price.read(csv_file3)
        search_Price.show_data(file1,file2,file3)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()