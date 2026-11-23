import random

entero=int(input("Escribe un numero: "))

while entero < 10:
    print("Error numero incorrecto debe ser mayor o igual a 10")
    entero=int(input("Escribe un numero: "))

print("5 numeros pares aleatorios entre el 1 y el", entero)

for numero in random.sample(range(2, entero + 1,2), 5): #desde el 2 hasta el entero +1 y de dos en dos, mas los numeros que queremos
    print(numero)