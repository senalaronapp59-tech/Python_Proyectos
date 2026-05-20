from tkinter import *
cato= Tk()

cato.title("Adiccion")
cato.geometry("600x200")
cato.config(bg="#A3F527")
#cato.resizable(False, False)

show_result=Label(cato,text="Resultado",fg="blue",bg="#A3F527",font=("Arial",20,"bold"))

def add():
    result= 4+1
    show_result["text"]=result

btn = Button(cato,text="Añadir", command=add)
btn.pack()
show_result.pack()

cato.mainloop()

print(type(cato))
