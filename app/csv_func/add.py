import csv
import tkinter as tk


def add_show(csv_file):
  def add_medikament():
      stoka_number = number_entry.get()
      stoka_name = name_entry.get()
      group = group_entry.get()
      with open(csv_file, mode="a", newline="",encoding="utf-8") as file:
          writer = csv.writer(file)
          writer.writerow([stoka_number, stoka_name, group])
      number_entry.delete(0, tk.END)
      name_entry.delete(0, tk.END)
      group_entry.delete(0, tk.END)
      message_label.config(text="Новият артикул е добавен успешно.")

  def read_stoki():
    from csv_func import Goods
    file=Goods.read(csv_file)
    Goods.show_data(file)

  root = tk.Tk()
  root.title("Добавяне на медикамент")
  root.geometry("280x150")
  number_label = tk.Label(root, text="Код на медикамент: ",bg="#fad400",fg="#000000")
  number_label.grid(row=0, column=0, padx=5, pady=5)
  number_entry = tk.Entry(root)
  number_entry.grid(row=0, column=1, padx=5, pady=5)
  name_label = tk.Label(root, text="Име на медикамент: ",bg="#fad400",fg="#000000")
  name_label.grid(row=1, column=0, padx=5, pady=5)
  name_entry = tk.Entry(root)
  name_entry.grid(row=1, column=1, padx=5, pady=5)
  group_label = tk.Label(root, text="Група: ",bg="#fad400",fg="#000000")
  group_label.grid(row=3, column=0, padx=5, pady=5)
  group_entry = tk.Entry(root)
  group_entry.grid(row=3, column=1, padx=5, pady=5)
  add_button = tk.Button(root, text="Добави",activebackground="#fad400",activeforeground="#000000",bg="#fad400",fg="#000000", command=add_medikament)
  add_button.grid(row=5, column=0, columnspan=1,
  padx=5, pady=5)
  read_button = tk.Button(root, text="Преглед на медикаментите",activebackground="#fad400",activeforeground="#000000",bg="#fad400",fg="#000000", command=read_stoki)
  read_button.grid(row=5, column=1, columnspan=1,
  padx=5, pady=5)
  message_label = tk.Label(root, text="", fg="green")
  message_label.grid(row=6, column=0, columnspan=2, padx=5,
  pady=5)
  root.mainloop()