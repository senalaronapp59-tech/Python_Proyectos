from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("600x400")

list_name = ["mickey mouse", "Elsa", "Anna", "Pato Donald"]
dict_student = {"nombre": "shincan",
                "edad":"5"}
try:
    print(list_name[8])
    print(dict_student["mama"])
except IndexError:
    print("Index fuera de rango")
    messagebox.showinfo("error", "Index no encontrado")
except KeyError:
    print("Clave fuera de rango")
    messagebox.showinfo("error", "Clave no encontrado")


root.mainloop()