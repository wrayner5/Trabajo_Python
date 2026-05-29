estudiantes = []
continuar =  "si"
while continuar.lower()=="si":
    nombre = input("Ingrese el nombre del estudiante")
    nota1 = float(input("Ingrese la nota 1:"))
    nota2 = float(input("Imgrese la nota 2:"))
    nota3 = float(input("Ingrese la nota 3:"))
    promedio= (nota1+nota2+nota3) / 3
    if promedio >=3.0:
        estado = "Aprobado"
    else:
        estado ="Reprobado"   
    estudiantes.append([nombre,promedio,estado])
    print("Estudiante:",nombre)
    print("Promedio:round",promedio,2)
    print("Estado:",estado)
    continuar=input("¿Desea registar mas estudiantes si,no")
print("Resumen Final ")
for est in estudiantes:
    print ("Nombre:",est[0],"|Promedio:",round(est[1],2),"|Estado:",est[2])
