# Algoritmos y Programación Básica
# --------------------------------------------------------------
# TEMA: Ciclo For
# DESCRIPCIÓN: Calcula promedios de notas por estudiante y general
# AUTOR: Erick Marroquín
# FECHA: 15/04/26
# ==============================================================
cant_estudiantes = int(input("Ingrese la cantidad de estidoantes: "))
cant_actividades = int(input("Ingrese la cantidad de actividades: "))

total_estudiante = 0
total_general = 0
prom_estudiante = 0
prom_general = 0

for estudiante in range(1, cant_estudiantes + 1):
    print("Evaluando estudiante", str(estudiante))
    
    total_estudiante = 0
    
    for actividad in range(1, cant_actividades + 1):
        nota = float(input("Ingrese la nota de la activiad " + str(actividad) + ": "))
        total_estudiante = total_estudiante + nota
        
    prom_estudiante = total_estudiante / cant_actividades
    total_general = total_general + prom_estudiante
    
    print("Promedio estudiante", prom_estudiante)
    
prom_general = total_general / cant_estudiantes
print("Promedio general", prom_general)
    
    
    
    