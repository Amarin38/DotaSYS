# importing modules
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton, QWidget
from PySide6.QtGui import QShortcut, QKeySequence

# importing files
import app.utils as utils
import app.styles as styles


class ReplacementPartEditWindow(QWidget):
    def __init__(self):
        super().__init__()

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
        self.apply_changes_button = QPushButton("Guardar cambios", self)
        self.exit_button = QPushButton("Salir", self)

        # Shortcuts ----------------------------------------------------------------------------------------------------
        self.return_to_edit = QShortcut(QKeySequence("Return"), self)
        self.esc_to_exit = QShortcut(QKeySequence("Escape"), self)

        # Connections
        self.return_to_edit.activated.connect(lambda: utils.validate_register(self.stock_entry, self.barcode_entry,
                                                                              self.name_entry, self.brand_entry))
        self.apply_changes_button.clicked.connect(lambda: utils.validate_register(self.stock_entry, self.barcode_entry,
                                                                                  self.name_entry, self.brand_entry))

        self.esc_to_exit.activated.connect(lambda: self.close())
        self.exit_button.clicked.connect(lambda: self.close())

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
        self.brand_entry.move(30, 165)  # 280x50
        self.stock_entry.move(340, 165)  # 280x50

        self.apply_changes_button.move(30, 230)  # 280x50
        self.exit_button.move(340, 230)  # 280x50

        # Labels config. -----------------------------------------------------------------------------------------------
        styles.label_config(self.barcode_label)
        styles.label_config(self.name_label)
        styles.label_config(self.brand_label)
        styles.label_config(self.stock_label)

        # Buttons config. ----------------------------------------------------------------------------------------------
        styles.entry_config(self.barcode_entry)
        styles.entry_config(self.name_entry)
        styles.entry_config(self.brand_entry)
        styles.entry_config(self.stock_entry)

        # Entries config. ----------------------------------------------------------------------------------------------
        styles.button_config(self.apply_changes_button)
        styles.button_config(self.exit_button)

        # TODO asignarle los valores del recuadro seleccionado
        # Seteo los valores ingresados ya en el registro
        self.barcode_entry.setText("{}".format(1214415))
        self.name_entry.setText("{}".format("Joystick"))
        self.brand_entry.setText("{}".format("Sony"))
        self.stock_entry.setText("{}".format(70))
