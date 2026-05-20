from tkinter import *
import random
vent= Tk()

label= Label(vent)

lista1 = ["pancho", "Pablo", "Ramon"] 
print(lista1)

for i in range(len(lista1)):
    Label(vent,text=lista1[i]).grid(row=i, column=0, padx=5, pady=5)   


lista2 = [["Maria","A"],["Franco","B"],["Daniel","C"]] 
print(lista2)

lista3 = [[["Maria","D","Muy bien"],["Estela","C","Maso"],["Leli","B","Bien"]]] 
print(lista3)


vent.mainloop()