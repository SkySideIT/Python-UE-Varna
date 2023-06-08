import csv
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox   
def read(csv_file):
    with open(csv_file, "r", encoding="utf-8") as file:
        csvreader = csv.reader(file)
        list1 = []
        for row in csvreader:
            list1.append(row)  
        return list1

def show_data(list1,list2,list3):
    def search_st():
       stoka_Data = medikament_entry.get() 
       medikament_entry.delete(0, tk.END)
       data_list_search=[]

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
               
       for index1 in list2: 
           if index1[2]==index2[0]:
               index1.insert(3,index2[1])
               break 
           
       for dat1 in list2:
            data_list_search.append(dat1)
            break  
       
       for dat1 in list2:
            if dat1[4]==stoka_Data:
                data_list_search.append(dat1)
       root.destroy()

       if len(data_list_search)==1:
        response=messagebox.askyesno('Грешка','Няма данни')
        if response:
            root.destroy()
       else:
        from csv_func import showResult
        showResult.show(data_list_search)
        
    root = tk.Tk()
    root.title('Търене по дата')
    medikament_label = tk.Label(root, text="Въведете дата: ",bg="#fad400",fg="#000000")
    medikament_label.grid(row=0, column=0, padx=5, pady=5)
    medikament_entry = tk.Entry(root)
    medikament_entry.grid(row=0, column=1, padx=5, pady=5)
    search_button = tk.Button(root, text="Търси по дата",activebackground="#fad400",activeforeground="#000000",bg="#fad400",fg="#000000", command=search_st)
    search_button.grid(row=0, column=3, columnspan=2,padx=5, pady=5)
    root.mainloop()