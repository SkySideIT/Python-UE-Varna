import csv
import tkinter as tk
from tkinter import ttk


def read(csv_file):
    with open(csv_file, "r", encoding="utf-8") as file:
        csvreader = csv.reader(file)
        data_list = []
        for row in csvreader:
            data_list.append(row)  
        return data_list

def show_data(data_list):
    root = tk.Tk()
    root.title('Наличности')                
    table = ttk.Treeview(root)
    table.pack(fill=tk.BOTH, expand=True)
    table["columns"] = data_list[0]
    table.heading("#0", text="Index")
    table.column("#0", width=50)

    for col in data_list[0]:
        table.heading(col, text=col)
        table.column(col, width=100)
        
    for i,row in enumerate(data_list[1:]):
        table.insert("", "end",text=i+1, values=row)
    root.mainloop()
