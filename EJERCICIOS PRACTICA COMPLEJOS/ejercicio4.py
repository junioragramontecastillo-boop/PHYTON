import random


for i in range(4): #los bloques
    clave=""

    for j in range(5): #los numeros
        grupo=random.randint(0,99999) #comprendidos entre este rango
        clave=clave+f"{grupo:05d}" #la longitud que queremos
        if j < 4:
            clave=clave + "-"
    print(clave)


