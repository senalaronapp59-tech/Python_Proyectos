#error de geomettria equivocada
from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("error de geometria")
root.geometry("600x400")
input_box = Entry(root)
input_box.pack()

def addition():
    number = 5
    get_input = input_box.get()
    try:
        print(number + get_input)
    except(TypeError):
        messagebox.showinfo2("error", "No se pueden añadir tipos diferentes :P")

button = Button(root, text = "suma", command= addition)
button.pack()
root.mainloop()