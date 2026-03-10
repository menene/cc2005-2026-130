# ==============================================================
# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Variables y Expresiones
# DESCRIPCIÓN: Script que ejemplifica cada uno de los diversos
# operadores (aritméticos, relacionales y lógicos)
# AUTOR: Erick Marroquin
# FECHA: 05/10/26
# ==============================================================

# ==============================
# OPERADORES ARITMÉTICOS
# ==============================

x = 10
y = 3

print("Suma:", x + y)
print("Resta:", x - y)
print("Multiplicación:", x * y)
print("División:", x / y)
print("División entera:", x // y)
print("Módulo (residuo):", x % y)
print("Potencia:", x**y)


# ==============================
# OPERADORES RELACIONALES
# ==============================

print("Igual que:", x == y)
print("Diferente de:", x != y)
print("Mayor que:", x > y)
print("Menor que:", x < y)
print("Mayor o igual que:", x >= y)
print("Menor o igual que:", x <= y)


# ==============================
# OPERADORES LÓGICOS
# ==============================

a = True
b = False

print("AND:", a and b)
print("OR:", a or b)
print("NOT a:", not a)
print("NOT b:", not b)


# ==============================
# EXPRESIONES
# ==============================

edad = 20
nota = 85
asistencia = 90

print("Expresión 1:", (edad >= 18) and (nota >= 70))
print("Expresión 2:", (nota > 90) or (asistencia > 80))
print("Expresión 3:", not (edad < 18))
print("Expresión 4:", (edad >= 18) and (nota >= 70) and (asistencia >= 80))
print("Expresión 5:", ((edad > 18) and (nota > 80)) or (asistencia > 95))
