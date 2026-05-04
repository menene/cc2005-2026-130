# ==============================================================
# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Cadenas
# DESCRIPCIÓN: Uso de endswith() y startswith() para verificar
# el inicio y fin de una cadena
# AUTOR: Erick Marroquin
# FECHA: 05/04/26
# ==============================================================

archivo = "informe_final.pdf"
 
if archivo.endswith(".pdf"):
    print("Es un PDF")
 
correo = "jose@uvg.edu.gt"
 
if correo.startswith("jose"):
    print("Correo de José")