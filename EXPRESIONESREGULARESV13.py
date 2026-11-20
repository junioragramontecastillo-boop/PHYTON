# Las reglas básicas

# a		- El caracter a y ningún otro
# .c 		- El punto valida cualquier caracter (abc, a3c...)
# [abc] 	- Uno de los caracteres (a, b o c)
# [a-z]	- Un caracter en el rango indicado (a, p, x...) siguen la tabla ascci (la ñ no está incluida)
# [^aeiou]	- Cualquiera excepto estos (1, n, P...). El signo ^ tiene que ir el primero después del corchete
# \d		- Un dígito cualquiera
# \w		- Una letra, un dígito o el signo de subrayado _
# \W        - cualquiera que no esté incluido en el anterior: símbolos que no sean el _, espacios, etc.
# \s		- Un espacio, un tabulador o un salto de línea

 CARDINALIDAD:
  *		- 0 o mas veces
  +		- 1 o mas veces
  ? 		- 0 o 1 vez
  {n}		- exactamente n veces
  {n,m}	- entre n y m veces (ambas incluidas
  {n,}		- n o mas veces
  ^Hola	- Valida la cadena Hola si está al inicio
  mundo$	- Valida la cadena mundo si está al final
  a|b		- Alternativa (o a o b)

#MATCH
#VALIDA UNA CADENA SI ENCUENTRA UN PATRON QUE BUSCA AL PRINCIPIO DE LA CADENA

#SEARCH
#VALIDA LO QUE SEA SI SE ENCUENTRA EL PATRON DENTRO DE LA CADENA EN CUALQUIER POSICION

#FULLMATCH
#SOLAMENTE NOS DA VALIDA SI COINCIDE LA CADENA ENTERA


#IMPORTAMOS LA LIBRERIA
import re



#ponemos una r al patron que vamos a comparar en expresiones regulares

patron=r"123xxx"
cadena="123xxx"

if re.match(patron,cadena):
    print(cadena, "tiene el patron inicial")
else:
    print(cadena, "no tiene el patron inicial")

if re.search(patron,cadena):
    print(cadena, "tiene el patron inicial")
else:
    print(cadena, "no tiene el patron inicial")

if re.fullmatch(patron,cadena):
    print(cadena, "cumple con el patron inicial")
else:
    print(cadena, "no cumple con el patron inicial")

print("----------------------------------------------")

#un unico caracter que este entre 0 y 9 y al lado la longitud de numeros que son 7 en este caso y al lado las letras validas
#podemos poner lo que queramos dentro de los corchetes que tiene que estar representado dentro, por ejemplo el nie para validarlo
#si le ponemos los corchetes elige una entre las 3 si se lo quitamos tienen que aparecer
#y vamos poniendo el rango de las letras
#podemos poner ? , eso expresa que es opcional, + al menos 1, * todas las que quiera
patronNIE=r"[XYZ][0-9]{7}[A-HJ-NP-TV-Z]"
patronNIF=r"[0-9]{8}[A-HJ-NP-TV-Z]"
cadena="X28896844Ñ"

if re.fullmatch(patronNIF,cadena) or re.fullmatch(patronNIE,cadena):
    print(cadena, "cumple con el patron inicial")
else:
    print(cadena, "no cumple con el patron")

print("-----------------------------------------")

patron1=r"[A-ZÑ]{3}-[0-9]{3}"
patron2=r"[A-ZÑ]{2}-[0-9]{4}"
patron3=r"[A-ZÑ]{2,3}-[0-9]{3,4}"
codigo="AB-771476"
#if re.fullmatch(patron1,codigo) or re.fullmatch(patron2,codigo):
if re.fullmatch(patron3,codigo) and len(codigo)==7:
    posicion=codigo.find("-")
    suma1=int(codigo[posicion+1])
    suma2=int(codigo[posicion+2])
    suma=int(codigo[posicion+3:])
    if suma1+suma2==suma:
        print(codigo, "es valido")
else:
    print(codigo, "NO es un codigo valido")


patronFraccion=r"[0-9]+/[1-9][0-9]*" #no vale denominador 0 pero numerador si
fraccion=r"3/4"

if re.fullmatch(patronFraccion,fraccion):
    posicion=fraccion.find("/")
    numerador=int(fraccion[:posicion])
    denominador=int(fraccion[posicion+1:])
    print(fraccion, "vale", round(numerador/denominador,3))
else:
    print(fraccion, "NO es un fraccion válida")

print("--------------------------------------------")
print("Ejemplo con las matriculas de coche:")

matricula=r"1234 BCD"

patronMatricula1=r"[A-Z]{1,2}-[0-9]{4}"
patronMatricula2=r"[A-Z]{1,2}-[1-9]{4}-[A-ZÑ]{2}" #SI QUEREMOS QUE CUENTE LA Ñ LA PONEMOS
patronMatricula3=r"[0-9]{4}[ -]?[B-DF-HJ-NPR-TV-Z]{3}" #DEBEMOS DE PONER LAS LETRAS QUE ENTRAN LAS QUE NO NOS LAS SALTAMOS, EL ? ES POR QUE SI ES OPCIONAL UN ESPACIO O ASTERISCO

if re.fullmatch(patronMatricula1,matricula) or re.fullmatch(patronMatricula2,matricula) or re.fullmatch(patronMatricula3,matricula):
    print(matricula, "es una matricula válida")
else:
    print(matricula, "no es válida")
