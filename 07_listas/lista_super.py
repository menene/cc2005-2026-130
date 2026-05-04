# ==============================================================
# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Listas
# DESCRIPCIÓN: Lista de supermercado con menú interactivo para
# agregar, eliminar y mostrar elementos usando append y remove
# AUTOR: Erick Marroquin
# FECHA: 05/04/26
# ==============================================================

lista_super = []
opcion = ""

while opcion != "4":

    print("=== Lista de Super ===")
    print()
    print("1. Agregar elemento")
    print("2. Eliminar elemento")
    print("3. Mostrar lista")
    print("4. Salir")
    
    opcion = input("Ingresa una opción: ")
    
    if opcion == "1":
        elemento = input("Ingrese un elemento: ")
        lista_super.append(elemento.lower())
        
        print()
        print(elemento, "agregado exitosamente a la lista!")
        
    elif opcion == "2":
        elemento = input("Ingrese un elemento a eliminar: ")
        elemento = elemento.lower()
        
        count = lista_super.count(elemento)
        
        n = 0
        while count > 0:
            lista_super.remove(elemento)
            count = lista_super.count(elemento)
            
            n = n + 1
            
        print(n, "copias del elemento", elemento, "eliminado de al lista")
        
#         if count > 0:
#             lista_super.remove(elemento)
#             print()
#             print(elemento, "eliminado correctamente")
#         else:
#             print()
#             print(elemento, "no encontrado, imposible eliminar")
        
    elif opcion == "3":
        print()
        print(lista_super)
        print("Cuentas con", len(lista_super), "elementos") 
        
    elif opcion == "4":
        print()
        print("Suerte en tus compras...")
    
    else:
        print()
        print("Selecciona una opción correcta")
