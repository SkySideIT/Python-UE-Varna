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
    root.title('Наличности')
    for index1 in list2:
        for index2 in list3:
            if index1[0]==index2[0]:
                index1.insert(1,index2[1])
                index1.insert(2,index2[2])
                break

    for index1 in list2:
        for index2 in list1:
            if index1[2]==index2[0]:
                index1.insert(3,index2[1])
                break     

    table = ttk.Treeview(root)
    table.pack(fill=tk.BOTH, expand=True)
    table["columns"] = list2[0]
    table.heading("#0", text="Index")
    table.column("#0", width=50)

    for col in list2[0]:
        table.heading(col, text=col)
        table.column(col, width=100)
        
    for i,row in enumerate(list2[1:]):
        table.insert("", "end",text=i+1, values=row)
    root.mainloop()

