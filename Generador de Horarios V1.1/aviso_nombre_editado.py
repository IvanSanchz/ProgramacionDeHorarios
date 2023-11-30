from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_nombre_editado(object):
    def setupUi(self, nombre_editado):
        nombre_editado.setObjectName("nombre_editado")
        nombre_editado.resize(200, 105)
        self.label = QtWidgets.QLabel(nombre_editado)
        self.label.setGeometry(QtCore.QRect(10, 30, 181, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(nombre_editado)
        self.pushButton.setGeometry(QtCore.QRect(60, 60, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(nombre_editado.close)

        self.retranslateUi(nombre_editado)
        QtCore.QMetaObject.connectSlotsByName(nombre_editado)

    def retranslateUi(self, nombre_editado):
        _translate = QtCore.QCoreApplication.translate
        nombre_editado.setWindowTitle(_translate("nombre_editado", "Nombre Editado"))
        self.label.setText(_translate("nombre_editado", "Nombre EDITADO con éxito!"))
        self.pushButton.setText(_translate("nombre_editado", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    nombre_editado = QtWidgets.QDialog()
    ui = Ui_nombre_editado()
    ui.setupUi(nombre_editado)
    nombre_editado.show()
    sys.exit(app.exec_())
