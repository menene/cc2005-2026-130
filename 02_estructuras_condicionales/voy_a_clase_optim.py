# ==============================================================
# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Estructuras Condicionales
# DESCRIPCIÓN: condicional de ir a clase con expresión
# booleana compleja. Versión optimizada
# AUTOR: Erick Marroquín
# FECHA: 16/03/26
# ==============================================================

dia = int(input("Ingese el día (1 = Lunes, 2 = Martes, etc): "))
hora = float(input("Ingrese la hora (formato 24 hrs):"))

if (dia == 1 and (hora >= 10.40 and hora <= 12.15)) or (
    dia == 2 and (hora >= 8.4 and hora <= 10.15)
):
    print("voy a clase")

else:
    print("No voy")
