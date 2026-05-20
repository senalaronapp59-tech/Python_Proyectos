
# error de variable no definida
a= 10
b= 20
try:
    print(a)
    print(b)
    print(x)
except NameError:
    print('Variable x no esta defionida')

print(a+b)

