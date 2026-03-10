# ==============================================================
# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Variables y Expresiones
# DESCRIPCIÓN: Script que calcula la hipótenusa dados 2 catetos
# usando el teoréma de Pitágoras
# AUTOR: Erick Marroquin
# FECHA: 03/10/26
# ==============================================================

# ingreso de datos
cateto1 = float(input("Ingresa el valor del primer cateto: "))
cateto2 = float(input("Ingresa el valor del segundo cateto: "))

# cuadrados de los catetos
cuadrado1 = cateto1**2
cuadrado2 = cateto2**2

print("Cateto1^2:", cuadrado1)
print("Cateto2^2:", cuadrado2)

# suma de cuadrados
suma_cuadrados = cuadrado1 + cuadrado2
print("Suma de cuadrados:", suma_cuadrados)

# hipotenusa
hipotenusa = suma_cuadrados**0.5
print("Hipotenusa:", hipotenusa)
