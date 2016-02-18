primerNumero = int(input("Introduce un número entero: "))
segundoNumero = int(input("Introduce un segundo numero entero: "))
if primerNumero < 0 and segundoNumero < 0:
	print ("No se calcula la suma porque los dos números son negativos.")

if primerNumero < 0:
	print ("No se calcula la suma porque el primer número es negativo.")

if segundoNumero < 0:
	print ("No se calcula la suma porque el segundo número es negativo.")

if primerNumero >= 0 and segundoNumero >= 0:
        print ("La suma de los números es:", primerNumero + segundoNumero)
