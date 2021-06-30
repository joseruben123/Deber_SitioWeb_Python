#ejercicio: Diseñar un algoritmo tal que dados como datos dos variables de tipo entero, obtenga el resultado de la siguiente función:
#100*v si num=1
#100^v si num = 2
#100/v si num = 3 para v <>0
#0 cialquier otro valor de num

print("Ingrese los valores a continuacion: ")
NUM = int( input("Ingrese NUM: "))
V = int( input("Ingrese V: "))

Funcion = {
1 : 100*V,
2 : 100**V,
3 : 100/V
}

VAL = Funcion.get(NUM, 0)

print("Num es", NUM, "Por lo tanto")
print("Su caso es el", VAL)