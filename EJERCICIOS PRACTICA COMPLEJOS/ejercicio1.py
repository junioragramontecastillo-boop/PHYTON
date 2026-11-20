

numero1=int(input("Ingresa numero 1:"))
numero2=int(input("Ingresa numero 2:"))

capicua=0


if numero1>numero2:

    inicio=numero2
    final=numero1
else:
    inicio=numero1
    final=numero2

total=0
capicuas=""

for i in range(inicio,final+1):

    numeros=str(i)

    if numeros==numeros[::-1]:
        if total == 0:
            capicuas= str(i)
        else:
            capicuas=capicuas + ", " + str(i)
        total=total+1


if total > 0:
    print("Numeros capicuas entre", numero1, "y", numero2, ":", capicuas)
    print("Hay un total de", total, "numeros capicuas")
else:
    print("No hay ningun numero capicua entre", numero1, "y" , numero2)








