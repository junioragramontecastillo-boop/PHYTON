#Escribir un programa que pida por teclado un número al usuario y diga si es divisible por 3 o
#no

numero=int(input("Ingresa un numero: "))

if numero % 3 == 0:
    print("El numero es divisible por 3")
else:
    print("El numero no es divisble por 3")