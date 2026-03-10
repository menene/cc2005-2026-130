# ==============================================================
# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Variables y Expresiones
# DESCRIPCIÓN: Script que ejemplifica el uso de la función
# input para el ingreso de datos
# AUTOR: Erick Marroquin
# FECHA: 05/10/26
# ==============================================================

# ingreso de datos
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

print("--- OPERACIONES ARITMÉTICAS ---")

print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicación:", num1 * num2)
print("División:", num1 / num2)
print("División entera:", num1 // num2)
print("Módulo:", num1 % num2)
print("Potencia (num1^num2):", num1**num2)


print("--- EXPRESIONES RELACIONALES ---")
print("¿Son iguales?:", num1 == num2)
print("¿Son diferentes?:", num1 != num2)
print("¿num1 es mayor que num2?:", num1 > num2)
print("¿num1 es menor o igual que num2?:", num1 <= num2)


print("--- EXPRESIONES LÓGICAS ---")
print("Expresión 1:", (num1 > 0) and (num2 > 0))
print("Expresión 2:", ((num1 + num2) > 10) or ((num1 * num2) < 5))
print("Expresión 3:", not ((num1 - num2) == 0))
print("Expresión 4:", ((num1**2) + (num2**2)) > (2 * num1 * num2))
print("Expresión 5:", ((num1 > num2) and (num2 != 0)) or ((num1 % 2) == 0))
print("Expresión 6:", (((num1 + 5) * num2) > 50) and not ((num1 - num2) < 0))
