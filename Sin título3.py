
from tkinter import *
import random
vent= Tk()
vent.geometry("600x500")

 
enter_word = Entry(vent)
enter_word.place(relx=0.5 ,rely=0.2, anchor=CENTER)

texto = Label(vent)
texto_1 = Label(vent)
texto_2 = Label(vent)






list1 = []

def Addf():
    friend_name = enter_word.get()
    list1.append(friend_name)
    texto["text"] = "Tu lista de amigos " + str(list1)
    
    
def random_n():
    lenght = len(list1)
    random_no = random.randint(0, lenght-1)
    texto_1 ["text"] = str(random_no)
    generated_random_number = list1[random_no]
    texto_2 ["text"] = "Tu amigo afotunado es: " + str(generated_random_number)
    
    
texto.place(relx=0.5,rely=0.4,anchor= CENTER)

btn_1 = Button(vent,text="Añadir a lista de amigos",command=Addf)
btn_1.place(relx=0.5,rely=0.3,anchor= CENTER)

btn = Button(vent,text="¿quien es tu amigo afortunado?",command=random_n)
btn.place(relx=0.5,rely=0.5,anchor= CENTER)

texto_1.place(relx=0.5,rely=0.6,anchor= CENTER)

texto_2.place(relx=0.5,rely=0.7,anchor= CENTER)


vent.mainloop()