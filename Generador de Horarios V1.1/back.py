from PyQt5.QtCore import QObject, pyqtSignal
import random
import csv
import os

# Estructuras de datos
clases_disponibles = {} 

salones = {f'X{i}': {} for i in range(1, 23)}

profesores = {}

# Función para cargar clases desde un archivo CSV
def cargar_clases_desde_csv():
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Ruta del directorio del script actual
    file_path = os.path.join(script_dir, 'generador.csv')  # Ruta al archivo CSV relativa al directorio del script

    with open(file_path, newline='', encoding='utf-8') as archivo_csv:
        reader = csv.reader(archivo_csv)
        for row in reader:
            if len(row) >= 2:
                clases_disponibles[row[0]] = {'Duracion': int(row[1])}

# Cargar clases al inicio del programa
cargar_clases_desde_csv()

# Actualización de la función generar_horarios() y funciones relacionadas

def generar_horarios():
    for salon in salones:
        for dia in ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']:
            horario = generar_horario(dia)
            salones[salon][dia] = horario

def generar_horario(dia):
    horario = []

    # Obtener todas las clases disponibles
    clases_disponibles_hoy = list(clases_disponibles.keys())

    # Mezclar la lista para una selección aleatoria
    random.shuffle(clases_disponibles_hoy)

    for clase in clases_disponibles_hoy:
        duracion = clases_disponibles[clase]['Duracion']

        # Verificar si hay espacio disponible en el horario para esta clase
        if hay_espacio_para_clase(horario, duracion):
            # Añadir la clase con su horario correspondiente
            horario_clase = {'Clase': clase, 'Horario': obtener_horario_disponible(horario, duracion, dia), 'Dia': dia}
            horario.append(horario_clase)

    return horario

# Actualización de la función obtener_horario_disponible() y función relacionada

def obtener_horario_disponible(horario, duracion, dia):
    horas_disponibles = list(range(9, 16, 2))  # Cambio en el rango horario
    for clase_existente in horario:
        if clase_existente['Dia'] == dia:
            for hora_inicio, hora_fin in clase_existente['Horario']:
                horas_disponibles = [h for h in horas_disponibles if h not in range(hora_inicio, hora_fin)]
    
    horario_clase = []
    while duracion > 0 and horas_disponibles:
        hora = random.choice(horas_disponibles)
        horario_clase.append((hora, hora + 2))  # Asignar bloques de 2 horas
        horas_disponibles.remove(hora)
        duracion -= 2
    
    return horario_clase

# Actualización de la función hay_espacio_para_clase() y función relacionada

def hay_espacio_para_clase(horario, duracion):
    # Verificar si hay suficiente espacio para la nueva clase
    horas_disponibles = list(range(9, 18, 2))  # Cambio en el rango horario
    for clase_existente in horario:
        for hora_inicio, hora_fin in clase_existente['Horario']:
            horas_disponibles = [h for h in horas_disponibles if h not in range(hora_inicio, hora_fin)]
    
    return len(horas_disponibles) >= duracion

def siguiente_dia(dia):
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
    indice_dia = dias.index(dia)
    siguiente_indice = (indice_dia + 1) % len(dias)
    return dias[siguiente_indice]

# Función para añadir profesor a un salón y materia
def añadir_profesor():
    salon = input("Ingrese el nombre del salón: ")
    materia = input("Ingrese el nombre de la materia: ")
    profesor = input("Ingrese el nombre del profesor: ")
    
    if salon in salones and materia in clases_disponibles:
        for dia, horario in salones[salon].items():
            for clase in horario:
                if clase['Clase'] == materia:
                    clase['Profesor'] = profesor
                    print(f"Profesor {profesor} asignado a {materia} en {salon}.")
                    return  # Salir de la función después de asignar el profesor

        # Si llega aquí, la materia no fue encontrada en el horario del salón
        print(f"Error: La materia {materia} no encontrada en el horario del salón {salon}.")
    else:
        print("Error: Salón o materia no encontrados.")

# Función para mostrar horarios
def mostrar_horarios():
    for salon, horarios in salones.items():
        print(f"\nSalón: {salon}")
        for dia, horario in horarios.items():
            print(f"\n{dia}:")
            for clase in horario:
                profesor = clase.get('Profesor', 'Sin asignar')
                print(f"  {clase['Clase']} - {clase['Horario']} - Profesor: {profesor}")

