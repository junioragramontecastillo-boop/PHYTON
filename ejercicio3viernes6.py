texto = input("Escribe el texto a cifrar: ")
# los caracteres en posiciones pares
pares = texto[::2]
# y los de las posiciones impares
impares = texto[1::2]
#para probar...
#print(pares)
#print(impares)

# vamos a componer la cadena de salida
cifrado = ""
# primero ponemos los caracteres de las posiciones pares seguidos de x
for caracter in pares:
    cifrado += caracter
    cifrado += "x"
# y luego los de las posiciones impares seguidos de w
for caracter in impares:
    cifrado += caracter
    cifrado +="w"
# mostramos el resultado
print("Mensaje Oculto:", cifrado)
