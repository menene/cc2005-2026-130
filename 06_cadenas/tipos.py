# ==============================================================
# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Cadenas
# DESCRIPCIÓN: Métodos de verificación de tipo de cadena
# (isdigit, isalpha, isalnum, isspace) con validación de input
# AUTOR: Erick Marroquin
# FECHA: 05/04/26
# ==============================================================

#print("12345".isdigit())    # True  — solo dígitos
#print("Hola".isalpha())     # True  — solo letras
#print("abc123".isalnum())   # True  — letras y dígitos
#print("   ".isspace())      # True  — solo espacios



#edad = input("Tu edad: ")
 
#if edad.isdigit():
#    print("Edad:", int(edad))
#else:
#    print("Eso no es un número.")
    
    
edad = input("Tu edad: ")
while not edad.isdigit():
    print("La edad debe ser numerica")
    edad = input("Tu edad: ")
    
# yo estoy seguro que es un valor numerico
edad = int(edad)

