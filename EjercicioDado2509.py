#Tiramos un dado y segun en que rango este nos muestra una cosa o otra

dado = 2
if dado in range (1,3):
    print("Has fallado")
else: #podemos hacerlo con elif
    if dado in range (3,4):
        print("Herida Leve")
    else: #elif
        if dado == 5:
            print("Herida Grave")
        else:
            print("Crítico")

