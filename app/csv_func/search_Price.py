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
       stoka_cena = cena_entry.get() 
       cena_entry.delete(0, tk.END)
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
       data_list_search={}
       data_list5={}
       data_list_search_cena=[]
       for index2 in list.values():
           data_list5[round(index2,2)]=1
                
       for index2 in list4[1:]:
           for index3 in data_list5.keys():
               if index2[3]==index3:
                    data_list_search.setdefault(float(index2[3]),[]).append(index2)

       for index2 in list4:
           data_list_search_cena.append(index2)
           break
       
       for item in data_list_search.keys():
            if item<=float(stoka_cena):
                value= data_list_search.get(item)
                for x in value:
                    data_list_search_cena.append(x)
       root.destroy()

       if len(data_list_search_cena)==1:
        response=messagebox.askyesno('Грешка','Няма данни')
        if response:
            root.destroy()
       else: 
          from csv_func import showResult
          showResult.show(data_list_search_cena)

    root = tk.Tk()
    root.title('Търсене по цена')
    cena_label = tk.Label(root, text="Въведете сума: ",bg="#fad400",fg="#000000")
    cena_label.grid(row=0, column=0, padx=5, pady=5)
    cena_entry = tk.Entry(root)
    cena_entry.grid(row=0, column=1, padx=5, pady=5)
    search_button = tk.Button(root, text="Търси",activebackground="#fad400",activeforeground="#000000",bg="#fad400",fg="#000000", command=search_st)
    search_button.grid(row=0, column=3, columnspan=2,
    padx=5, pady=5)
    root.mainloop()