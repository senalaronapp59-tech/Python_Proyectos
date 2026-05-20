from tkinter import *
import random
vent= Tk()
vent.geometry("600x500")

label= Label(vent)

lista3 = [[["1","2","3","4","5","6",],["Patata","pizarron","Cabeza"],["A","B","C","D",'E','F','G','H']]]

def new_password():
    random_1 = random.randint(0,5)
    random_2 = random.randint(0,2)
    random_3 = random.randint(0,7)
    
    letter1 =lista3[0][0][random_1]
    letter2 =lista3[0][1][random_2]
    letter3 =lista3[0][2][random_3]

    label['text'] = letter1 + letter2 + letter3
    print(label['text'])

btn = Button(vent, text='Nueva contraseña',command= new_password)
btn.place(relx= 0.5,rely= 0.5, anchor= CENTER)

label.place(relx= 0.5, rely= 0.6, anchor= CENTER)


vent.mainloop()



