import random
encontrado = False
contador = 0
# Como no sabemos cuanto vamos a tardar en encontrar el número que nos piden
# usamos un while y una buooleana que pondremos a True cuando lo hayamos logrado
while encontrado == False:
    # creamos un número aleatorio dentro del rango que nos piden
    # vimos en clase, y está en los apuntes, la forma de obterner números aleatorios con decimales
    n = random.uniform(0.5, 2.5)
    # usamos un contador puesto que nos piden cuantos números necesitamos para conseguir nuestro resultado
    contador+=1
    print(n)
    # si al redondear el resultado a 3 cifras obtenemos lo mismo que al truncar el resultado y quedarnos
    # con su parte entera quiere decir que al reddondear a tres cifras, ls tres son ceros
    if round(n,3) == int(n):
        encontrado = True
# Al salir del bucle mostramos el resultado que se nos pide
print("He tenido que generar", contador, "números para encontrar uno con sus tres primeras cifras decimales a 0")