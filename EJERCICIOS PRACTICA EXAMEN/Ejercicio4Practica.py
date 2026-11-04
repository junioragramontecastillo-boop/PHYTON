# Ejercicio 4: Categorizar edades
edad=int(input("Introduce tu Edad: "))

if edad <= 0 or edad <= 2:
    print("Eres un bebe ")
elif edad <= 3 or edad <= 12:
    print("Eres un niño")
elif edad <= 13 or edad <= 17:
    print("Eres un adolescente")
elif edad <= 18 or edad <= 64:
    print("Eres un adulto")
elif edad >= 65:
    print("Eres un adulto mayor")
else:
    print("Edad no válida")

