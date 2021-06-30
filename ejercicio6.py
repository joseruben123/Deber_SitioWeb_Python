#ejercicio: Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene dos calificaciones denotadas 
# como C1 y C2. El aspirante que obtenga calificaciones mayores que 80 en ambos exámenes es aceptado; en caso contrario es rechazado.

C1=float(input("Ingresa la nota del examen 1:"))
C2=float(input("Ingresa la nota del examen 2:"))

if (C1 >= 80) and (C2 >= 80):

    print("Usted a sido aceptado")
else:

    print("Usted a sido rechazado")
