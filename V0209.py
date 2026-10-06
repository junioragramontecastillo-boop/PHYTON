#GENERACION DE NUMEROS ALEATORIOS

import random

print(random.random())

print(random.randint(1,10)) #numeros random entre esos dos numeros

dado = random.randint(1,10)
print(dado)

#otra forma

print(random.uniform(1,10))


#CONVERSIÓN ENTRE TIPOS DE DATOS

entero= 45

decimales = 44.56812

texto1 = "333"
texto2 = "33.5"

#conversion entre entero y decimal

entero2=int(decimales) #decimal a entero usamos int
decimales2=float(entero) #entero a decimal usamos float

print(entero2)
print(decimales2)
decimales3=round(decimales,2) #para el numero de cifras que quiero que muestre en este caso dos
print(decimales3)

#para truncar un numero en el que quiero solo las dos cifras

decimales4=int(decimales*100)/100
print(decimales4)


#CONVERSION DE NUMERO A TEXTO

texto3=str(entero)
texto4=str(decimales)
print(texto3)
print(texto4)

#CONVERSION DE TEXTO A NUMEROS

entero2=int(texto1)
decimales2=float(texto2) #numeros con los que ya podemos operar
print(entero2)
print(decimales2)

#COMO PODEMOS VER QUE TIPO DE DATO TIENE UNA VARIABLE

entero="HOLA mundo"
entero = 5
entero = 45.6

print(type(entero))#nos devuelve el tipo directo
print(isinstance(entero,int)) #nos devuelve falso por que lo que hay no es un numero entero

#metodo type

if type(entero) is int:
    print("El numero es entero")
elif type(entero) is float:
    print("El numero es decimal")
elif type(entero) is str:
    print("El numero es un texto")
else:
    print("Es una vaina rara")

#metodo issintance

if isinstance(entero,int):
    print("El numero es entero")
elif isinstance(entero, float):
    print("El numero es decimal")
elif isinstance(entero, str):
    print("El numero es un texto")
else:
    print("Es una vaina rara")

#INTRUCCIONES REPETITIVAS

#USAMOS FOR CUANDO SABEMOS CUANTAS VECES VAMOS A REPETIR ALGO, SI NO LO SABEMOS USAMOS WHILE

print("INICIO")
for i in range(5): #del 0 al 5
    print(i)
    print("---")
print("FIN")

print("INICIO")
for i in range(3,7): #lo mismo pero para coger unos valores entre ellos
    print(i)
    print("---")
print("FIN")

print("INICIO")
for i in range(3,10,2): # aqui indicamos la secuencia que queramos de dos en dos por ejemplo
    print(i)
    print("---")
print("FIN")


print("INICIO")
for i in range(10,0,-2): #lo mismo pero hacia atrás
    print(i)
    print("---")
print("FIN")

print("INICIO")
vocales = "AEIOU"
for letra in vocales:
    print(letra)
    print("---")
print("FIN")


#WHILE

for i in range(0,5):
    print(i)
    print("---")


i=0 #iniciamos i a 0
while i<5: # si i es menor a 5 y los mostramos
    print(i)
    i+=1

import random

print("DADO CON WHILE")
dado = 0
contador = 0 #ponemos el contador en cero
while dado !=6:
    dado = random.randint(1,6)
    print(dado)
    contador += 1 #lo incrementamos para ver las tiradas que hemos tenido que hacer

print("Has tirado " , contador, "veces para que te salga un 6")