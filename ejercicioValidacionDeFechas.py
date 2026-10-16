#Escribe un programa que reciba por teclado una fecha en el formato DD/MM/YYYY. El
#programa debe de comprobar si la fecha es correcta teniendo en cuenta:
#Qué el formato sea el correcto
#Escribe un programa que reciba por teclado una fecha en el formato DD/MM/YYYY. El
#programa debe de comprobar si la fecha es correcta teniendo en cuenta:
#- Qué el formato sea el correcto
#- Que la fecha sea totalmente válida teniendo en cuenta incluso los años que son bisiestos
#(aquellos que son divisibles entre cuatro).

fecha=input("Introduce tu fecha: ")

if len(fecha)!=10:
    print("La fecha no es válida")
elif fecha[2]  != "/" or fecha[5] !="/": #comprobamos que la posicion 2 y 5 haya las barras
    print("La fecha es incorrecta, escríbela correctamente")
else:
    dia=fecha[:2] #comprobamos las posiciones de los numeros
    mes=fecha[3:5]
    ano=fecha[6:]
    if dia.isdigit() and mes.isdigit() and ano.isdigit(): #aqui comprobamos que sean digitos
        dia=int(dia) #los pasamos a entero
        mes=int(mes)
        ano=int(ano)
        if dia == 0 or dia > 31 or mes == 0 or mes > 12: #comprobamos si el dia es 0 o mayor que 31 y el mes igual
            print("Día o mes incorrecto")
        else:
            if dia ==31 and (mes == 2 or mes == 4 or mes == 6 or mes == 9 or mes == 11): #comprobamos que los meses no tengan 31 dias
                print("Este mes no puede tener 31 dias")
            elif mes == 2 and dia == 30: # comprobacion de febrero
                print("Este mes no puede tener 30 dias")
            elif mes == 2 and dia == 29:
                if ano%4==0 and (ano % 100 != 0 or ano % 400 == 0): #comprobacion de año bisiesto
                    print("Fecha Válida, año bisiesto")
                else:
                    print("Febrero no puede tener 29 dias si no es bisiesto")

            else:
                print("Fecha correcta")

    else:
        print("Fecha incorrecta")


