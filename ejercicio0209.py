import random

numeroAle= random.randint(1,10)
contador = 0
opcion = 0
while opcion != numeroAle:
    opcion = int(input("Ingresa un numero para adivinarlo: "))
    contador += 1
    if opcion < numeroAle:
        print("EL numero a adivinar es mayor")

        print("Llevas " , contador , "intentos")
    elif opcion > numeroAle:
        print("El numero a adivinar es menor")

        print("Llevas " , contador , "intentos")
    else:
        print("Has acertado")


        if contador == 1:
            print("Felicidades has acertado a la primera")
        else:
            print("Has necesitado ", contador , "intentos")