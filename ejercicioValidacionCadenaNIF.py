#Escribe un programa que valide si un NIF español introducido por teclado es correcto. La
#longitud exacta de la cadena ha de ser de 9 caractéres. Los ocho primeros han de ser
#números comprendidos entre el 0 y el 9 y el último una letra que puede estar escrita en
#mayúsculas o minúsculas.

#-----------------------------------------------------------------------------------------
#Mejorar el programa anterior para que detecte si se trata de un NIF o un NIE y nos
#comunique, además de si es válido de que tipo es

letras="ABCDEFGHIJKLMNOPQRSTUVWXYZ" #DEFINIMOS las letras validas
letrasNIE="XYZ"
nif=input("Introduce tu nif o nie: ")
if len(nif)!=9: #comprobamos la longitud de la cadena con len
    print("La longitud del nif no es válida")
elif nif[-1] in letras and nif[-1] not in letras.upper(): #nos dice el ultimo caracter de la cadena y nos lo valida si no la ponemos en minuscula
#podemos hacerlo con is digit para que nos valide si son numeros la cadena
#tambien con isalpha nos da true si la ultima es una letra y false si no lo es
    print("El ultimo caracter no es una letra")
else:
    if nif[:-1].isdigit(): #estamos validando si son numeros menos la ultima posicion
        print("Es correcto")
    elif nif[0] in letrasNIE and nif[1:8].isdigit(): #si es primer caracter es valido y comprobamos que lo demas sea numero
        print("Es correcto")
    else:
        print("No es correcto ")





