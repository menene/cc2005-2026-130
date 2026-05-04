# ==============================================================
# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Listas
# DESCRIPCIÓN: Cálculo de promedio de notas utilizando listas
# y recorriendo sus elementos con un for (versión 3)
# AUTOR: Erick Marroquin
# FECHA: 05/04/26
# ==============================================================

# version 3
def promedio(notas):
    suma = 0
    n = len(notas)
    
    for nota in notas:
        suma = suma + nota
    
    return suma / n


#----------------------------

calificaciones = [90, 95, 100, 60, 89, 90, 91]

print("El promedio es:", promedio(calificaciones))
