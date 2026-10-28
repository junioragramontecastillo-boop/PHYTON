import random

numero1=int(input("Introduce un el primer número: "))
numero2=int(input("Introduce el segundo número: "))

aleatorio=random.randint(numero1,numero2)

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

aleatorio=random.randint(numero1,numero2)

print(f"Numero aleatorio entre {numero1} y {numero2} : {aleatorio}")