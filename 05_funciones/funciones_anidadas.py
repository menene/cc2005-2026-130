# ==============================================================
# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Funciones
# DESCRIPCIÓN: Función que suma 4 números utilizando funciones
# anidadas, llamando a sumar() dentro de sumar4()
# AUTOR: Erick Marroquin
# FECHA: 05/04/26
# ==============================================================

def sumar(a, b):
    return a + b

def sumar4(a, b ,c ,d):
    primera_suma = sumar(a, b)
    segunda_suma = sumar(c, d)
    
    return sumar(primera_suma, segunda_suma)

num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))
num3 = int(input("Ingrese el numero 3: "))
num4 = int(input("Ingrese el numero 4: "))

resultado = sumar4(num1, num2, num3, num4)

print(resultado)