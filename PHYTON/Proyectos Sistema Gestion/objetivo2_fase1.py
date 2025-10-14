#Nombre: LiLi Fernández Pedrosa 
# Grupo: 2ºDAM 

# 1. Operaciones básicas con dos enteros
print ("1. Operaciones con enteros")
numero = int (input ("Introduce el primer numero entero: "))
numero2 = int (input ("Introduce el segundo numero entero: "))
print ("La suma es: ", numero + numero2)
print ("La resta es: ", numero - numero2)
print ("La multiplicacion es: ", numero*numero2)

if numero2 !=0:
    print ("La division es: ", numero / numero2)
else:
    print ("No se puede dividir entre 0")

#2. Promedio de tres números reales.
print("\n2. Promedio de tres decimales")
decimal = float (input ("Introduce el primer número decimal: "))
decimal2 = float (input ("Introduce el segundo número decimal: "))
decimal3 = float (input ("Introduce el tercer número decimal: "))

promedio = round ((decimal + decimal2 + decimal3) /3, 2)
print ("El promedio redondeado a 2 decimales son: ", promedio)

#3. Comparaciones entre dos enteros.
print ("\n3. Comparaciones entre enteros")
numero6 = int (input ("Introduce el primer numero entero: "))
numero7 = int (input ("Introduce el segundo numero entero: "))
print ("¿El primer numero es mayor que el segundo?" , numero6 > numero7)
print ("¿Son iguales? ", numero6 == numero7)
print ("¿El segundo numero es distinto de 0?" , numero7 !=0)

#4. Operaciones lógicas con valores booleanos.
print ("\n4. Operaciones logicas")
booleano1 = eval (input ("Introduce el primer valor logico (True/False): "))
booleano2 = eval (input ("Introduce el segundo valor logico (True/False): "))
print ("And: ", booleano1 and booleano2)
print ("Or: ", booleano1 and booleano2)
print ("NOT del primero: ", not booleano1)
print ("NOT del segundo: ", not booleano2)

# 5. Suma y promedio de edades escritas como texto
print("\n5. Edades como texto")
edad = int(input("Introduce la primera edad: "))
edad2 = int(input("Introduce la segunda edad: "))
sumaEdades = edad + edad2
promedioEdades = round(sumaEdades / 2, 1)
print("Suma de edades:", sumaEdades)
print("Promedio de edades (1 decimal):", promedioEdades)

# 6. Evaluación de expresiones lógicas con reales
print("\n6. Evaluación lógica con reales")
numero = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
print ("(numero > 10) and (numero2 < 5): ", (numero > 10) and (numero2 < 5))
print("(numero == numero2) or (numero2 > 0):", (numero == numero2) or (numero2 > 0))
print ("Not (numero < numero2)", not (numero < numero2))

# 7. División de dos reales redondeada
print("\n7. División de reales")
decimal = float (input ("Introduce el primer numero decimal: "))
decimal2 = float (input ("Introduce el segundo numero decimal:"))
if decimal2 !=0:
    resultado = round (decimal / decimal2, 1)
    print("Resultado de la división redondeado a 1 decimal:", resultado)
else:
    print ("No se puede dividir entre 0")