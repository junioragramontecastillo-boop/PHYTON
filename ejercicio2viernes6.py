codigo = input("Introduce un código: ")
esCorrecto = True
numeros="0123456789"

# primero comprobamos si la longitud es correcta y hay un guíon (y solo uno)
if len(codigo) != 7 or codigo.count("-") != 1:
    esCorrecto = False
else:
    posicion = codigo.find("-")
    # Extraemos las dos partes a partir de la posición
    primeraParte = codigo[:posicion]
    segundaParte = codigo[posicion+1:]
    # La segunda parte tiene que ser de tre so cuatro caractéres y la primera de dos o tres
    if len(primeraParte) < 2 or len(segundaParte) < 3:
        esCorrecto = False
    else:
        # vamos a validar primero la primera parte
        for caracter in primeraParte:
            # ninguno de sus caracteres puede ser número o espacio
            # ya sabemos que no son guiones porque solo hay uno
            if caracter in numeros or caracter == " ":
                esCorrecto == False
        # y ahora la segunda.
        # primero probamos que es un numero
        if segundaParte.isdigit():
            # ahora sumamos los dos primeros caracteres
            suma = int(segundaParte[0]) + int(segundaParte[1])
            # y comprobamos si esa suma es igual a lo que queda en la segundaParte
            if suma != int(segundaParte[2:]):
                esCorrecto = False
        else:
            esCorrecto = False
# por último mostramos el resultado
if esCorrecto:
    print("El código es correcto")
else:
    print("El código es incorrecto")