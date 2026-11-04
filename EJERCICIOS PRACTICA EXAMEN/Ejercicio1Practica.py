# Ejercicio 1: Determinar el mayor de dos números

n1=int(input("Introduce el primer numero: "))
n2=int(input("Introduce el segundo numero: "))

if n1 > n2:
    print(n1, "Es mayor que", n2)
elif n2 > n1:
    print(n2, "Es mayor que", n1)
elif n1 == n2:
    print("Los números son iguales")

