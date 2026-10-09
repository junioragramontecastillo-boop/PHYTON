import random


equipos = ["Fc Barcelona", "Real Madrid", "Betis FC", "Sevilla FC", "Getafe FC", "Athletic Club", "Atlético de Madrid", "Villareal FC", "Deportivo Alavés"
    , "Real Sociedad", "Rayo Vallecano FC", "Celta de Vigo", "Valencia", "Real Racing"]

resultado = random.randint(1,7)

for i in range(0,len(equipos),2):#el rango de la quiniela
    local=equipos[i]
    visitante=equipos[i+1]
    resultado = random.randint(1,3) #el resultado entre 1 y 3
    if resultado == 5 or resultado == 6: #si es 3 como no se puede ponemos la X
        print("    X    ")
    elif resultado == 7:
        print("2")
    else:
        print("    1")

    

    print(f"{local} vs {visitante} --> [{resultado}]")




