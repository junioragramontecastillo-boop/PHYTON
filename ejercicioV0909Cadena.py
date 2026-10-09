original="Agramonte Castillo, Samuel Junior"

#vemos que posicion ocupa la coma con find, y lo ordenamos

n=original.find(", ")

apellido = original[:n]
nombre = original[n+2:]
print(apellido)
print(nombre)
resultado = nombre + " " + apellido
print(resultado)


#sacamos el nombre ordenado con los asteriscos en las vocales
for vocal in "aeiou":
    original = original.replace(vocal, "*")
    apellido = original[:n]
    nombre = original[n + 2:]
    resultado = nombre + " " + apellido
print(resultado)
