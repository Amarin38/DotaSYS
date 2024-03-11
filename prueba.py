from PySide6 import QtCore, QtWidgets
import sys

from PySide6.QtGui import QPixmap, QAction

from app import styles


class Prueba(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout(self)

        self.label = QtWidgets.QLabel("Prueba")
        self.image = QtWidgets.QLabel()
        self.entry = QtWidgets.QLineEdit("")
        self.checkbox = QtWidgets.QCheckBox("Checkbox")
        self.checkbox2 = QtWidgets.QCheckBox("Checkbox 2")
        self.checkbox3 = QtWidgets.QCheckBox("Checkbox 3")
        self.button_group = QtWidgets.QButtonGroup(self)
        self.boton = QtWidgets.QPushButton("Push")
        self.boton.clicked.connect(lambda: print("apretado"))
        self.menu = QtWidgets.QMenu()
        self.nuevo_menu = QtWidgets.QMenu()

        self.init_ui()

    def init_ui(self):
        self.image.setPixmap(QPixmap("/resources/icons/logo.ico"))
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.image)
        self.layout.addWidget(self.entry)

        self.layout.addWidget(self.checkbox)
        self.layout.addWidget(self.checkbox2)
        self.layout.addWidget(self.checkbox3)

        self.layout.addWidget(self.boton)

        self.layout.addWidget(self.nuevo_menu)

        self.layout.setAlignment(self.label, styles.align_center())
        self.layout.setAlignment(self.label, styles.align_center())
        self.layout.setAlignment(self.entry, styles.align_center())
        self.layout.setAlignment(self.checkbox, styles.align_center())
        self.layout.setAlignment(self.checkbox2, styles.align_center())
        self.layout.setAlignment(self.checkbox3, styles.align_center())
        self.layout.setAlignment(self.boton, styles.align_center())
        self.layout.setAlignment(self.nuevo_menu, styles.align_center())

        self.button_group.addButton(self.checkbox)
        self.button_group.addButton(self.checkbox2)
        self.button_group.addButton(self.checkbox3)
        self.boton.setDefault(True)

        accion1 = QAction("Hola", self)
        accion2 = QAction("Que tal", self)
        accion3 = QAction("Adios", self)

        accion1.triggered.connect(self.hola)
        accion2.triggered.connect(self.quetal)
        accion3.triggered.connect(self.adios)

        self.menu.addAction(accion1)
        self.menu.addAction(accion2)
        self.menu.addAction(accion3)

        self.boton.setMenu(self.menu)

        self.nuevo_menu.addAction(accion1)
        self.nuevo_menu.addAction(accion2)
        self.nuevo_menu.addAction(accion3)
        self.nuevo_menu.addMenu(self.menu)
        self.nuevo_menu.showTearOffMenu()

        self.image.setScaledContents(True)

    def hola(self):
        print("hola")

    def quetal(self):
        print("que tal")

    def adios(self):
        print("adios")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    prueba = Prueba()
    prueba.show()

    sys.exit(app.exec())
