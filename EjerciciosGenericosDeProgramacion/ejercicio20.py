numero=int(input("Ingresa un numero: "))


divisores=[]
for i in range(1,numero):
    if numero%i==0:
        divisores.append(i)
print("Los divisores de ", numero, "son ", str(divisores))