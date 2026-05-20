# 1. Bloques de codigo


x = 0

if x > 5 :
    print("Mayor :O")
    
#2. punto y coma
num = 10.9

#3. Variables

y = 5

#4. Funciones
def saludar(nombre):
    return "hola " + nombre
    print("hola " + nombre) 

print(saludar("Julieta"))

#5. imprimir

print(":D")

#6. Condicionales

#6.1 if (si) Ejecuta un bloque solo si la condición es verdadera.

edad = 18

if edad >= 18:
    print("eres mayor de edad")

if x > 0:
    print("Positivo")
    
#6.2 if - else (si / si no) Ejecuta un bloque si la condición es verdadera y otro si es falsa.
numero = 5

if numero > 0:
    print("Positivo")
else:
    print("Negativo o cero")

#6.3 if - else if - else Permite evaluar varias condiciones.
if numero > 0:
    print("Positivo")
elif x == 0:
    print("Cero")
else:
    print("Negativo")
#6.4 Condicionales ternarios: Condicional en una sola liena 

edad = 20
mensaje = 'mayor' if edad >= 18 else "menor"

#6.5 swich / case util cuando compras una sola variable con varios valores 

dia = 2

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case 8:
        print("Día no válido")

#6.6 Condicionales anidadas: Un id dentro de otro if

edad = 20
tiene_credencial = True
if edad >= 18:
    if tiene_credencial:
        print("Puedes entrar")
    else:
            print("Necesitas credencial")
else:
    print("Eres menor de edad")

    
#7.Bucles
#7.1 for  Se usa para recorrer secuencias (listas, rangos, cadenas, etc.

for i in range(5):
    print(i)
    
#7.2 While Se ejecuta mientras la condicion sea verdadera
contador = 0

while contador < 5:
    print("ciclo"+str(contador))
    contador +=1

#7.3 do-while (solo en JavaScript): (while + break) Se ejecuta al menos una vez, aunque la condición sea falsa.

i = 0

while True:
    print(i)
    i += 1 
    
    if i>= 5:
        break
    
#7.4 for-each  Itera directamente sobre los elementos.

lista = ["a", "b", "c"]
print(lista[-1])


for elemento in lista:
    print(elemento)
    
#7.5 Bucles anidados  Un bucle dentro de otro bucle.

for i in range(3):
    for j in range(2):
        print(i,j)


#8.Comentarios

#hola

#9.Listas

lista = [1,2,3,4,5]

#10.Comparaciones

if x == y:
    print(i)
    
    
nombre = "Julieta"
print(type(x))
print(type(num))
print(type(nombre))
print(type(lista))
print(type(tiene_credencial))
print(type(tiene_credencial))