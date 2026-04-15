# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Ciclo While
# DESCRIPCIÓN: Valida la entrada de un número positivo
# AUTOR: Erick Marroquín
# FECHA: 15/04/26
# ==============================================================
numero = int(input("Ingresa un número positivo: "))
 
while numero <= 0:
    print("El número debe ser positivo.")
    numero = int(input("Ingresa un número positivo: "))
 
print("Número aceptado:", numero)