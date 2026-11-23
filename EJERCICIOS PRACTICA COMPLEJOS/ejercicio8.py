import random


pares=0
impares=0
mayor=0
menor=1001

print("10 numeros entre el 1 el 1000")

for i in range(10):
    numero=random.randint(1,1000)

    if i < 9:
        print(numero,end=", ")
    else:
        print(numero)

    if numero % 2 == 0:
        pares +=1
    else:
        impares +=1

    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
print("He generado", pares, "números pares y", impares, "números impares")
print("El número mayor ha sido el", mayor, "y el menor el", menor)

