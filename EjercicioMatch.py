usuarios = []
while True:
    print("1. Añadir Nombre")
    print("2. Eliminar")
    print("3. Mostrar")
    print("4. Salir")
    opcion=input("Introduce una opción: ")
    match opcion:
        case "1":
            nombre=input("Introduzca el Nombre del usuario: ")
            usuarios.append(nombre)
            print("Nombre añadido correctamente")
        case "2":
            nombre=input("Introduce el nombre a eliminar: ")
            if nombre in usuarios:
                usuarios.remove(nombre)
                print("Nombre eliminado correctamente")
            else:
                print("El nombre no existe debes añadirlo para eliminarlo")
        case "3":
            if usuarios:
                print("Usuarios:")
                for i, nombre in enumerate(usuarios, start=1):
                    print(f" Usuario {i}: {nombre}")
                print("Numero de usuarios: ", len(usuarios))
            else:
                print("No hay usuarios")
        case "4":
            print("Saliendo...")
            break
        case _:
            print("Opcion inválida")

