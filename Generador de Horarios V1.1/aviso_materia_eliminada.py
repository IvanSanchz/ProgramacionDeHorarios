from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_materia_eliminada(object):
    def setupUi(self, materia_eliminada):
        materia_eliminada.setObjectName("materia_eliminada")
        materia_eliminada.resize(200, 105)
        self.pushButton = QtWidgets.QPushButton(materia_eliminada)
        self.pushButton.setGeometry(QtCore.QRect(54, 60, 81, 23))
        self.pushButton.setObjectName("pushButton")

        # Conectar el botón "OK" con la función de cerrar la ventana
        self.pushButton.clicked.connect(materia_eliminada.close)
        
        self.label = QtWidgets.QLabel(materia_eliminada)
        self.label.setGeometry(QtCore.QRect(10, 30, 181, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(materia_eliminada)
        QtCore.QMetaObject.connectSlotsByName(materia_eliminada)

    def retranslateUi(self, materia_eliminada):
        _translate = QtCore.QCoreApplication.translate
        materia_eliminada.setWindowTitle(_translate("materia_eliminada", "Materia Eliminada"))
        self.pushButton.setText(_translate("materia_eliminada", "OK"))
        self.label.setText(_translate("materia_eliminada", "La Materia fue ELIMINADA con éxito!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    materia_eliminada = QtWidgets.QDialog()
    ui = Ui_materia_eliminada()
    ui.setupUi(materia_eliminada)
    materia_eliminada.show()
    sys.exit(app.exec_())
