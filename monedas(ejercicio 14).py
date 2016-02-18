#Rutinas
def contadorBilletes(cantidadDinero):
        listaBilletes = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01 ]
        listaCantidadBilletes = []
        posicionListaBilletes = 0
                while cantidadDinero >= listaBilletes[posicionListaBilletes]:
                cantidadDineroBilletes = cantidadDinero // listaBilletes[posicionListaBilletes]
                listaCantidadBilletes.append(cantidadDineroBilletes)
                cantidadDinero = cantidadDinero % listaBilletes[posicionListaBilletes]
                posicionListaBilletes += 1
                if cantidadDinero <= listaBilletes[posicionListaBilletes]:
                        posicionListaBilletes += 1
                return listaCantidadBilletes

#Programa
cantidadDinero = int(input("Introduce la cantidadDinero de dinero: "))
print (contadorBilletes(cantidadDinero))

