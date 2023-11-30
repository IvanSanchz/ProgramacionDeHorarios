from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog # Archivo CSV
from aviso_horarios_generados import Ui_horarios_generados # Aviso OK
from error_01 import Ui_error
import os
import shutil
import random
import csv
import json

class BackendManager(QtCore.QObject):
    generarHorariosSignal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        # Aquí se incluirían las variables y funciones del backend que necesitas

    @QtCore.pyqtSlot()
    def generarHorarios(self):
        # Aquí se colocaría la lógica para generar los horarios
        cargar_clases_desde_csv()
        generar_horarios()
        # Otras funciones necesarias del backend

        # Imprimir los horarios generados como ejemplo
        print("Horarios generados exitosamente.")
        # Emitir señal cuando los horarios se han generado
        self.generarHorariosSignal.emit()

class Ui_GenerarHorario(object):
    # Se define una señal personalizada para generar los horarios
    generarHorariosSignal = QtCore.pyqtSignal()
    def setupUi(self, GenerarHorario):
        GenerarHorario.setObjectName("GenerarHorario")
        GenerarHorario.resize(274, 136)
        self.label = QtWidgets.QLabel(GenerarHorario)
        self.label.setGeometry(QtCore.QRect(20, 15, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setFamily("Nunito Sans Black")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.toolButton = QtWidgets.QToolButton(GenerarHorario)
        self.toolButton.setGeometry(QtCore.QRect(20, 38, 241, 22))
        self.toolButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolButton.setAutoRaise(False)
        self.toolButton.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.openFileDialog) # Buscar Archivo CSV
        self.pushButton = QtWidgets.QPushButton(GenerarHorario)
        self.pushButton.setGeometry(QtCore.QRect(80, 92, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.emitGenerarHorariosSignal)

        # Agregar QLineEdit para mostrar la ruta del archivo
        self.lineEdit = QtWidgets.QLineEdit(GenerarHorario)
        self.lineEdit.setGeometry(QtCore.QRect(20, 60, 241, 20))  # Ajustar posición y tamaño
        self.lineEdit.setReadOnly(True)  # Hacer el QLineEdit de solo lectura

        self.retranslateUi(GenerarHorario)
        QtCore.QMetaObject.connectSlotsByName(GenerarHorario)

    def abrir_aviso_horarios_generados(self):
        self.aviso_window = QtWidgets.QDialog()
        self.ui_aviso = Ui_horarios_generados()
        self.ui_aviso.setupUi(self.aviso_window)
        self.aviso_window.show()

    def emitGenerarHorariosSignal(self):
        # Verificar si se ha seleccionado un archivo CSV
        if not self.lineEdit.text().endswith('.csv'):
            # Mostrar la ventana de error si no se ha seleccionado un archivo CSV
            self.mostrar_ventana_error()
            return
        # Se incluye la lógica del backend aquí
        cargar_clases_desde_csv()
        generar_horarios()

        # Imprimir los horarios generados como ejemplo
        print("Horarios generados exitosamente.")
        guardar_horarios()
        self.abrir_aviso_horarios_generados()
        
    def mostrar_ventana_error(self):
            # Crear y mostrar la ventana de error
            self.ventana_error = QtWidgets.QDialog()
            self.ui_error = Ui_error()
            self.ui_error.setupUi(self.ventana_error)
            self.ventana_error.show()

    def retranslateUi(self, GenerarHorario):
        _translate = QtCore.QCoreApplication.translate
        GenerarHorario.setWindowTitle(_translate("GenerarHorario", "Generar Horarios"))
        self.label.setText(_translate("GenerarHorario", "Archivo CSV"))
        self.toolButton.setText(_translate("GenerarHorario", "Buscar archivo"))
        self.pushButton.setText(_translate("GenerarHorario", "Generar Horarios"))

    def openFileDialog(self):
        # Abre el diálogo de archivo y filtra por archivos CSV
        file_name, _ = QFileDialog.getOpenFileName(None, "Open CSV", "", "CSV Files (*.csv)")
        if file_name:
            # Copia el archivo a la carpeta del proyecto
            current_dir = os.path.dirname(os.path.abspath(__file__))  # Directorio actual del script
            destination = os.path.join(current_dir, "generador.csv")
            # Actualiza el QLineEdit con la ruta del archivo
            self.lineEdit.setText(file_name)
            # Copia el archivo seleccionado a la carpeta del proyecto
            shutil.copy(file_name, destination)

# Resto del código del backend...

# Aquí añadimos la lógica del backend (copiar desde el inicio del código del backend)

# Estructuras de datos
clases_disponibles = {} 

salones = {f'X{i}': {} for i in range(1, 23)}

profesores = {}

# Función para cargar clases desde un archivo CSV
def cargar_clases_desde_csv():
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Ruta del directorio del script actual
    file_path = os.path.join(script_dir, 'generador.csv')  # Ruta al archivo CSV relativa al directorio del script
    try:
        with open(file_path, newline='', encoding='utf-8') as archivo_csv:
            reader = csv.reader(archivo_csv)
            for row in reader:
                if len(row) >= 2:
                    clases_disponibles[row[0]] = {'Duracion': int(row[1])}
    except:
        pass

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
    
    with open('horarios.txt', 'w') as archivo:
        json.dump(horarios_guardados, archivo, indent=4)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GenerarHorario = QtWidgets.QWidget()
    ui = Ui_GenerarHorario()
    ui.setupUi(GenerarHorario)
    GenerarHorario.show()
    sys.exit(app.exec_())