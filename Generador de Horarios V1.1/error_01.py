from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt  # Importa Qt


class Ui_error(object):
    def setupUi(self, error):
        # Configura las banderas de la ventana para quitar el botón de ayuda
        error.setWindowFlags(error.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        
        error.setObjectName("error")
        error.resize(200, 105)
        self.label = QtWidgets.QLabel(error)
        self.label.setGeometry(QtCore.QRect(10, 30, 181, 16))
        font = QtGui.QFont()
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(error)
        self.pushButton.setGeometry(QtCore.QRect(60, 60, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(error)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 181, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.pushButton.clicked.connect(error.close)

        self.retranslateUi(error)
        QtCore.QMetaObject.connectSlotsByName(error)

    def retranslateUi(self, error):
        _translate = QtCore.QCoreApplication.translate
        error.setWindowTitle(_translate("error", "ERROR // Opción Válida"))
        self.label.setText(_translate("error", "Seleccione una opción válida"))
        self.pushButton.setText(_translate("error", "OK"))
        self.label_2.setText(_translate("error", "ERROR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    error = QtWidgets.QDialog()
    ui = Ui_error()
    ui.setupUi(error)
    error.show()
    sys.exit(app.exec_())
