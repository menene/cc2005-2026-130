# ==============================================================
# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Listas
# DESCRIPCIÓN: Demostración de los métodos pop() y remove()
# para eliminar elementos de una lista
# AUTOR: Erick Marroquin
# FECHA: 05/04/26
# ==============================================================

lista_super = []

n = 3

while n > 0:
    producto = input("Ingrese un producto a la lista: ")
    
    if producto != "":
        lista_super.append(producto)
        
    print(lista_super)
    
    n = n - 1
    
#a = lista_super.remove("leche")
#print(lista_super, a)

#b = lista_super.pop()
#print(lista_super, b)
    
c = lista_super.pop(1)
print(lista_super, c)