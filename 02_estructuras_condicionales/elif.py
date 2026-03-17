# ==============================================================
# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Estructuras Condicionales
# DESCRIPCIÓN: estructura elif
# AUTOR: Erick Marroquín
# FECHA: 16/03/26
# ==============================================================


numero = int(input("Ingrese un número"))

if numero >= 0 and numero <= 10:
    print("Número entre 0 y 10")
elif numero > 10 and numero <= 20:
    print("Número entre 11 y 20")
elif numero < 0:
    print("Número menor que 0")
else:
    print("Número mayor que 20")
