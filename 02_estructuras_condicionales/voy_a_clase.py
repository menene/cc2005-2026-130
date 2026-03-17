# ==============================================================
# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Estructuras Condicionales
# DESCRIPCIÓN: condicional de ir a clase con if anidado
# AUTOR: Erick Marroquín
# FECHA: 16/03/26
# ==============================================================

dia = int(input("Ingese el día (1 = Lunes, 2 = Martes, etc): "))
hora = float(input("Ingrese la hora (formato 24 hrs):"))


if dia == 1 or dia == 2:

    if dia == 1:

        if hora >= 10.40 and hora <= 12.15:
            print("Voy a clase")

        else:
            print("No voy")

    else:

        if hora >= 8.40 and hora <= 10.15:
            print("Voy a clase")

        else:
            print("No voy")

else:
    print("No voy")
