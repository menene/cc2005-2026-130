# ==============================================================
# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Funciones
# DESCRIPCIÓN: Calculadora básica que usa funciones para
# realizar operaciones de suma, resta y multiplicación
# AUTOR: Erick Marroquin
# FECHA: 05/04/26
# ==============================================================

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b
 
def multiplicar(a, b):
    return a * b
 
x = float(input("Primer número: "))
y = float(input("Segundo número: "))
 
print("Suma:", sumar(x, y))
print("Resta:", restar(x, y))
print("Multiplicación:", multiplicar(x, y))