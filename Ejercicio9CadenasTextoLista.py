numeros = [10, 20, 30, 40, 50]

#accedemos metiendo la posicion y poniendole el nuevo valor que queramos
numeros[0], numeros[-1] = numeros[-1], numeros[0]

print(numeros)
