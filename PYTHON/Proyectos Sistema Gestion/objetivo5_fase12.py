#Nombre: LiLi Fernández Pedrosa 
# Grupo: 2ºDAM 
# ============================================
# 1. Crear funciones independientes para cada operación:
# • sumar()
# • restar()
# • multiplicar()
# • dividir()
# • potencia()
# • raiz_cuadrada()
# • modulo()
# ============================================

# 3. Cada función de operación debe:
# • Pedir los números necesarios al usuario.
# • Calcular el resultado y mostrarlo con dos decimales.
# 4. El programa debe gestionar los siguientes errores:
# • Evitar divisiones entre cero.
# • Controlar entradas no numéricas.

def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: debes introducir un número válido.")

def sumar():
    numero1 = pedir_numero("Introduce el primer número: ")
    numero2 = pedir_numero("Introduce el segundo número: ")
    resultado = numero1 + numero2
    print("Resultado de la suma: {:.2f}".format(resultado))

def restar():
    numero1 = pedir_numero("Introduce el primer número: ")
    numero2 = pedir_numero("Introduce el segundo número: ")
    resultado = numero1 - numero2
    print("Resultado de la resta: {:.2f}".format(resultado))

def multiplicar():
    numero1 = pedir_numero("Introduce el primer número: ")
    numero2 = pedir_numero("Introduce el segundo número: ")
    resultado = numero1 * numero2
    print("Resultado de la multiplicación: {:.2f}".format(resultado))

def dividir():
    numero1 = pedir_numero("Introduce el dividendo: ")
    while True:
        numero2 = pedir_numero("Introduce el divisor: ")
        if numero2 != 0:
            break
        print("Error: no se puede dividir entre cero.")
    resultado = numero1 / numero2
    print("Resultado de la división: {:.2f}".format(resultado))

def potencia():
    base = pedir_numero("Base: ")
    exponente = pedir_numero("Exponente: ")
    resultado = base ** exponente
    print("Resultado: {:.2f}".format(resultado))

def raiz_cuadrada():
    while True:
        numero = pedir_numero("Número: ")
        if numero >= 0:
            break
        print("Error: no se puede calcular la raíz de un número negativo.")
    resultado = numero ** 0.5
    print("Resultado: {:.2f}".format(resultado))

def modulo():
    numero1 = pedir_numero("Número: ")
    while True:
        numero2 = pedir_numero("Divisor: ")
        if numero2 != 0:
            break
        print("Error: no se puede calcular el módulo con divisor cero.")
    resultado = numero1 % numero2
    print("Resultado: {:.2f}".format(resultado))

# ============================================
# 2. Crear una función principal menu() que:
# • Muestre las opciones disponibles.
# • Llame a la función correspondiente según la elección del usuario.
# • Permita repetir el menú hasta seleccionar la opción de salida.
# ============================================

def operaciones_avanzadas():
    while True:
        print("\nOperaciones avanzadas:")
        print("a) Potencia")
        print("b) Raíz cuadrada")
        print("c) Módulo")
        print("d) Volver")
        opcion = input("Selecciona una opción: ").lower()

        if opcion == "a":
            potencia()
        elif opcion == "b":
            raiz_cuadrada()
        elif opcion == "c":
            modulo()
        elif opcion == "d":
            break
        else:
            print("Opción no válida.")

def menu():
    while True:
        print("\n=========================")
        print("  CALCULADORA AVANZADA")
        print("=========================")
        print("1) Sumar")
        print("2) Restar")
        print("3) Multiplicar")
        print("4) Dividir")
        print("5) Operaciones avanzadas")
        print("6) Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            sumar()
        elif opcion == "2":
            restar()
        elif opcion == "3":
            multiplicar()
        elif opcion == "4":
            dividir()
        elif opcion == "5":
            operaciones_avanzadas()
        elif opcion == "6":
            print("Fin del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
menu()
