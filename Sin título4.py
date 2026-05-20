from tkinter import *
import random
vent= Tk()
vent.geometry("600x500")



# =========================
# LISTA 1D
# =========================

lista1 = ["pancho", "Pablo", "Ramon"] 
print(lista1)


frame1 = Frame(vent)
frame1.grid(row=0, column=0, pady=20)


for i in range (len(lista1)):
    Label(frame1,
          text=lista1[i],
          borderwidth=1,
          relief="solid",
          width=15,
          height=2).grid(row=0, column=i)


lista2 = [["Maria","A"],["Franco","2A"],["Daniel","C"],["Cristo","2B"]] 
print(lista2[2][0])

frame2 = Frame(vent)
frame2.grid(row=1, column=0,pady=20)

# Encabezados
Label(frame2, text="Nombre", font=("Arial", 12, "bold"), borderwidth=1, relief="solid", width=15).grid(row=0, column=0)
# Encabezados
Label(frame2, text="Grupo", font=("Arial", 12, "bold"), borderwidth=1, relief="solid", width=10).grid(row=0, column=1)

for i in range(len(lista2)):
    for j in range (len(lista2[i])):
        Label(frame2,
              text=lista2[i][j],
              borderwidth=1,
              relief="solid",
              width=15,
              height=2).grid(row=i+1, column=j)
                



lista3 = [[["A"], ["b"],["c"],["A"], ["b"],["c"],["1"],['2'],['3']],
          [["1"],['2'],['3'],["A"], ["b"],["c"],["1"],['2'],['3']],
          [["#"],["!"],["="],["A"], ["b"],["c"],["1"],['2'],['3']]]
print(lista3[0][2][0])

frame3 = Frame(vent)
frame3.grid(row=2, column=0,pady=20)


for i in range(len(lista3)):
    for j in range (len(lista3[i])):
        for k in range (len(lista3[i][j])):
            Label(frame3,
                  text=lista3[i][j][k],
                  borderwidth=1,
                  relief="solid",
                  width=5,
                  height=2).grid(row=i+1, column=j)
                

#lista3 = [[["Maria","D","Muy bien"],["Estela","C","Maso"],["Leli","B","Bien"]]] 
#print(lista3)

vent.mainloop()