def guardar_horarios():
    horarios_guardados = {}  # Diccionario para almacenar los horarios

    for salon, horarios in salones.items():
        if salon not in horarios_guardados:
            horarios_guardados[salon] = {}

        for dia, horario in horarios.items():
            if dia not in horarios_guardados[salon]:
                horarios_guardados[salon][dia] = []

            for clase in horario:
                profesor = clase.get('Profesor', 'Sin asignar')
                # Guardar los datos en el diccionario
                horarios_guardados[salon][dia].append({
                    'Clase': clase['Clase'],
                    'Horario': clase['Horario'],
                    'Profesor': profesor
                })

    nuevos_horarios = {}  # Diccionario para almacenar los nuevos horarios

    for salon, horario_salon in horarios.items():
        nuevos_horarios[salon] = {}
        for dia, clases in horario_salon.items():
            nuevos_horarios[salon][dia] = []
            for clase in clases:
                horario = clase['Horario']
                if len(horario) == 2:  # Verifica si hay dos elementos en el horario
                    for horario_individual in horario:
                        nueva_clase = clase.copy()  # Copia la clase actual
                        nueva_clase['Horario'] = horario_individual  # Actualiza el horario
                        nuevos_horarios[salon][dia].append(nueva_clase)
                else:
                    nuevos_horarios[salon][dia].append(clase)
    return nuevos_horarios


# Función para mostrar el horario de un salón específico
def mostrar_horario_salon():
    salon = input("Ingrese el nombre del salón: ")
    if salon in salones:
        print(f"\nHorario del Salón {salon}:")
        for dia, horario in salones[salon].items():
            print(f"\n{dia}:")
            for clase in horario:
                profesor = clase.get('Profesor', 'Sin asignar')
                print(f"  {clase['Clase']} - {clase['Horario']} - Profesor: {profesor}")
    else:
        print("Error: Salón no encontrado.")

# Función para editar materias
def editar_materia():
    print("\n--- Editar Materia ---")
    salon = input("Ingrese el nombre del salón: ").upper()
    dia = input("Ingrese el día (Lunes, Martes, Miércoles, Jueves o Viernes): ")

    if salon not in salones or dia not in salones[salon]:
        print("Error: Salón o día no encontrados en el horario.")
        return

    # Mostrar las materias actuales para seleccionar cuál editar
    print("\nMaterias en este horario:")
    for i, clase in enumerate(salones[salon][dia]):
        print(f"{i + 1}. {clase['Clase']} - {clase['Horario']}")

    # Pedir al usuario que elija una materia
    try:
        opcion_materia = int(input("\nSeleccione el número de la materia que desea editar: ")) - 1
        materia_editar = salones[salon][dia][opcion_materia]['Clase']
    except (ValueError, IndexError):
        print("Error: Selección no válida.")
        return

    print("\n--- Opciones de Edición ---")
    print("1. Editar Horario")
    print("2. Editar Nombre de la Materia")
    print("3. Eliminar Materia")
    print("4. Cancelar")

    opcion_edicion = input("\nSeleccione una opción: ")

    if opcion_edicion == '1':
        # Editar horario de la materia seleccionada
        nuevo_horario = []
        nuevo_horario1 = int(input("Ingrese el horario de inicio: "))
        while(nuevo_horario1 < 9 and nuevo_horario1 > 15):
            nuevo_horario1 = int(input("Ingrese el horario de inicio: "))
        nuevo_horario.append(nuevo_horario1)
        nuevo_horario2 = int(input("Ingrese el horario de fin: "))
        while(nuevo_horario2 < 11 and nuevo_horario1 > 17):
            nuevo_horario1 = int(input("Ingrese el horario de inicio: "))
        nuevo_horario.append(nuevo_horario2)
        salones[salon][dia][opcion_materia]['Horario'] = nuevo_horario
        print(f"Horario de {materia_editar} actualizado a {nuevo_horario} en {dia}.")
    elif opcion_edicion == '2':
        # Editar nombre de la materia
        nuevo_nombre = input("Ingrese el nuevo nombre de la materia: ")
        if nuevo_nombre in clases_disponibles:
            salones[salon][dia][opcion_materia]['Clase'] = nuevo_nombre
            print(f"Nombre de la materia actualizado a {nuevo_nombre} en {dia}.")
        else:
            print(f"Error: La materia {nuevo_nombre} no existe en el registro.")
    elif opcion_edicion == '3':
        # Eliminar materia
        salones[salon][dia].pop(opcion_materia)
        print(f"{materia_editar} eliminada del horario en {dia}.")
    elif opcion_edicion == '4':
        # Cancelar
        print("Operación cancelada.")
    else:
        print("Opción no válida.")
