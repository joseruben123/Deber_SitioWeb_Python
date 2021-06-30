#ejercicio: en una tienda se ofrece un descuento del 15% sobre el total de la compra y 
#un cliente desea saber cuánto deberá pagar finalmente por su compra.

total=float(input("Ingresa el total de la compra: $"))

descuento = total*0.15

print("El valor total de su pago es: $", total-descuento)
print("El total de su descuento de 15(%) aplicado es: $", descuento)