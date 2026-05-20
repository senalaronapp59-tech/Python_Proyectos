
from tkinter import *

vent= Tk()

vent.title("Numeros :P")
vent.geometry("400x400")
vent.config(bg="#D5FFBF")
vent.configure(background= 'snow')

enter_word = Entry(vent)
enter_word.place(relx=0.5 ,rely=0.4, anchor=CENTER)


label = Label(vent, text= "Nombre en ASCII:", bg='light yellow', fg= 'black')

def asciConverte():
    input_word = enter_word.get()
    for letter in input_word :
        label["text"] += str(ord(letter)) + "    "




btn=Button(vent, text="Muestra el nombre en ASCII", command=asciConverte, bg= "gold", fg= "black")
btn.place(relx=0.5 ,rely=0.5, anchor=CENTER)

label.place(relx=0.5, rely=0.6, anchor=CENTER)


    


vent.mainloop()