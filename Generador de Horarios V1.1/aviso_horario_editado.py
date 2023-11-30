from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_horario_editado(object):
    def setupUi(self, horario_editado):
        self.horario_editado = horario_editado
        horario_editado.setObjectName("horario_editado")
        horario_editado.resize(200, 105)
        self.label = QtWidgets.QLabel(horario_editado)
        self.label.setGeometry(QtCore.QRect(10, 30, 181, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(horario_editado)
        self.pushButton.setGeometry(QtCore.QRect(60, 60, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("OK")

        # Conectar el botón "OK" directamente con el método close de la ventana
        self.pushButton.clicked.connect(horario_editado.close)

        self.retranslateUi(horario_editado)
        QtCore.QMetaObject.connectSlotsByName(horario_editado)

    def retranslateUi(self, horario_editado):
        _translate = QtCore.QCoreApplication.translate
        horario_editado.setWindowTitle(_translate("horario_editado", "Horario Editado"))
        self.label.setText(_translate("horario_editado", "Horario EDITADO con éxito!"))
        self.pushButton.setText(_translate("horario_editado", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    horario_editado = QtWidgets.QDialog()
    ui = Ui_horario_editado()
    ui.setupUi(horario_editado)
    horario_editado.show()
    sys.exit(app.exec_())
