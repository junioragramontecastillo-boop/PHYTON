texto=input("Ingresa un texto: ")

if texto[::2] or texto[1::2]:
    print(texto[::2], texto[1::2])