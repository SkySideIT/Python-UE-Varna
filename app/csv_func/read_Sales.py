import csv
import tkinter as tk
from tkinter import ttk
def read1(csv_file):
    with open(csv_file, "r", encoding="utf-8") as file:
        csvreader = csv.reader(file)
        data_list1 = []
        for row in csvreader:
            data_list1.append(row)  
        return data_list1

def show_csv_data(data_list1,data_list2,data_list3):
    root = tk.Tk()
    root.title('Продажби')
    data_list={}
    data_list4=[]
    for i2 in data_list2[1:]:
        data_list[i2[0]]=1
                
    for i2 in data_list2[1:]:
        for i3 in data_list.keys():
            if i2[0]==i3:
                 data_list[i2[0]]+=(float(i2[2])*float(i2[3])) 
                 break 
    for i1 in data_list3:
        for i2 in data_list1:
            if i1[2]==i2[0]:
                i1.insert(2,i2[1])
                i1.remove(i2[0])
                break

    for i1 in data_list3:
        value= "Сума"
        i1.insert(3,value)
        data_list4.append(i1)
        break
    
    for i1 in data_list3[1:]:
        check=False
        for i3 in data_list.keys():
                if i1[0]==i3:
                   value= round(data_list.get(i3),2)
                   i1.insert(3,value)
                   check=True
                   break
        if check==True:
            data_list4.append(i1)
    table = ttk.Treeview(root)
    table.pack(fill=tk.BOTH, expand=True)
    table["columns"] = data_list4[0]
    table.heading("#0", text="Index")
    table.column("#0", width=50)
    for col in data_list4[0]:
        table.heading(col, text=col)
        table.column(col, width=100)
 
    for i,row in enumerate(data_list4[1:]):
        table.insert("", "end",text=i+1, values=row)     
    root.mainloop()

