# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Ciclo For
# DESCRIPCIÓN: Genera una tabla de multiplicar hasta un tope
# AUTOR: Erick Marroquín
# FECHA: 15/04/26
# ==============================================================
numero = int(input("Ingrese el número: "))
tope = int(input("Hasta qué número quieres llegar: "))
 
for i in range(1, tope + 1):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
