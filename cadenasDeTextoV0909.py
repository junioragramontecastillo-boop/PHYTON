#cadenas de texto
texto= "Hola mundo " + "cruel"
print(texto)
print(texto + "otra vez")
print(texto , "otra vez")
print(texto, "otras", 2, "veces")
print(texto+ " otras "+ str(2) + " veces") #de numero a cadena debemos de pasarlo nosotros con str

texto = texto + " otras "+ str(2) + " veces"
texto = texto , " otras " , str(2) , " veces" #con comas nos saca una lista
print(texto)


#para coger elementos de una cadena
texto = "Hola mundo cruel"
print(texto)
print(texto[2])
print(texto[3:6])
print(texto[:2])
print(texto[2:]) #desde la posicion dos hasta el final
print(texto[3:-4]) #empieza a contar desde el final hasta la posicion que pongamos
print(texto[2:12:2]) #del 2 al 12 pero de dos en dos
print(texto[::2]) #solo posiciones pares de la cadena
print(texto[1::2]) #posicones impares de la cadena
print(texto[::-1]) #cadena al reves

#como recorrer una cadena

texto = "Hola mundo cruel"

print(len(texto)) #longitud de una cadena

for indice in range(len(texto)):
    print("En la posicion ", indice , "aparece el caracter", texto[indice])

for letra in texto:
    print(letra)

for indice in range(len(texto)-1,-1,-1): #recorrer al reves
    print("En la posicion ", indice , "aparece el caracter", texto[indice])

print(texto.upper()) #para el texto en mayusculas
print(texto.lower()) #en minusculas
print(texto.swapcase()) #combiando

texto = "Hola mundo cruel"
print(texto.find("o")) #nos dice cuantas letras hay de esas

print(texto.find("do"))
print(texto.replace("o","x")) #nos sustituye la letra que queramos
print(texto.replace(" ","")) #quitamos los espacios

texto = "        Hola mundo cruel       "
print(texto)
print(texto.strip()) #texto corregido sin espacios
print(texto.lstrip()) #te quita los espacios de la izquierda
print(texto.rstrip()) #te quita espacios de la derecha

codigo = "3456"
print(codigo.zfill(6)) #cogemos una cadena de longitud 6 rellenando con 0 a la izquierda
