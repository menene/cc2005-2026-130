# ==============================================================
# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Cadenas
# DESCRIPCIÓN: Uso de strip(), lstrip() y rstrip() para limpiar
# espacios en cadenas, aplicado a validación de input
# AUTOR: Erick Marroquin
# FECHA: 05/04/26
# ==============================================================

entrada = "   Pyt hon   "
 
print(entrada.strip())    # "Python"  — elimina ambos lados
print(entrada.lstrip())   # "Python   "  — solo izquierda
print(entrada.rstrip())   # "   Python"  — solo derecha

nombre = input("Tu nombre: ")

limpio = nombre.lower()
limpio = limpio.strip()

print(limpio)

if limpio == "erick":
    print("Hola Erick")
else:
    print("No son iguales")