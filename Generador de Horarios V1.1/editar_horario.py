from PyQt5 import QtCore, QtGui, QtWidgets
import os
import json

from error_01 import Ui_error

def cargar_desde_txt(nombre_archivo):
    ruta_archivo = os.path.join(os.getcwd(), nombre_archivo)
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo:
            data = json.load(archivo)
            return data


class Ui_EditarHorario(object):
    def setupUi(self, EditarHorario):
        # Conectar la señal de la otra ventana a la función que recibe los datos
        EditarHorario.setObjectName("EditarHorario")
        EditarHorario.resize(301, 161)
        self.label_3 = QtWidgets.QLabel(EditarHorario)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 261, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(EditarHorario)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 261, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(EditarHorario)
        self.lineEdit.setGeometry(QtCore.QRect(20, 80, 261, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(EditarHorario)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 30, 261, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(EditarHorario)
        self.pushButton.setGeometry(QtCore.QRect(110, 120, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Confirmar")

        # Conectar el botón "Confirmar" con la función para editar el horario
        self.pushButton.clicked.connect(self.editar_horario)
        
        self.retranslateUi(EditarHorario)
        QtCore.QMetaObject.connectSlotsByName(EditarHorario)

    def abrir_aviso(self):
        from aviso_horario_editado import Ui_horario_editado
        # Crear la ventana de aviso
        self.aviso_window = QtWidgets.QDialog()
        self.ui_aviso = Ui_horario_editado()
        self.ui_aviso.setupUi(self.aviso_window)

        # Mostrar la ventana de aviso
        self.aviso_window.show()
    
    def editar_horario(self):
        # Verificar si alguno de los campos de texto está vacío
        if not self.lineEdit.text() or not self.lineEdit_2.text():
            # Mostrar la ventana de error si alguno de los campos está vacío
            self.mostrar_ventana_error()
            return
        
        try:
            edicion = cargar_desde_txt("edicion.txt")
        except:
            pass
        # Obtener los valores ingresados por el usuario
        nuevo_horario2 = int(self.lineEdit.text())
        nuevo_horario1 = int(self.lineEdit_2.text())
        # Obtener la materia seleccionada para editar
        materia_editar = edicion[2]

        # Obtener el día y salón seleccionados
        dia = edicion[0]
        salon = edicion[1]
        if 9 <= nuevo_horario1 <= 15 and 11 <= nuevo_horario2 <= 17:
            data = cargar_desde_txt('horarios.txt')
            for clase in data.get(salon, {}).get(dia, []):
                if clase['Clase'] == materia_editar:
                    if len(clase['Horario']) <= 1:
                        clase['Horario'] = [[nuevo_horario1, nuevo_horario2]]
                        break
                    else:
                        clase['Horario'] = [[nuevo_horario1, nuevo_horario1 + 2], [nuevo_horario2, nuevo_horario2 + 2]]

            with open('horarios.txt', 'w') as file:
                json.dump(data, file, indent=4)

            # Abrir aviso de horario editado solo si la edición es exitosa
            self.abrir_aviso()

    def mostrar_ventana_error(self):
        # Crear y mostrar la ventana de error
        self.ventana_error = QtWidgets.QDialog()
        self.ui_error = Ui_error()
        self.ui_error.setupUi(self.ventana_error)
        self.ventana_error.show()

    def retranslateUi(self, EditarHorario):
        _translate = QtCore.QCoreApplication.translate
        EditarHorario.setWindowTitle(_translate("EditarHorario", "Editar Horario"))
        self.label_3.setText(_translate("EditarHorario", "Ingrese el Horario de inicio"))
        self.label_4.setText(_translate("EditarHorario", "Ingrese el Horario de fin"))
        self.pushButton.setText(_translate("EditarHorario", "Confirmar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditarHorario = QtWidgets.QWidget()
    ui = Ui_EditarHorario()
    ui.setupUi(EditarHorario)
    EditarHorario.show()
    sys.exit(app.exec_())
