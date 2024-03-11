# archivo que ejecuta el programa
import sys

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QShortcut, QKeySequence, QCloseEvent

import app.utils as utils
from app.gui.login_window import LoginWindow
from app.gui.main_window import MainWindow
from app.gui.replacementpart_register_window import ReplacementPartRegisterWindow
from app.gui.replacementpart_edit_window import ReplacementPartEditWindow


# Uso una clase para llamar a todas las otras clases y abrirlas cuando las necesito
class OpenWindows:
    def __init__(self):
        self.login_window = LoginWindow()
        self.main_window = MainWindow()
        self.register_window = ReplacementPartRegisterWindow()
        self.edit_window = ReplacementPartEditWindow()

        self.return_to_login = QShortcut(QKeySequence("Return"), self.login_window)

        self.login_window.init_ui()
        self.main_window.init_ui()
        self.register_window.init_ui()
        self.edit_window.init_ui()

        # Button connections -------------------------------------------------------------------------------------------

        # Cuando se clickea el botón que se ejecute la verificación y se abra la ventana Main
        self.login_window.login_button.clicked.connect(
            lambda: utils.verify_passw(self.login_window.user_entry, self.login_window.user_entry.text(),
                                       self.login_window.passwrd_entry, self.login_window.passwrd_entry.text(),
                                       self.login_window, self.main_window))
        # Shortcut
        self.return_to_login.activated.connect(
            lambda: utils.verify_passw(self.login_window.user_entry, self.login_window.user_entry.text(),
                                       self.login_window.passwrd_entry, self.login_window.passwrd_entry.text(),
                                       self.login_window, self.main_window))

        # Cuando se clickea el botón que se abra el toplevel de registro
        self.main_window.register_product_button.clicked.connect(
            lambda: utils.open_toplevel_window(self.register_window, "DotaSYS - Registrar"))

        # Cuando se clickea el botón que se abra el toplevel de edición
        self.main_window.edit_product_button.clicked.connect(
            lambda: utils.open_toplevel_window(self.edit_window, "DotaSYS - Editar"))


if __name__ == '__main__':
    app = QApplication([])
    main = OpenWindows()
    main.login_window.show()

    sys.exit(app.exec())
    # TODO deployear app despues
