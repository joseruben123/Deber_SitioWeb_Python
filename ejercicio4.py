#ejercicio: Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10% si su sueldo es inferior a $600, 
# en caso contrario no tendrá aumento.

sueldo=float(input("Ingresa el total de sus sueldo: $"))

if sueldo < 600:
    aumento=sueldo+(sueldo*0.10)
    print("Usted tiene un aumento del 10(%) y su suelto total es: $", aumento)
else:
    print("Sue sueldo es superior a los 600$ no obtiene un aumento")