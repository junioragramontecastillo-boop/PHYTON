import random

intentos = 0

while True:
    aleatorio = random.randint(1, 1000)
    intentos += 1
    print(aleatorio)

    if aleatorio == 666:
        print(f"¡Faltan {intentos} días para que se acabe todo!")
