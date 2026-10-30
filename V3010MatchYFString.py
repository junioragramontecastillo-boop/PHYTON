#match sirve para evaluar el valor de una variable
#FString nos permite imprimir con formato


#MATCH

opcion=input("P para parar, C para continuar, o X para salir: ")

#podemos poner las opciones que queramos con barra vertical
match(opcion):

    case "P" | "p":
        print("Parando")
    case "C" | "c":
        print("Continuando")
        print("Continuando dos veces :) ")
    case "X" | "x":
        print("Saliendo")

    case _: #La _ es como default si no existe lo que pulsamos
        print("Opcion no válida")



#FSTRING
nombre= "Samuel"

edad=22
sueldo=1557.767

#con end es lo que ponemos al final
#con sep es el separados le ponemos lo que queramos y lo sacara en los espacios
print("Mi nombre es", nombre, "tengo", edad, "años y mi sueldo es de", sueldo, "$ al mes", end=".-\n", sep=" ")

#aqui ponemos la cadena y el signo % indica el tipo de variable %String, %decimal, %float
#podemos redondearlo tambien a dos decimales por ejemplo
print("Mi nombre es %s tengo %d y mi sueldo es de %.3f$ al mes" % (nombre, edad, sueldo))
print("Mi nombre es %s tengo %d y mi sueldo es de %.2f $ al mes" % (nombre, edad, sueldo))
print("Mi nombre es %s tengo %d y mi sueldo es de %f $ al mes" % (nombre, edad, sueldo))
#podemos ponerlo asi tambien
texto = "Mi nombre es %s tengo %d y mi sueldo es de %f $ al mes" % (nombre, edad, sueldo)

print(texto)

#para redondear usamos :. y el numero acontinuacion mas la f
print(f"Mi nombre es {nombre} tengo {edad} y mi sueldo es de {sueldo:.2f} $ al mes")

#para redondear decimales
porcentaje=0.457698

print(f"Porcentaje: {porcentaje:.2%}")

#para los miles nos lo separa
poblacion=34536366

print(f"Poblacion: {poblacion:,} habitantes")


#para alinearlos con el punto al mismo nivel

num1=45.55
num2=1456.7755
num3=564.123
num4=1.5
#si le ponemos 0 nos ocupa los espacios a la izquierda con ceros
print(f"{num1:08.2f}\n{num2:08.2f}\n{num3:08.2f}\n{num4:08.2f}")

#formatear textos

titular=f"Titular de la noticia"

#le indicamos que tendra 40 espacios a la derecha
print(f"*** {titular:<40} ***")

# a la izquierda
print(f"*** {titular:>40} ***")

#en el centro
print(f"*** {titular:^40} ***")

#para debugear y ver los errores que nos pueda dar

for i in range(5):
    n=i*0.456
    k=i/1.456
    print(f"{i=}, {n=}, {k=}")

#para que nos saque literal lo que queramos por pantalla
ficha=(f"""
FICHA DEL ALUMNO
================
Nombre: {nombre:^10}
Edad: {edad:^10}
Sueldo: {sueldo:^10.2f}
================""")

print(ficha)




