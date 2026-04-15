# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Ciclo For
# DESCRIPCIÓN: Calcula el promedio de un número fijo de notas
# AUTOR: Erick Marroquín
# FECHA: 15/04/26
# ==============================================================
total = 0
 
for i in range(1, 6):
    nota = float(input("Ingresa la nota " + str(i) + ": "))
    total = total + nota
 
promedio = total / 5
print("Promedio:", promedio)