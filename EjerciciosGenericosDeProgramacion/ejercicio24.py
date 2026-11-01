for numero in range(2,101):
    esPrimo=True
    for i in range(2,numero):
        if numero%i==0:
            esPrimo=False
    if esPrimo:
        print(numero)