from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_horarios_generados(object):
    def setupUi(self, horarios_generados):
        horarios_generados.setObjectName("horarios_generados")
        horarios_generados.resize(200, 105)
        self.label = QtWidgets.QLabel(horarios_generados)
        self.label.setGeometry(QtCore.QRect(10, 30, 181, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(horarios_generados)
        self.pushButton.setGeometry(QtCore.QRect(60, 60, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(horarios_generados.close)

        self.retranslateUi(horarios_generados)
        QtCore.QMetaObject.connectSlotsByName(horarios_generados)

    def retranslateUi(self, horarios_generados):
        _translate = QtCore.QCoreApplication.translate
        horarios_generados.setWindowTitle(_translate("horarios_generados", "Horarios Generados"))
        self.label.setText(_translate("horarios_generados", "Horarios GENERADOS con éxito!"))
        self.pushButton.setText(_translate("horarios_generados", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    horarios_generados = QtWidgets.QDialog()
    ui = Ui_horarios_generados()
    ui.setupUi(horarios_generados)
    horarios_generados.show()
    sys.exit(app.exec_())
