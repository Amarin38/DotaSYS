# importing modules
from PySide6.QtWidgets import QLineEdit, QCheckBox, QLabel, QWidget, QPushButton

# importing files
import app.utils as utils
import app.styles as styles


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Labels -------------------------------------------------------------------------------------------------------
        self.user_title = QLabel("Usuario", self)
        self.passwrd_title = QLabel("Contraseña", self)

        # Button -------------------------------------------------------------------------------------------------------
        self.login_button = QPushButton("Iniciar sesión", self)

        # Entries ------------------------------------------------------------------------------------------------------
        self.user_entry = QLineEdit("", self)
        self.passwrd_entry = QLineEdit("", self)
        self.passwrd_entry.setEchoMode(QLineEdit.EchoMode.Password)  # Defino * como caracteres base

        # Checkbuttons -------------------------------------------------------------------------------------------------
        self.pass_value_checkbtn = QCheckBox("Mostrar contraseña", self)
        self.pass_value_checkbtn.stateChanged.connect(self.show_hide_passw)  # Comprueba el cambio de estado

        self.init_ui()

    def init_ui(self):
        # Position Config. ---------------------------------------------------------------------------------------------
        utils.root_config(self)
        self.setFixedSize(535, 285)

        self.user_entry.move(120, 63)  # 280x50

        self.passwrd_title.move(201, 110)  # 280x50
        self.passwrd_entry.move(120, 160)  # 280x50

        self.user_title.move(220, 15)  # 280x50
        self.pass_value_checkbtn.move(405, 172)

        self.login_button.move(100, 220)  # 320x50

        # Labels config. -----------------------------------------------------------------------------------------------
        styles.label_config(self.user_title)
        styles.label_config(self.passwrd_title)

        # Entries config. ----------------------------------------------------------------------------------------------
        styles.entry_config(self.user_entry)
        styles.entry_config(self.passwrd_entry)

        # Button config. -----------------------------------------------------------------------------------------------
        styles.button_config(self.login_button)
        self.login_button.setFixedSize(320, 50)

    def show_hide_passw(self):  # Para mostrar u ocultar la contraseña
        if self.pass_value_checkbtn.isChecked():
            self.passwrd_entry.setEchoMode(QLineEdit.EchoMode.Normal)  # Defino el texto real como caracteres base

        else:
            self.passwrd_entry.setEchoMode(QLineEdit.EchoMode.Password)  # Defino * como caracteres base
