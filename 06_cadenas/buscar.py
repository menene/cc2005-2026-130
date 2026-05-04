# ==============================================================
# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Cadenas
# DESCRIPCIÓN: Función que busca un término dentro de un texto
# usando find(), de forma insensible a mayúsculas
# AUTOR: Erick Marroquin
# FECHA: 05/04/26
# ==============================================================

def buscar_texto(texto, termino):
    texto_min = texto.lower()
    pos = texto_min.find(termino.lower())
    
    if pos >= 0:
        print(termino.upper(), "si se encontro")
    else:
        print(termino.upper(), "no se encontro")

# ----------------------------------------------

texto = "El gato está en el tejado" 

buscar_texto(texto, "Gato")
buscar_texto(texto, "perro")