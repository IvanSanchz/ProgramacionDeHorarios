from PyQt5 import QtCore, QtGui, QtWidgets

from menu_principal import Ui_MenuPrincipal


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 240)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("* {\n"
            "    color: #000;\n"
            "}\n"
            "\n"
            "QWidget {\n"
            "    background-image: url(principal.jpg);\n"  # Cambia "background.jpg" al nombre de tu imagen
            "    background-repeat: no-repeat;\n"
            "    background-position: center;\n"
            "    border-radius: 12px;\n"
        "}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.background)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.app_name = QtWidgets.QLabel(self.background)
        font = QtGui.QFont()
        font.setFamily("Gumbo")
        font.setPointSize(36)
        self.app_name.setFont(font)
        self.app_name.setAlignment(QtCore.Qt.AlignCenter)
        self.app_name.setObjectName("app_name")
        self.verticalLayout_2.addWidget(self.app_name)
        self.app_description = QtWidgets.QLabel(self.background)
        font = QtGui.QFont()
        font.setFamily("Gumbo")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.app_description.setFont(font)
        self.app_description.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.app_description.setObjectName("app_description")
        self.verticalLayout_2.addWidget(self.app_description)
        self.progress = QtWidgets.QFrame(self.background)
        self.progress.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.progress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.progress.setObjectName("progress")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.progress)
        self.verticalLayout_3.setContentsMargins(30, -1, 30, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.percentage = QtWidgets.QLabel(self.progress)
        font = QtGui.QFont()
        font.setFamily("Nunito Sans Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.percentage.setFont(font)
        self.percentage.setAlignment(QtCore.Qt.AlignCenter)
        self.percentage.setObjectName("percentage")
        self.verticalLayout_3.addWidget(self.percentage)
        self.progressBar = QtWidgets.QProgressBar(self.progress)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 10))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 15))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    background: rgba(255, 255, 255, 180);\n"
"    border-style: none;\n"
"    border-radius: 5px;\n"
"    color: rgba(200, 200, 200, 0);\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 241, 255, 255), stop:1 rgba(26, 65, 187, 255))\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.verticalLayout_2.addWidget(self.progress)
        self.footer = QtWidgets.QFrame(self.background)
        self.footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.footer)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.status = QtWidgets.QLabel(self.footer)
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(10)
        self.status.setFont(font)
        self.status.setObjectName("status")
        self.horizontalLayout_2.addWidget(self.status)
        self.author = QtWidgets.QLabel(self.footer)
        font = QtGui.QFont()
        font.setFamily("Nunito Sans Black")
        font.setPointSize(10)
        self.author.setFont(font)
        self.author.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.author.setObjectName("author")
        self.horizontalLayout_2.addWidget(self.author)
        self.verticalLayout_2.addWidget(self.footer)
        self.verticalLayout.addWidget(self.background)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupProgressBar(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateProgressBar)
        self.timer.start(5)  # Actualiza cada 5 milisegundos
        self.progressValue = 0

    def updateProgressBar(self):
        increment = 100 / (5000 / 5)  # Ajuste para una animación fluida en 5 segundos
        self.progressValue += increment
        self.progressBar.setValue(int(self.progressValue))
        self.percentage.setText(f"{int(self.progressValue)}%")

        if self.progressValue < 100:
            self.status.setText("Inicializando programa...")
        else:
            self.timer.stop()  # Detiene el temporizador una vez que la barra esté completa
            self.status.setText("Programa inicializado")
            self.progressBar.setValue(100)  # Asegura que la barra esté completamente llena
            self.openMenuPrincipal()  # Abre la ventana del menú principal

    def openMenuPrincipal(self):
        # Cierra la ventana actual
        MainWindow.close()

        # Abre la nueva ventana
        self.menuWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MenuPrincipal()
        self.ui.setupUi(self.menuWindow)
        self.menuWindow.show()
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.app_name.setText(_translate("MainWindow", "Generador"))
        self.app_description.setText(_translate("MainWindow", "De Horarios"))
        self.percentage.setText(_translate("MainWindow", "24%"))
        self.status.setText(_translate("MainWindow", "status"))
        self.author.setText(_translate("MainWindow", "Autores: Los BichoLovers"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    # Configurar las banderas de la ventana para eliminar el marco
    MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    # Configurar los atributos de la ventana para habilitar la transparencia
    MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.setupProgressBar()  # Configura la barra de progreso

    # Aplicar una hoja de estilo para bordes redondeados
    MainWindow.setStyleSheet("QMainWindow {border-radius: 15px;}")

    MainWindow.show()
    sys.exit(app.exec_())
