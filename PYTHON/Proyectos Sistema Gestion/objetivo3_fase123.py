#Nombre: LiLi Fernández Pedrosa 
# Grupo: 2ºDAM 

#1. Evaluar un número
#Pide un número entero y muestra:
numero = int (input ("Introduce un numero entero: "))
 #•"El número es positivo" si es mayor que 0.
if numero > 0:
    print ("El numero es positivo")
 #•"El número es negativo" si es menor que 0.
elif numero < 0:
    print ("El numero es negativo")
 #•"El número es cero" en cualquier otro caso.
else: 
    print ("El numero es cero")

#2. Comparar dos números
#Pide dos números entero y muestra uno de estos tres mensajes:
numero = int (input ("Introduce el primer numero entero: "))
numero2 = int (input ("Introduce el segundo numero entero: "))
 #•“El primero es mayor que el segundo.”
if numero > numero2:
    print ("El primero es mayor que el segundo")
 #•“El segundo es mayor que el primero.”
elif numero2 < numero:
    print ("El segunfo es mayor que el primero")
 #•“Ambos son iguales.”
else:
    print ("Ambos son iguales")

#3. Comprobar texto dentro de una frase
#Pide una frase y una palabra, y muestra:
frase = input ("Escribe una frase: ")
palabra = input ("Escribe una palabra para buscar: ")
 #•“La palabra está en la frase.” si aparece,
if palabra in frase:
    print ("La palabra esta en la frase")
 #•o “La palabra no se encuentra.” si no aparece.
else:
    print ("La palabra no se encuentra")

#4. Verificar el formato de una cadena
#Pide un texto y muestra
texto = input ("Escribe un texto: ")
 #•“Empieza por mayúscula.” si el texto empieza por una letra mayúscula.
if texto and texto [0].isupper():
    print ("Empieza en mayuscula")
 #•“Termina en punto.” si finaliza con un punto (.).
elif texto and texto.endswith("."):
    print ("Termina en punto")
 #•“El texto no cumple las condiciones.” si no cumple ninguna de las dos.
else: 
    print ("El texto no cumple las condiciones")

#5. Clasificar una nota
#Pide una nota numérica (de 0 a 10) y muestra el nivel del alumno
nota = float(input("Introduce una nota entre 0 y 10: "))
# según la nota:
if 0 <= nota <= 4:
    print("Insuficiente")
elif nota == 5:
    print("Suficiente")
elif nota == 6:
    print("Bien")
elif 7 <= nota <= 8:
    print("Notable")
elif 9 <= nota <= 10:
    print("Sobresaliente")
else:
    print("Nota no válida")

print ("Fin del programa.")