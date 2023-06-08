import csv
import tkinter as tk
from tkinter import ttk


def read(csv_file):
    with open(csv_file, "r", encoding="utf-8") as file:
        csvreader = csv.reader(file)
        list1 = []

        for row in csvreader:
            list1.append(row)  
        return list1

def show_data(list1,list2,list3):
    root = tk.Tk()
    root.title('Продажби')
    list={}
    list4=[]

    for index2 in list2[1:]:
        list[index2[0]]=1
                
    for index2 in list2[1:]:
        for index3 in list.keys():
            if index2[0]==index3:
                 list[index2[0]]+=(float(index2[2])*float(index2[3])) 
                 break 
            
    for index1 in list3:
        for index2 in list1:
            if index1[2]==index2[0]:
                index1.insert(2,index2[1])
                index1.remove(index2[0])
                break

    for index1 in list3:
        value= "Сума"
        index1.insert(3,value)
        list4.append(index1)
        break
    
    for index1 in list3[1:]:
        check=False
        for index3 in list.keys():
                if index1[0]==index3:
                   value= round(list.get(index3),2)
                   index1.insert(3,value)
                   check=True
                   break
        if check==True:
            list4.append(index1)

    table = ttk.Treeview(root)
    table.pack(fill=tk.BOTH, expand=True)
    table["columns"] = list4[0]
    table.heading("#0", text="Index")
    table.column("#0", width=50)
    
    for col in list4[0]:
        table.heading(col, text=col)
        table.column(col, width=100)
 
    for i,row in enumerate(list4[1:]):
        table.insert("", "end",text=i+1, values=row)     
    root.mainloop()

