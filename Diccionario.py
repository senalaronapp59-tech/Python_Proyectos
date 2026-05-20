from tkinter import *
import random
vent= Tk()
vent.geometry("900x900")
vent.configure(background='orange')
vent.title("Diccionario")

Ib_mutable = Label(vent)
Ib_Inmurable = Label(vent)
Ib_Tkinter = Label(vent)
Ib_Tardis = Label(vent)
lb_atadura_celestial = Label(vent)


diccionary = {'Mutable': 'los valores se pueden cambiar, como en la lista',
              'Inmurable': 'Los valores no se pueden cambiar, como en una tupla',
              'Tkinter': 'es una biblioteca GUI de Python',
              'Tardis': 'Es una nave que viaja en el tiempo y que tiene una fomra de una cabina telefonica azul',
              'Atadura_celestial': 'Es un voto vinculante que esta inpuesto al nacer que limita al hechicero a cambio de hablidades extraordinarias'}

def atadura_celestial():
    lb_atadura_celestial["text"] = diccionary['Atadura_celestial']

button_atadura_celestial= Button(vent, text= 'Significado de atadura_celestial', command = atadura_celestial)
button_atadura_celestial.place(relx = 0.5, rely=0.05, anchor= CENTER)
lb_atadura_celestial.place(relx = 0.5, rely=0.1, anchor= CENTER)


def mutable():
    Ib_mutable["text"] = diccionary['Mutable']

    
button_mutable= Button(vent, text= 'Significado de Mutable', command = mutable)
button_mutable.place(relx = 0.5, rely=0.2, anchor= CENTER)
Ib_mutable.place(relx = 0.5, rely=0.3, anchor= CENTER)


def inmurable():
    Ib_Inmurable["text"] = diccionary['Inmurable']

    
button_Inmurable= Button(vent, text= 'Significado de Inmurable', command = inmurable)
button_Inmurable.place(relx = 0.5, rely=0.4, anchor= CENTER)
Ib_Inmurable.place(relx = 0.5, rely=0.5, anchor= CENTER)


def tkinter():
    Ib_Tkinter["text"] = diccionary['Tkinter']

    
button_Tkinter= Button(vent, text= 'Significado de Tkinter', command = tkinter)
button_Tkinter.place(relx = 0.5, rely=0.6, anchor= CENTER)
Ib_Tkinter.place(relx = 0.5, rely=0.7, anchor= CENTER)



def tardis():
    Ib_Tardis["text"] = diccionary['Tardis']

    
button_Tardis= Button(vent, text= 'Significado de Tardis', command = tardis)
button_Tardis.place(relx = 0.5, rely=0.8, anchor= CENTER)
Ib_Tardis.place(relx = 0.5, rely=0.9, anchor= CENTER)










vent.mainloop()
