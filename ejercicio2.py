#ejercicio: eUn vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas. El vendedor desea saber cuánto 
# dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes 
# tomando en cuenta su sueldo base y sus comisiones.

venta1=float(input("Ingresa el total de la venta 1: $"))
venta2=float(input("Ingresa el total de la venta 2: $"))
venta3=float(input("Ingresa el total de la venta 3: $"))
print("Perfecto")
sueldo=float(input("Ingresa el total de sus useldo mensual: $"))

comision=(venta1+venta2+venta3)*0.10

print("Su comsion por las ventas es: $", comision)
print("Su sueldo base incluida su comision es: $", sueldo+comision)