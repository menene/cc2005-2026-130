# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Ciclo While
# DESCRIPCIÓN: Juego para adivinar un número secreto con límite de intentos
# AUTOR: Erick Marroquín
# FECHA: 15/04/26
# ==============================================================
secreto = 42
intentos = 1

intento = int(input("Adivina el número: "))
 
while intento != secreto and intentos < 3:
    if intento < secreto:
        print("Muy bajo. Intenta de nuevo.")
    else:
        print("Muy alto. Intenta de nuevo.")

    intento = int(input("Adivina el número: "))
    intentos = intentos + 1

if intento == secreto:
    print("¡Correcto! El número era", secreto, "te tomaron", intentos, "intentos")
else:
    print("Lo siento... te quedaste sin intentos... núnca sabras el número")