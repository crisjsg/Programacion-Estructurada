sueldoBruto = int(input("Introduce tu sueldo en bruto para saber cuanto cobraras neto: "))
retencion = sueldoBruto * 0.2
sueldoNeto = sueldoBruto - retencion
print ("Tu sueldo neto en caso de cobrar", sueldoBruto, "€ es:", sueldoNeto,"€")
input("Apreta cualquier boton para cerrar el programa una vez hayas visto tu sueldo neto")