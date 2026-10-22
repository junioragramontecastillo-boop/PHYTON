palabra1 = input("Escribe la primera palabra")
palabra2 = input("Escribe la segunda palabra")
palabra3 = input("Escribe la tercera palabra")

palabras = [palabra1, palabra2, palabra3]
palabras.sort(reverse=True) #las ordenamos descendentemente
#palabras.sort() #con sort las ordenamos ascendentemente
print("Palabras ordenadas: ")
for palabra in palabras:
    print(palabra)



