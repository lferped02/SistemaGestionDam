#Nombre: LiLi Fernández Pedrosa 
# Grupo: 2ºDAM 

# 1. Pide al usuario los siguientes datos con input():
    #Creamos 4 variables que son:
nombreYApellido = input ("Nombre: ") # El nombre y apellidos.
curso = input ("Curso: ") # El curso.
grupo = input ("Grupo: ") #El grupo.
RutaProyecto = input ("Ruta del proyecto: ") #La ruta del proyecto.

#Muestra el siguiente formato de salida: 
    #Lo que he hecho para que me salga como las indicaciones del ejercicio tenemos que pooner el "\n", para que haga un salto
print (
    "------------------------------\n"
	      "Ficha del alumno/a\n"
    "------------------------------\n"
    "Nombre: "+nombreYApellido,"\n"
    "Curso: "+ curso, "Grupo: "+grupo,"\n"
    "Ruta del proyecto: "+ RutaProyecto
    
)