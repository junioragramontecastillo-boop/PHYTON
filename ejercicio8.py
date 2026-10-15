#metemos importe a pagar
#despues los meses
#nos debe de devolver el dinero que tenemos que pagar cada mes
#redondeamos a dos decimales

cantidad_a_pagar=float(input("Escribe la cantidad a pagar")) #para aceptar decimales escribimos float

numero_de_meses=int(input("Escribe el numero de meses"))

cantidad_final=round(cantidad_a_pagar/numero_de_meses,2)

print("La cantidad a pagar en " + str(numero_de_meses) + " meses es: " + str(cantidad_final))

