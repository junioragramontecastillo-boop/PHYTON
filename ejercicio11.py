#mostrar tirada de dadso entre el 1,6 y mostrarlo en pantalla
import random
dado1=random.randint(1,6)
dado2=random.randint(1,6)

cont=0

while dado1!=dado2:
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    print(dado1 , "-" , dado2)
    cont+=1
if cont==1:
    print("Vaya suerte a la primera")
else:
    print("Has tenido que tirar" , cont , "veces para que salgan igual")
