
mylist = [0,1,2,3]
try:
    print(mylist[5])
except IndexError:
    print("ese numero no existe en la lista")