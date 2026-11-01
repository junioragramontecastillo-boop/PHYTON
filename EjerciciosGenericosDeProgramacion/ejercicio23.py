import random

aleatorio = random.randint(10000000,50000000)
esPrimo=False

while not esPrimo:
    aleatorio=random.randint(10000000,50000000)
    esPrimo=True
    for i in range (2,aleatorio):
        if aleatorio%i==0:
            esPrimo=False
print("Numero Primo: ", aleatorio)

