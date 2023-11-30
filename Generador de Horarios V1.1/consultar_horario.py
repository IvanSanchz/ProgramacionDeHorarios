from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import os
import json

def cargar_desde_txt(nombre_archivo):
    ruta_archivo = os.path.join(os.getcwd(), nombre_archivo)
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo:
            data = json.load(archivo)
            return data

def procesar_string(cadena):
    # Eliminar corchetes
    cadena_sin_corchetes = cadena.replace('[', '').replace(']', '')
    
    # Reemplazar comas por 'a'
    cadena_final = cadena_sin_corchetes.replace(',', ' a')
    
    return cadena_final

def actualizar_datos():
    horarios = cargar_desde_txt('horarios.txt')
    nuevos_horarios = {}
    # Código para construir nuevos_horarios...
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

class Ui_ConsultarHorario(object):
    def setupUi(self, ConsultarHorario):
        ConsultarHorario.setObjectName("ConsultarHorario")
        ConsultarHorario.resize(561, 775)
        ConsultarHorario.setMouseTracking(False)
        self.tabWidget = QtWidgets.QTabWidget(ConsultarHorario)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 521, 731))
        self.tabWidget.setMouseTracking(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(33, 50, 451, 631))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(20)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(185, 18, 140, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setFamily("Nunito Sans Black")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(40, 60, 421, 631))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(20)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(178, 8, 150, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setFamily("Nunito Sans Black")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 30, 261, 22))
        self.comboBox_2.setAutoFillBackground(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(ConsultarHorario)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ConsultarHorario)

    def retranslateUi(self, ConsultarHorario):
        _translate = QtCore.QCoreApplication.translate
        ConsultarHorario.setWindowTitle(_translate("ConsultarHorario", "Consultar Horario"))
        # Asegúrate de que haya suficientes elementos en el encabezado vertical
        self.tableWidget.setRowCount(22 * 20)  # Total de salones multiplicado por 20
        horarios = actualizar_datos()
        # Asigna los nombres de los salones a las filas correspondientes
        row_count = 0
        for i in range(1, 23):
            for j in range(20):
                item = self.tableWidget.verticalHeaderItem(row_count)
                if item is None:
                    item = QTableWidgetItem()
                    self.tableWidget.setVerticalHeaderItem(row_count, item)
                item.setText(_translate("ConsultarHorario", f"X{i}"))
                row_count += 1
        
        column_count = 0  # Comenzamos en la primera columna
        row = 0
        # Iterar sobre las materias para mostrarlas una vez por cada salón
        for salon, horario_salon in horarios.items():
            for dia, clases in horario_salon.items():
                for clase in clases:
                    nombre_clase = clase['Clase']

                    # Obtener la celda actual en la tercera columna
                    item = self.tableWidget.item(row, column_count)
                    # Si la celda no está inicializada, inicializarla
                    if item is None:
                        item = QTableWidgetItem()
                        self.tableWidget.setItem(row, column_count, item)

                    # Insertar la información de la clase en la tercera columna
                    item.setText(_translate("ConsultarHorario", nombre_clase))

                    # Mover a la siguiente fila para la próxima materia
                    row += 1

        column_count = 1  # Comenzamos en la segunda columna
        row = 0
        # Iterar sobre los días de la semana para mostrarlos 4 veces por cada salón
        for salon, horario_salon in horarios.items():
            for dia, _ in horario_salon.items():
                for _ in range(4):
                    # Obtener la celda actual en la segunda columna
                    item = self.tableWidget.item(row, column_count)
                    # Si la celda no está inicializada, inicializarla
                    if item is None:
                        item = QTableWidgetItem()
                        self.tableWidget.setItem(row, column_count, item)
                    
                    # Insertar el nombre del día en la segunda columna
                    item.setText(_translate("ConsultarHorario", dia))
                    
                    # Mover a la siguiente fila para el próximo día de la semana
                    row += 1

        column_count = 2  # Comenzamos en la tercera columna
        row = 0
        # Iterar sobre las materias para mostrarlas una vez por cada salón
        for salon, horario_salon in horarios.items():
            for dia, clases in horario_salon.items():
                for clase in clases:
                    horario_clase = clase['Horario']
                    horario_clase = procesar_string(str(horario_clase))

                    # Obtener la celda actual en la tercera columna
                    item = self.tableWidget.item(row, column_count)
                    # Si la celda no está inicializada, inicializarla
                    if item is None:
                        item = QTableWidgetItem()
                        self.tableWidget.setItem(row, column_count, item)

                    # Insertar la información de la clase en la tercera columna
                    item.setText(_translate("ConsultarHorario", horario_clase))

                    # Mover a la siguiente fila para la próxima materia
                    row += 1
        
        column_count = 3  # Comenzamos en la cuarta columna
        row = 0
        # Iterar sobre las materias para mostrarlas una vez por cada salón
        for salon, horario_salon in horarios.items():
            for dia, clases in horario_salon.items():
                for clase in clases:
                    Profesor_clase = clase['Profesor']

                    # Obtener la celda actual en la tercera columna
                    item = self.tableWidget.item(row, column_count)
                    # Si la celda no está inicializada, inicializarla
                    if item is None:
                        item = QTableWidgetItem()
                        self.tableWidget.setItem(row, column_count, item)

                    # Insertar la información de la clase en la tercera columna
                    item.setText(_translate("ConsultarHorario", Profesor_clase))

                    # Mover a la siguiente fila para la próxima materia
                    row += 1

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ConsultarHorario", "Materia"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ConsultarHorario", "Día"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ConsultarHorario", "Horario"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ConsultarHorario", "Profesor"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("ConsultarHorario", "Horario General"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ConsultarHorario", "General"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("ConsultarHorario", "Materia"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("ConsultarHorario", "Día"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("ConsultarHorario", "Horario"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("ConsultarHorario", "Profesor"))
        self.label.setText(_translate("ConsultarHorario", "Horario del Salón"))
        self.comboBox_2.setItemText(0, _translate("ConsultarHorario", "..."))
        self.comboBox_2.setItemText(1, _translate("ConsultarHorario", "X1"))
        self.comboBox_2.setItemText(2, _translate("ConsultarHorario", "X2"))
        self.comboBox_2.setItemText(3, _translate("ConsultarHorario", "X3"))
        self.comboBox_2.setItemText(4, _translate("ConsultarHorario", "X4"))
        self.comboBox_2.setItemText(5, _translate("ConsultarHorario", "X5"))
        self.comboBox_2.setItemText(6, _translate("ConsultarHorario", "X6"))
        self.comboBox_2.setItemText(7, _translate("ConsultarHorario", "X7"))
        self.comboBox_2.setItemText(8, _translate("ConsultarHorario", "X8"))
        self.comboBox_2.setItemText(9, _translate("ConsultarHorario", "X9"))
        self.comboBox_2.setItemText(10, _translate("ConsultarHorario", "X10"))
        self.comboBox_2.setItemText(11, _translate("ConsultarHorario", "X11"))
        self.comboBox_2.setItemText(12, _translate("ConsultarHorario", "X12"))
        self.comboBox_2.setItemText(13, _translate("ConsultarHorario", "X13"))
        self.comboBox_2.setItemText(14, _translate("ConsultarHorario", "X14"))
        self.comboBox_2.setItemText(15, _translate("ConsultarHorario", "X15"))
        self.comboBox_2.setItemText(16, _translate("ConsultarHorario", "X16"))
        self.comboBox_2.setItemText(17, _translate("ConsultarHorario", "X17"))
        self.comboBox_2.setItemText(18, _translate("ConsultarHorario", "X18"))
        self.comboBox_2.setItemText(19, _translate("ConsultarHorario", "X19"))
        self.comboBox_2.setItemText(20, _translate("ConsultarHorario", "X20"))
        self.comboBox_2.setItemText(21, _translate("ConsultarHorario", "X21"))
        self.comboBox_2.setItemText(22, _translate("ConsultarHorario", "X22"))
        # Conectar la señal 'currentIndexChanged' a un método que maneje la selección del salón
            # Conectar la señal 'currentIndexChanged' a un método que maneje la selección del salón
        self.comboBox_2.currentIndexChanged.connect(self.mostrar_informacion_salon)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ConsultarHorario", "Por Salón"))
    
    def mostrar_informacion_salon(self, index):
        salon_seleccionado = self.comboBox_2.itemText(index)
        horarios = actualizar_datos()
        if salon_seleccionado in horarios:
            horario_salon = horarios[salon_seleccionado]

            row = 0
            for dia, clases in horario_salon.items():
                for clase in clases:
                    nombre_clase = clase['Clase']

                    # Obtener la celda actual en la tercera columna
                    item = self.tableWidget_2.item(row, 0)
                    # Si la celda no está inicializada, inicializarla
                    if item is None:
                        item = QTableWidgetItem()
                        self.tableWidget_2.setItem(row, 0, item)

                    # Insertar la información de la clase en la primera columna
                    item.setText(nombre_clase)

                    # Obtener la celda actual en la segunda columna
                    item = self.tableWidget_2.item(row, 1)
                    # Si la celda no está inicializada, inicializarla
                    if item is None:
                        item = QTableWidgetItem()
                        self.tableWidget_2.setItem(row, 1, item)

                    # Insertar el nombre del día en la segunda columna
                    item.setText(dia)

                    # Obtener la celda actual en la tercera columna
                    item = self.tableWidget_2.item(row, 2)
                    # Si la celda no está inicializada, inicializarla
                    if item is None:
                        item = QTableWidgetItem()
                        self.tableWidget_2.setItem(row, 2, item)

                    horario_clase = clase['Horario']
                    horario_clase = procesar_string(str(horario_clase))

                    # Insertar la información del horario en la tercera columna
                    item.setText(horario_clase)

                    # Obtener la celda actual en la cuarta columna
                    item = self.tableWidget_2.item(row, 3)
                    # Si la celda no está inicializada, inicializarla
                    if item is None:
                        item = QTableWidgetItem()
                        self.tableWidget_2.setItem(row, 3, item)

                    Profesor_clase = clase['Profesor']

                    # Insertar la información del profesor en la cuarta columna
                    item.setText(Profesor_clase)

                    # Mover a la siguiente fila para la próxima clase
                    row += 1

            # Limpiar las celdas restantes en la tabla si es necesario
            for i in range(row, self.tableWidget_2.rowCount()):
                for j in range(4):
                    item = self.tableWidget_2.item(i, j)
                    if item:
                        item.setText('')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConsultarHorario = QtWidgets.QWidget()
    ui = Ui_ConsultarHorario()
    ui.setupUi(ConsultarHorario)
    ConsultarHorario.show()
    sys.exit(app.exec_())
