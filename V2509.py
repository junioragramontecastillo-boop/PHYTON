from operator import truediv

calculoGordo = ((45+7.4) /3 + 2 ) **1

edad = 22
edad = edad + 1
edad+=1
print(edad)

print(7<5) # 7 es menor que 5 nos devuelve falso
print(14>3) # 14 es mayor que 3 nos devuelve verdadero

n = 1
print(n<=5)

#comparar dos cosas
n = 1
m=3
print(n==m) # nos dice falso por que no son iguales

print(n!=m) # nos dice verdadero por que  nos distintos

n = 4
print(5>=n and n>=2) #nos da true por que se cumplen las dos condiciones

n = 4
print(5<n or n<2)

encontrado = False

n= 5
print(n in range (1,7)) # nos da true por que el 5 esta en rango 1 a 6, si no daria false

n=4
print(n not in range (1,7)) #nos devuelve false por que si esta

print("A" in "AEIOU") #nos da true por que la A esta en el IN, si no da false

#LEER DATOS DE TECLADO
nombre = input("Introduce tu nombre: ")
edad =int(input("Dime tu edad: ")) #para leer numeros enteros debemos de poner int

if edad>=18:
    print("Tu nombre es", nombre, "y eres mayor de edad")
else:
    print("Tu nombre es ", nombre, "y eres menor de edad")


