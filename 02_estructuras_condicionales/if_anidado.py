# ==============================================================
# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Estructuras Condicionales
# DESCRIPCIÓN: estructura if anidado
# AUTOR: Erick Marroquín
# FECHA: 16/03/26
# ==============================================================

numero = int(input("Ingrese un número: "))

if numero >= 0 and numero <= 20:
    print("Número entre 0 y 20")

    if numero <= 10:
        print("Número ente 0 y 10")

    else:
        print("Número entre 11 y 20")

else:
    print("numero no entre 0 y 20")

    if numero < 0:
        print("Número menor a 0")

    else:
        print("Número mayor a 20")
