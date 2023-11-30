from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from anadir_profesor import Ui_AnadirProfesor
from consultar_horario import Ui_ConsultarHorario
from editar_materias import Ui_EditarMaterias
from generar_horarios import Ui_GenerarHorario
from ayuda import Ui_MainWindow 

import os
import json

def hay_horarios_disponibles():
    ruta_archivo = os.path.join(os.getcwd(), 'horarios.txt')
    return os.path.exists(ruta_archivo)

class Ui_MenuPrincipal(object):

    def openAyuda(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openAnadirProfesor(self):
        if hay_horarios_disponibles():    
            self.window = QtWidgets.QWidget()
            self.ui = Ui_AnadirProfesor()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            QMessageBox.warning(None, "Advertencia", "No hay horarios disponibles. Por favor, genera los horarios primero.")

    def openConsultarHorario(self):
        if hay_horarios_disponibles():
            self.window = QtWidgets.QWidget()
            self.ui = Ui_ConsultarHorario()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            QMessageBox.warning(None, "Advertencia", "No hay horarios disponibles. Por favor, genera los horarios primero.")

    def openEditarMaterias(self):
        if hay_horarios_disponibles():
            self.window = QtWidgets.QWidget()
            self.ui = Ui_EditarMaterias()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            QMessageBox.warning(None, "Advertencia", "No hay horarios disponibles. Por favor, genera los horarios primero.")

    def openGenerarHorario(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_GenerarHorario()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MenuPrincipal):
        MenuPrincipal.setObjectName("MenuPrincipal")
        MenuPrincipal.resize(805, 442)

        # Cargar la imagen de fondo
        fondo = QtGui.QPixmap("principal.jpg")  # Asegúrate de cambiar esto por la ruta real de tu imagen
        fondo = fondo.scaled(MenuPrincipal.size(), QtCore.Qt.IgnoreAspectRatio)  # Escala la imagen para que se ajuste al tamaño de la ventana

        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(fondo))
        MenuPrincipal.setPalette(palette)

        MenuPrincipal.setObjectName("MenuPrincipal")
        MenuPrincipal.resize(805, 442)
        
        self.centralwidget = QtWidgets.QWidget(MenuPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 60, 361, 151))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setFamily("Nunito Sans")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openGenerarHorario) # Abrir ventana Generar Horarios
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 60, 361, 151))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setFamily("Nunito Sans")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openConsultarHorario) # Abrir ventana Consultar Horario
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 220, 361, 151))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setFamily("Nunito Sans")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.openAnadirProfesor) # Abrir ventana Añadir Profesor
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 220, 361, 151))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setFamily("Nunito Sans")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.openEditarMaterias) # Abrir ventana Editar Materias
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 15, 221, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setFamily("Gumbo")
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MenuPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MenuPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 21))
        self.menubar.setObjectName("menubar")

        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")

        # Crear una acción para la opción Ayuda
        self.actionAyuda = QtWidgets.QAction(MenuPrincipal)
        self.actionAyuda.setObjectName("actionAyuda")
        self.actionAyuda.setText("Manual de Usuario")
        
        # Conectar la acción Ayuda a la función openAyuda
        self.actionAyuda.triggered.connect(self.openAyuda)

        # Agregar la acción al menú Ayuda
        self.menuAyuda.addAction(self.actionAyuda)
        
        # Agregar el menú Ayuda a la barra de menús
        self.menubar.addAction(self.menuAyuda.menuAction())

        MenuPrincipal.setMenuBar(self.menubar)

        self.retranslateUi(MenuPrincipal)
        QtCore.QMetaObject.connectSlotsByName(MenuPrincipal)

    def retranslateUi(self, MenuPrincipal):
        _translate = QtCore.QCoreApplication.translate
        MenuPrincipal.setWindowTitle(_translate("MenuPrincipal", "Menú Principal"))
        self.pushButton.setText(_translate("MenuPrincipal", "Generar Horarios"))
        self.pushButton_2.setText(_translate("MenuPrincipal", "Consultar Horario"))
        self.pushButton_3.setText(_translate("MenuPrincipal", "Añadir Profesor"))
        self.pushButton_4.setText(_translate("MenuPrincipal", "Editar Materias"))
        self.label_2.setText(_translate("MenuPrincipal", "Menú Principal"))
        self.menuAyuda.setTitle(_translate("MenuPrincipal", "Ayuda"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuPrincipal = QtWidgets.QMainWindow()
    ui = Ui_MenuPrincipal()
    ui.setupUi(MenuPrincipal)
    MenuPrincipal.show()
    sys.exit(app.exec_())
