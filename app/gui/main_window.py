# importing modules
from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QLabel, QPushButton, QWidget, QComboBox, QTableWidget, QTableWidgetItem

# importing files
import app.utils as utils
import app.styles as styles


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.my_signal = Signal()
        filter_list = ["Repuestos faltantes", "Ultimos repuestos ingresados", "Nombre: A-Z", "Nombre: Z-A",
                       "Marca: A-Z", "Marca: Z-A", "Stock menor-mayor", "Stock mayor-menor"]

        self.horizontal_labels_list = ["Código de barras", "Nombre", "Marca", "Stock"]

        # Buttons ------------------------------------------------------------------------------------------------------
        self.register_product_button = QPushButton("Registrar repuesto", self)
        self.edit_product_button = QPushButton("Editar", self)
        self.update_table_button = QPushButton(self)
        self.update_table_button.setIcon(
            QIcon("C:/Users/agust/Desktop/DotaSYS - PySide/resources/icons/reload_icon.png"))

        # ComboBox -----------------------------------------------------------------------------------------------------
        self.filter_combobox = QComboBox(self)
        self.filter_combobox.setPlaceholderText("---- Filtro ----")
        self.filter_combobox.addItems(filter_list)
        # TODO hacer a los filtros funcionales

        # Labels -------------------------------------------------------------------------------------------------------
        self.total_label = QLabel(f"Total: {utils.sum_in_DB()}", self)

        # Table --------------------------------------------------------------------------------------------------------
        self.main_table = QTableWidget(self)

        # Table header -------------------------------------------------------------------------------------------------
        self.hheader = self.main_table.horizontalHeader()

        # Table widget -------------------------------------------------------------------------------------------------
        self.new_widget = QTableWidgetItem()

        # TODO Crear una barra de búsqueda que esté conectada con la tabla y
        #  que esta se modifique para mostrar lo necesario.
        self.init_ui()

    def init_ui(self):
        # Position Config. ---------------------------------------------------------------------------------------------
        utils.root_config(self)
        self.setFixedSize(980, 700)

        self.filter_combobox.move(40, 20)

        self.register_product_button.move(300, 20)
        self.edit_product_button.move(500, 20)
        self.update_table_button.move(5, 30)

        self.total_label.move(700, 20)

        self.main_table.move(10, 80)

        # Widgets styling ----------------------------------------------------------------------------------------------
        styles.main_window_config(self.total_label, self.filter_combobox)

        styles.main_button_config(self.register_product_button)
        styles.main_button_config(self.edit_product_button)

        styles.reload_button_config(self.update_table_button)

        # Table config. ------------------------------------------------------------------------------------------------
        styles.main_table_config(self.main_table, self.hheader)  # Table styles

        utils.add_to_table(self.main_table, self.horizontal_labels_list)
        self.update_table_button.clicked.connect(
            lambda: utils.add_to_table(self.main_table, self.horizontal_labels_list))

        # TODO arreglar el problema de auto-actualización de la tabla
