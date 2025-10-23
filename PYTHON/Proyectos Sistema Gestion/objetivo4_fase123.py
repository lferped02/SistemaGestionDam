#Nombre: LiLi Fernández Pedrosa 
# Grupo: 2ºDAM 

# Preguntar cuántos alumnos hay en el grupo (validando que el número sea mayor que 0 con un while)
while True:
    try:
        numeroAlumnos = int(input("Introduce el número de alumnos: "))
        if numeroAlumnos > 0:
            break
        else:
            print("Debe haber al menos un alumno.")
    except ValueError:
        print("Por favor, introduce un número válido.")

# Inicializar contadores y acumuladores
sumaMedias = 0
aprobados = 0
mejorar = 0
suspensos = 0

 # Por cada alumno:
for i in range(1, numeroAlumnos + 1):
    print("\nAlumno", i)
 # Pedir su nombre
    nombre = input("Nombre del alumno " + str(i) + ": ")
 # Preguntar cuántas notas tiene (también con validación)
    while True:
        try:
            numeroNotas = int(input("¿Cuántas notas tiene " + nombre + "? "))
            if numeroNotas > 0:
                break
            else:
                print("Debe tener al menos una nota.")
        except ValueError:
            print("Por favor, introduce un número válido.")
 # Solicitar las notas una a una (usando un for)
    suma = 0
    for j in range(1, numeroNotas + 1):
        while True:
            try:
                nota = float(input("Introduce la nota " + str(j) + ": "))
                suma += nota
                break
            except ValueError:
                print("Por favor, introduce una nota válida.")
 # Calcular la media del alumno
    media = suma / numeroNotas
    sumaMedias += media
 # Mostrar un mensaje según su media:
    print("Media de", nombre, ":", round(media, 2), end=" -> ")
 # Si la media es mayor o igual a 5, mostrar "Aprobado"
    if media >= 5:
        print("Aprobado")
        aprobados += 1
 # Si está entre 4 y 5, mostrar "Necesita mejorar"
    elif 4 <= media < 5:
        print("Necesita mejorar")
        mejorar += 1
 # Si es menor que 4, mostrar "Suspenso"
    else:
        print("Suspenso")
        suspensos += 1

# Al final, calcular la media general del grupo y mostrar:
media_grupo = sumaMedias / numeroAlumnos
 # Media del grupo
print("\n--- RESUMEN FINAL ---")
print("Media del grupo:", round(media_grupo, 2))
 # Número de aprobados
print("Aprobados:", aprobados)
 # Número de alumnos que necesitan mejorar
print("Necesita mejorar:", mejorar)
 # Número de suspensos
print("Suspensos:", suspensos)
