import random


dados=int(input("Introduce el numero de dados que vas a tirar: "))
caras=int(input("Introduce el numero de caras de los dados: "))
total=0
numeroDeCaras=4,6,8,10,12,20,100
if caras not in numeroDeCaras:
    print("La tirada no es valida, introduce un numero de caras válido")
else:
    total=0
    for i in range(1, dados + 1):
        tirada=random.randint(1, caras)
        total+=total
        print(f"Dado {i} Tiradas: {total}")
        print(f"Total de dados: {total}")

