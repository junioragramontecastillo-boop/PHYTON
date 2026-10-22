

clave1=input("Ingresa clave: ")
confirmacion=input("Confirma la contraseña: ")

intentos=0

while clave1!=confirmacion: #con un while hacemos el bucle hasta que sea valida
    print("Las claves coinciden, vuelve a intentarlo")
    clave1 = input("Ingresa clave: ")
    confirmacion=input("Confirma la contraseña")
print("Las claves coinciden")
