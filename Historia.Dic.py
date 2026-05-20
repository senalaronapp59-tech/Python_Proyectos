from tkinter import *
import random
vent= Tk()
vent.geometry("300x400")
vent.title("Diccionario_hist")


Ib_azul = Label(vent)
Ib_rojo = Label(vent)
Ib_verde = Label(vent)

ib_nom_col = Label(vent)
ib_cod_col = Label(vent)

diccionary = {'azul': '#398ADB',
              'rojo': '#AB0202',
              'verde': '#3EDB39',}

def Dato():
    ib_nom_col = random.choice(list(diccionary.keys()))
    ib_cod_col = diccionary[ib_nom_col]
    #cambiar fondo
    vent.config(bg=ib_cod_col)
    
    # Actualizar texto
    label.config(text=f"Color: {nombre_color}", bg=codigo_color)

button_azul= Button(vent, text= 'Color', command = Dato)
button_azul.place(relx = 0.5, rely=0.1, anchor= CENTER)





vent.mainloop()