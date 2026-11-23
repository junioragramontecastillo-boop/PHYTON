import random
cadena=input("Introduce una cadena:")

resultado=""

for caracter in random.sample(cadena,len(cadena)):
    resultado=resultado+caracter
print("Resultado:",resultado)