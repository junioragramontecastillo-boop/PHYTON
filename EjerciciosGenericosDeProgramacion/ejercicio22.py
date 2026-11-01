numero=int(input("Ingrese un número: "))

if numero < 2:
    print("El número no es primo")
else:
    esPrimo=True #aqui lo ponemos como verdadero si encuentra un divisor es false
    for i in range (2,numero):
        if numero%i==0:
            esPrimo=False
    if esPrimo:
        print("El numero es primo")
    else:
        print("El numero no es primo")