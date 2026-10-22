Precio = float (input("Escribe la cantidad de la cuenta: "))
descuento = float (input("Escribe el descuento: "))
if descuento >=0 and descuento <=100:
    cantidad = Precio * (descuento / 100)
    precio_final = Precio - cantidad 
    print (f"El precio final es de: {precio_final}")
else: 
    print ("error: el descuento debe estar entre 0 y 100")