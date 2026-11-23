texto = input("Introduce la cantidad y la moneda (E euros, P pesos, R rupias, F francos): ")
texto = texto.strip().upper().replace(",", ".")
letra = texto[-1]
cantidad = float(texto[:-1])

if letra == "E":
    pesos = cantidad * 27.93
    rupias = cantidad * 102.81
    francos = cantidad * 0.93
    print(f"{cantidad} euros equivalen a {pesos:.4f} pesos cubanos, {rupias:.4f} rupias o {francos:.4f} francos suizos")
elif letra == "P":
    euros = cantidad / 27.93
    print(f"{cantidad} pesos cubanos equivalen a {euros:.4f} euros")
elif letra == "R":
    euros = cantidad / 102.81
    print(f"{cantidad} rupias equivalen a {euros:.4f} euros")
elif letra == "F":
    euros = cantidad / 0.93
    print(f"{cantidad} francos suizos equivalen a {euros:.4f} euros")
else:
    print("Moneda no reconocida")