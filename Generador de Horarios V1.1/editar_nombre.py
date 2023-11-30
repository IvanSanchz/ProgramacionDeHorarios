from PyQt5 import QtCore, QtGui, QtWidgets
import os
import json

from aviso_nombre_editado import Ui_nombre_editado
from error_01 import Ui_error

def cargar_desde_txt(nombre_archivo):
    ruta_archivo = os.path.join(os.getcwd(), nombre_archivo)
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo:
            data = json.load(archivo)
            return data

class Ui_EditarNombre(object):
    def setupUi(self, EditarNombre):
        EditarNombre.setObjectName("EditarNombre")
        EditarNombre.resize(301, 111)
        self.pushButton = QtWidgets.QPushButton(EditarNombre)
        self.pushButton.setGeometry(QtCore.QRect(110, 70, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(EditarNombre)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 261, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(EditarNombre)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 261, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")

        # Conectar el botón "Confirmar" con la función para editar el nombre
        self.pushButton.clicked.connect(self.editar_nombre)

        self.retranslateUi(EditarNombre)
        QtCore.QMetaObject.connectSlotsByName(EditarNombre)

    def editar_nombre(self):
        nuevo_nombre = str(self.lineEdit.text()).strip()

        # Verificar si el campo de texto está vacío
        if not nuevo_nombre:
            # Mostrar la ventana de error si el campo está vacío
            self.mostrar_ventana_error()
            return

        try:
            edicion = cargar_desde_txt("edicion.txt")
        except:
            pass
        # Obtener los valores ingresados por el usuario
        nuevo_nombre = str(self.lineEdit.text())
        print(nuevo_nombre)
        # Obtener la materia seleccionada para editar
        materia_editar = edicion[2]

        # Obtener el día y salón seleccionados
        dia = edicion[0]
        salon = edicion[1]
        data = cargar_desde_txt('horarios.txt')

        for clase in data.get(salon, {}).get(dia, []):
            if clase['Clase'] == materia_editar:
                clase['Clase'] = nuevo_nombre

        with open('horarios.txt', 'w') as file:
            json.dump(data, file, indent=4)

        # Abrir aviso de nombre editado solo si el cambio es exitoso
            self.abrir_aviso()
    
    def mostrar_ventana_error(self):
        # Crear y mostrar la ventana de error
        self.ventana_error = QtWidgets.QDialog()
        self.ui_error = Ui_error()
        self.ui_error.setupUi(self.ventana_error)
        self.ventana_error.show()

    def abrir_aviso(self):
        self.aviso_window = QtWidgets.QDialog()
        self.ui_aviso = Ui_nombre_editado()
        self.ui_aviso.setupUi(self.aviso_window)
        self.aviso_window.show()

    def retranslateUi(self, EditarNombre):
        _translate = QtCore.QCoreApplication.translate
        EditarNombre.setWindowTitle(_translate("EditarNombre", "Editar Nombre"))
        self.pushButton.setText(_translate("EditarNombre", "Confirmar"))
        self.label_4.setText(_translate("EditarNombre", "Ingrese el nuevo nombre de la materia"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditarNombre = QtWidgets.QWidget()
    ui = Ui_EditarNombre()
    ui.setupUi(EditarNombre)
    EditarNombre.show()
    sys.exit(app.exec_())
