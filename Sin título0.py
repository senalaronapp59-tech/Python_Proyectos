from tkinter import *
vent= Tk()

vent.title("Numeros :P")
vent.geometry("600x200")

label_series = Label(vent, text="Serie Fibonacci:")
label_flowers = Label(vent)
label_spiral = Label(vent)

def fibonacci():
    num= 10
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    while (counter <= num):
        label_series["text"] +=str(sum) + " "
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
    label_flower['text']= "la flor esta completamente florecida"
    label_spiral["text"] = "Los espirales en la dirección derecha son " + str(first_no) + " y los espirales en la dirección izquierda son " + str(second_no) + "\n El total de espirales es " + str(sum)


def pop():
    result= 87+45
    label_flowers["text"]=result

boton = Button(vent, text="agregar", command=fibonacci)
boton.pack()
label_series.pack()
label_flowers.pack()
label_spiral.pack()

vent.mainloop()