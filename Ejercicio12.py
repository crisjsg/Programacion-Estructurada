primerNumero = int(input("Introduce un número entero: "))
segundoNumero = int(input("Introduce un segundo numero entero: "))
if primerNumero%2==0 and segundoNumero%2==0 and primerNumero < 50 and segundoNumero in range (100, 500):
	print ("La suma de los números introducidos es igual a:", primerNumero + segundoNumero)
else:
	print ("Has introducido un número que no cumplía los requisitos.")
	
