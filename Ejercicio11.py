primerNumero = int(input("Introduce un número entero: "))
segundoNumero = int(input("Introduce un segundo numero entero: "))
tercerNumero = int(input("Introduce un tercer numero entero: "))
print ("Los números introducidos son:", primerNumero, segundoNumero, "y", tercerNumero )
if primerNumero == segundoNumero + tercerNumero :
	print ("Se cumple que N1 = N2 + N3")
elif segundoNumero == primerNumero + tercerNumero:
	print ("Se cumple que N2 = N1 + N3")
elif tercerNumero == primerNumero + segundoNumero:
	print ("Se cumple que N3 = N1 + N2")
else:
	print("Los números no cumplen la condición")
