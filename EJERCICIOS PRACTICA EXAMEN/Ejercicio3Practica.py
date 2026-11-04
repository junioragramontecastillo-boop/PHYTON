ano=int(input("Introduce el año para determinar si es bisiesto: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"{ano} es bisiesto")
else:
    print(f"{ano} no es bisiesto")
