from tkinter import *
import random
vent= Tk()

vent.title("Numeros :P")
vent.geometry("400x400")
vent.config(bg="#D5FFFF")

random_number_list = Label(vent)
random_number_sorted_list = Label(vent)

def randomlist():
    random_list = random.sample(range (10,30),5)
    random_number_list["text"] = ["Lista aleatoria " + str(random_list)]
    random_list.sort()
    random_number_sorted_list["text"] = "Números aleatorios ordenados" + str(random_list)
    
btn = Button(vent,text="generar lista aleatoria: ",command=randomlist)
btn.place(relx=0.5,rely=0.4,anchor= CENTER)

random_number_list.place(relx=0.5, rely=0.5,anchor=CENTER)
random_number_sorted_list.place(relx=0.5, rely=0.6,anchor=CENTER)

vent.mainloop()