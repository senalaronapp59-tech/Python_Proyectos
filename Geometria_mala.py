#error de geomettria equivocada
from tkinter import *
root=Tk()
root.title("error de geometria")
try:
    root.geometry("600")
except:
    print("Error en la geometria, se necesita mas datos")

root.mainloop()