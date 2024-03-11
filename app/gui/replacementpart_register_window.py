# importing modules
from PySide6.QtCore import QEvent
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton, QWidget
from PySide6.QtGui import QShortcut, QKeySequence

# importing files
import app.utils as utils
import app.styles as styles
from app.gui.main_window import MainWindow


class ReplacementPartRegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.main_window = MainWindow()

        # Labels -------------------------------------------------------------------------------------------------------
        self.barcode_label = QLabel("Código de barras", self)
        self.name_label = QLabel("Nombre del repuesto", self)
        self.brand_label = QLabel("Marca del repuesto", self)
        self.stock_label = QLabel("Stock", self)

        # Entries ------------------------------------------------------------------------------------------------------
        self.barcode_entry = QLineEdit("", self)
        self.name_entry = QLineEdit("", self)
        self.brand_entry = QLineEdit("", self)
        self.stock_entry = QLineEdit("", self)

        # Buttons ------------------------------------------------------------------------------------------------------
        self.register_button = QPushButton("Registrar", self)
        self.read_barcode_button = QPushButton("Leer código de barras", self)

        # Shortcuts ----------------------------------------------------------------------------------------------------
        self.return_to_register = QShortcut(QKeySequence("Return"), self)

        # Connections --------------------------------------------------------------------------------------------------
        self.return_to_register.activated.connect(lambda: utils.validate_register(self.stock_entry, self.barcode_entry,
                                                                                  self.name_entry, self.brand_entry))

        self.register_button.clicked.connect(lambda: utils.validate_register(self.stock_entry, self.barcode_entry,
                                                                             self.name_entry, self.brand_entry))

        # TODO hacer el "leer código de barras"
        # TODO hacer que al seleccionar un recuadro y tocar editar modifique esos datos en la base de datos
        self.init_ui()

    def init_ui(self):
        # Position Config. ---------------------------------------------------------------------------------------------
        utils.root_config(self)
        self.setFixedSize(650, 300)

        self.barcode_label.move(33, 12)  # 280x50
        self.name_label.move(340, 12)  # 280x50
        self.brand_label.move(30, 117)  # 280x50
        self.stock_label.move(340, 117)  # 280x50

        self.barcode_entry.move(30, 60)  # 280x50
        self.name_entry.move(340, 60)  # 280x50
        self.stock_entry.move(340, 165)  # 280x50
        self.brand_entry.move(30, 165)  # 280x50

        self.register_button.move(30, 230)  # 280x50
        self.read_barcode_button.move(340, 230)  # 280x50

        # Labels config. -----------------------------------------------------------------------------------------------
        styles.label_config(self.barcode_label)
        styles.label_config(self.name_label)
        styles.label_config(self.brand_label)
        styles.label_config(self.stock_label)

        # Entries config. ----------------------------------------------------------------------------------------------
        styles.entry_config(self.barcode_entry)
        styles.entry_config(self.name_entry)
        styles.entry_config(self.brand_entry)
        styles.entry_config(self.stock_entry)

        # Buttons config. ----------------------------------------------------------------------------------------------
        styles.button_config(self.register_button)
        styles.button_config(self.read_barcode_button)
