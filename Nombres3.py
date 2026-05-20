import random

lista = ["Damian", "Victoria", "Marianne","Ana","Milan"]
print(lista)

random_no = random.randint(0,4)

print(lista[random_no])

from tkinter import *
import random
vent= Tk()

lista = ["Damian", "Victoria", "Marianne","Ana","Milan"]
emojis = [" \U0001F44B", "\U0001F600", "\U0001F601","\U0000270C", "\U0001F431"]

print(lista)
    
texto =Label(vent, text= "Amigo afortunado", bg='light yellow', fg= 'black')
texto.place(relx=0.5,rely=0.3,anchor= CENTER)

def Boton():

    random_no = random.randint(0,4)
    print(lista[random_no])
    
    friend = lista[random_no]
    emojis_l = emojis[random_no]
    
    texto_2 =Label(vent, text= friend+" ganaste alimentar y convivir 1 día con la Jade :D" + emojis_l , bg='light yellow', fg= 'black')
    texto_2.place(relx=0.5,rely=0.6,anchor= CENTER)

    

btn = Button(vent,text="Oprime aqui para tener el ganador",command=Boton)
btn.place(relx=0.5,rely=0.4,anchor= CENTER)



vent.mainloop()