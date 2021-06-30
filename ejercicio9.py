#ejercicio: Determinar si un número entero proporcionado por el usuario es primo. Un número primo es un entero que no tiene más divisores que 
# 
# él mismo y la unidad.

m=int(2)
primo="V"

num=float(input("Ingrese un numero:"))

while((primo == "V") and (m< num)):
    if((num % m)==0):
        primo = "F"
    else:
        m=m+1
if(primo == "V"):
    print("El numero es primo")
else:
    print("El numero no es primo")
        