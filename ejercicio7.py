#precio de un articulo y despues le aplicamos el iva
#nos devuelve el precio con decimales

iva=1.21

precio=float(input("Escribe el precio para aplicarle el IVA"))

precio_con_iva=round(precio*iva,2) #definimos el precio y lo que queremos, que nos de el precio con dos decimales

print(f"El precio con iva es {precio_con_iva}")