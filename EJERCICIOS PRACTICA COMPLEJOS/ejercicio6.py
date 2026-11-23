texto1="Examen 1T01"
texto2="Octubre-2025"


resultado=texto1[7:11] + "-" + texto2[8:12] + " " + texto1[0:6] + " " + texto2[0:7]

longitud=len(texto1) + len(texto2)

print("Resultado: ", resultado, "(" + str(longitud) + ")")
