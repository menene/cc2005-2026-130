# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Ciclo While
# DESCRIPCIÓN: Muestra un menú de opciones interactivo
# AUTOR: Erick Marroquín
# FECHA: 15/04/26
# ==============================================================
opcion = "lo que sea"
 
while opcion != "3":
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Salir")
    opcion = input("Elige una opción: ")
 
    if opcion == "1":
        print("¡Hola!")
        
    elif opcion == "2":
        print("¡Adiós!")
        
    elif opcion == "3":
        print("Terminando programa...")

    else:
        print("Opción incorrecta, intentalo nuevamente")
 
print("Programa terminado.")