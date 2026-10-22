

clave1=input("Ingresa clave: ")
confirmacion=input("Confirma la contraseña: ")

intentos=0

if clave1==confirmacion:
    print("Las claves coinciden")
    clave1 = clave1.replace("", "*")
elif clave1!=confirmacion:
    clave1 = clave1.replace("", "*")
    print("Las claves no coinciden vuelve a intentarlo")
    clave1 = clave1.replace("", "*")
    intentos=intentos+1

