texto=input("Escribe un texto: ")

vocales="aeiouAEIOU"
resultado=""

vocalesQuitadas=0
espacios=0

for caracter in texto:
    if caracter in vocales:
        vocalesQuitadas+=1
    elif caracter == " ":
        espacios+=1
    else:
        resultado=resultado+caracter

print("Sin vocales ni espacios: ", resultado)
print("Vocales suprimidas: ", vocalesQuitadas)
print("Espacios: ", espacios)



