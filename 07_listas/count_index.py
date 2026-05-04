# ==============================================================
# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Listas
# DESCRIPCIÓN: Uso de los métodos count() e index() para
# contar y localizar elementos dentro de una lista
# AUTOR: Erick Marroquin
# FECHA: 05/04/26
# ==============================================================

frutas = ["manzana", "naranja", "uva"]

cuenta = frutas.count("pera")
print(cuenta)

if cuenta > 0:
    pos = frutas.index("pera")
    print(pos)