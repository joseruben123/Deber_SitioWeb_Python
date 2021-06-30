#ejercicio: construir un algoritmo tal, que dado como dato la calificación de un alumno en un examen, escriba si aprobo o no


nota = input("Nota del alumno: ")

promedio = float(nota)

if promedio >= 7:
    print("Aprobado")
else:
    print("No aprobado")