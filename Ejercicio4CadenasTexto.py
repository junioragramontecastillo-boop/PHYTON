texto=input("Ingresa una cadena de texto: ")
espacios=0

for letra in texto:
    if letra == " ":
        espacios+=1

sinEspacios=texto.replace(" ","")
print("Texto sin espacios: ", sinEspacios)
print("He encontrado y suprimido", espacios, "espacios")


