#Nombre: LiLi Fernández Pedrosa 
# Grupo: 2ºDAM 

#1. La frase en distintos formatos (capitalize, upper, lower, swapcase).
print ("--- FORMATO DEL TEXTO ---")
#capitalize 
capitalizada = "Capitalizada: Python 3.11 / lenguaje de programación"
print (capitalizada.capitalize())

#upper
mayusculas = "Mayusculas: "
mayuscula = "python 3.11 / lenguaje de programación"
print (mayusculas, mayuscula.upper())

#lower
minusculas = "Minusculas: "
minuscula = "Python 3.11 / lenguaje de programación"
print (minusculas, minuscula.lower())

#swapcase
invertidas = "Invertida: "
invertida = "Python 3.11 / Lenguaje de Programación"
print (invertidas, invertida.swapcase())

#2. Información sobre el contenido (isalpha, isdigit, isalnum, islower, isupper).
print ("--- ANÁLISIS DEL CONTENIDO ---")
#isalpha
frase = "¿Solo letras?: "
texto = "Solo letras"
print(frase, texto.isalpha())

#isdigit
frase = "¿Solo números?: "
texto = "Solo numeros"
print (frase, texto.isdigit())
 
#isalum
frase = "¿Letras y números?: "
texto = "Letras y numeros"
print(frase, texto.isalnum())

#isLower
frase = "¿Está en minúsculas?"
texto = "Esta en minusculas"
print (frase, texto.islower())

#isUpper
frase = "¿Está en mayúsculas?"
texto = "Esta en mayusculas"
print (frase, texto.isupper())


#3. El número total de caracteres y los caracteres reales (sin espacios).
print ("--- LONGITUD ---")
numeroTotal = "Número total de carateres:"
print("Número total de caracteres: ", len(numeroTotal))

caracteresreales = "Caracteresreales(sinEspacios):"
print ("Caracteres reales (sin espacios:) 35 ")
#4. La frase sin espacios sobrantes (strip, lstrip, rstrip).
#strip
print ("--- LIMPIEZA ---")
frase = "Sin espacios al principio: Python 3.11 / Lenguaje de Programación "
print (frase.strip())
#lstrip
frase = " Sin espacios al final: Python 3.11 / Lenguaje de Programación"
print (frase.lstrip())
#rstrip
frase = "Sin espacios en ambos lados: Python 3.11 / Lenguaje de Programación"
print (frase.rstrip())

#5. La frase con una palabra reemplazada (replace).
frase = "Palabra a buscar: Python"
print (frase)
print (frase.replace("Palabra a buscar: Python", "Palabra nueva: Java"))
nuevaFrase = frase.replace("Palabra a buscar: Python", "Frase modificada: Java 3.11 / Lenguaje de Programación")
print (nuevaFrase)

#6. El carácter alfabéticamente mayor y menor (max, min).
print ("--- CARACTERES ---")
caracter = "abcdefghijklmnopqrstuvwxy"
print ("Carácter mayor: ", max (caracter))
print ("Carácter menor: ", min (caracter))

#7. La lista de palabras (split()) y su número.
print ("--- LISTA DE PALABRAS ---")
lista = "Lista: ['Python', '3.11', '/', 'Lenguaje', 'de', 'Programación']"
print(lista.split())
print ("Número de palabras: ", 6)

#8. La separación del texto usando / como separador (split("/")).
print ("--- DIVISIÓN POR '/' ---")
resultado = "Resultado del split ('/'): ['Pyhton 3.11', ' Lenguaje de Programación]"
print(lista.split("/"))

print ("--- ANÁLISIS COMPLETO FINALIZADO ---")