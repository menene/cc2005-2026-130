# ==============================================================
# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Variables y Expresiones
# DESCRIPCIÓN: Script para calcular el total a pagar de una
# cuenta
# AUTOR: Erick Marroquin
# FECHA: 05/10/26
# ==============================================================

# Solicitar datos al usuario
precio = float(input("Ingresa el precio del producto: "))
cantidad = float(input("Ingresa la cantidad comprada: "))
descuento = float(input("Ingresa el porcentaje de descuento (ej. 10 para 10%): "))
impuesto = float(input("Ingresa el porcentaje de impuesto (ej. 12 para 12%): "))

# subtotal
subtotal = precio * cantidad
print("Subtotal:", subtotal)

# descuento
descuento_aplicado = subtotal * (descuento / 100)
print("Descuento aplicado:", descuento_aplicado)

# subtotal
subtotal_desc = subtotal - descuento_aplicado
print("Subtotal con descuento:", subtotal_desc)

# impuestos
impuesto_aplicado = subtotal_desc * (impuesto / 100)
print("Impuesto aplicado:", impuesto_aplicado)

# total
total = subtotal_desc + impuesto_aplicado
print("Total a pagar:", total)
