import csv
import tkinter as tk
from tkinter import ttk
def show(data_list_search):
    root = tk.Tk()
    root.title("Данните")
    table = ttk.Treeview(root)
    table.pack(fill=tk.BOTH, expand=True)
    table["columns"] = data_list_search[0]
    table.heading("#0", text="Index")
    table.column("#0", width=50)

    for col in data_list_search[0]:
        table.heading(col, text=col)
        table.column(col, width=100)
        
    for i,row in enumerate(data_list_search[1:]):
        table.insert("", "end",text=i+1, values=row)
    root.mainloop()

  