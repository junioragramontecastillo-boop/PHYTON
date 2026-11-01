matricula=input("Ingresa el numero de la matricula: ")

letras="BCDFGHJKLMNPRSTVWXYZ"

if len(matricula) == 8 and (matricula[4] == " " or matricula[4] == "-"):
    matricula=matricula[0:4] + matricula[5:8]

if len(matricula)!=7:
    print("La matricula no es válida debe de contener 4 números y tres letras")
elif not matricula[0:4].isdigit():
    print("Incorrecto: los 4 primeros digitos deben de ser números")

else:
    letrasValidas=True
    for letra in matricula[4:7]:
        if letras not in letras:
            letrasValidas=False
    if letrasValidas:
        print("Es correcto")
    else:
        print("No es correcto")






