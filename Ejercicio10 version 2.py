#10. Modifica el programa anterior para que en vez de mostrar un mensaje genérico en el caso
#de que alguno o los dos números sean negativos, escriba una salida diferenciada para cada
#una de las situaciones que se puedan producir, utilizando los siguientes mensajes:
#a. No se calcula la suma porque el primer número es negativo.
#b. No se calcula la suma porque el segundo número es negativo.
#c. No se calcula la suma porque los dos números son negativos.

def cogerNumeros(numero):
	numero = int(input("Introduce la cantidad de números que vayas a coger: "))
	listaNumeros = []
	listaNumeros.append(numero)

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
