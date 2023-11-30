from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_profesor_anadido(object):
    def setupUi(self, profesor_anadido):
        profesor_anadido.setObjectName("profesor_anadido")
        profesor_anadido.resize(200, 105)
        self.label = QtWidgets.QLabel(profesor_anadido)
        self.label.setGeometry(QtCore.QRect(10, 30, 181, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(profesor_anadido)
        self.pushButton.setGeometry(QtCore.QRect(60, 60, 81, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(profesor_anadido.close)

        self.retranslateUi(profesor_anadido)
        QtCore.QMetaObject.connectSlotsByName(profesor_anadido)

    def retranslateUi(self, profesor_anadido):
        _translate = QtCore.QCoreApplication.translate
        profesor_anadido.setWindowTitle(_translate("profesor_anadido", "Profesor Añadido"))
        self.label.setText(_translate("profesor_anadido", "El Profesor fue AÑADIDO con éxito!"))
        self.pushButton.setText(_translate("profesor_anadido", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    profesor_anadido = QtWidgets.QDialog()
    ui = Ui_profesor_anadido()
    ui.setupUi(profesor_anadido)
    profesor_anadido.show()
    sys.exit(app.exec_())
