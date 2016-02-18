precioCompra = int(input("Introduce la cantidad de tu compra (solo el número): "))
if precioCompra <= 20:
	print ("Tu compra no llega al precio mínimo para conseguir descuento. El valor se queda igual:", precioCompra, "€")
elif precioCompra <= 100:
	precioCompra = precioCompra - precioCompra * 0.05
	print ("Tu compra ha recibido un descuento del 5%, el precio actual entonces:", precioCompra, "€" )

elif precioCompra > 100:
	precioCompra = precioCompra - precioCompra * 0.1
	print ("Tu compra ha recibido un descuento del 10%, el precio actual entonces:", precioCompra, "€" )