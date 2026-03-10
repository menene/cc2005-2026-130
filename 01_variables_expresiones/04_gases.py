# ==============================================================
# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Variables y Expresiones
# DESCRIPCIÓN: Script para calcular la densidad de gases
# AUTOR: Erick Marroquin
# FECHA: 05/10/26
# ==============================================================

# constante de los gases ideales (atm·L/mol·K)
R = 0.082

# ingreso de datos
presion = float(input("Ingresa la presión (atm): "))
volumen = float(input("Ingresa el volumen (L): "))
temperatura = float(input("Ingresa la temperatura (K): "))

# calcular moles (n = PV / RT)
moles = (presion * volumen) / (R * temperatura)
print("Número de moles:", moles)

# calcular densidad
masa_molar = float(input("Ingresa la masa molar del gas (g/mol): "))
masa = moles * masa_molar
print("Masa del gas (g):", masa)

# densidad
densidad = masa / volumen
print("Densidad del gas (g/L):", densidad)
