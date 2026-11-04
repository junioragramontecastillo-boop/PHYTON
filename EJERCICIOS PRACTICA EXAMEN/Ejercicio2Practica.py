# Ejercicio 2: Calculadora simple

n1=float(input("Introduce un número: "))
n2=float(input("Introduce un número: "))
operacion=input("Que operación quieres hacer? ")

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

if operacion == "+":
    resultado = n1 + n2
    print(f"El resultado es: {resultado}")
elif operacion == "-":
    resultado = n1 - n2
    print(f"El resultado es: {resultado}")
elif operacion == "*":
    resultado = n1 * n2
    print(f"El resultado es: {resultado}")
elif operacion == "/":
    if n1 / n2 == 0:
        print("Error: no se puede dividir entre 0")
    else:
        resultado = float("{0:.2f}".format(n1 / n2))
        print(f"El resultado es: {resultado}")

