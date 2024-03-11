# ### Funciones de utilidad para el proyecto ### #
# importing files
# importing modules
import ctypes

import bcrypt
import sqlalchemy
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMessageBox
from sqlalchemy import func

from app.models import *
from app.gui.main_window import *

id_ventana = 'company.product.subproduct.version'  # task bar icon


# Configurations -------------------------------------------------------------------------------------------------------
def root_config(root_window):
    root_window.setWindowTitle("DotaSYS")
    root_window.setWindowIcon(QIcon('C:/Users/agust/Desktop/DotaSYS - PySide/resources/icons/logo.ico'))
    root_window.setStyleSheet("background-color: #d5e8d4;")
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(id_ventana)


def clear_entries(*args):
    for a in args:
        a.clear()


def open_window(old_window, new_window):
    old_window.close()
    new_window.show()


def open_toplevel_window(new_window, title):
    new_window.setWindowTitle(title)
    new_window.show()


# Validation functions -------------------------------------------------------------------------------------------------
def error_msg(message):
    errbox = QMessageBox()
    errbox.setIcon(QMessageBox.Icon.Critical)
    errbox.setText(message)
    errbox.setWindowTitle("Error")
    errbox.setStandardButtons(QMessageBox.StandardButton.Ok)
    errbox.exec()


def info_msg(message):
    msgbox = QMessageBox()
    msgbox.setIcon(QMessageBox.Icon.Information)
    msgbox.setText(message)
    msgbox.setWindowTitle("Info.")
    msgbox.setStandardButtons(QMessageBox.StandardButton.Ok)
    msgbox.exec()


# checkeo si la contraseña es correcta
def verify_passw(user_entry, user_text, password_entry, password_text, old_window, new_window):
    bytes_password = password_text.encode('utf-8')

    # verifica si los usuarios y sus contraseñas están bien
    if verification_DB(Employee, user_text, bytes_password, "empleado", "employee_username"):
        open_window(old_window, new_window)  # Cerrar ventana login y abrir main_window

    elif verification_DB(Manager, user_text, bytes_password, "gerente", "manager_username"):
        open_window(old_window, new_window)  # Cerrar ventana login y abrir main_window

    else:
        error_msg("El usuario o la contraseña son incorrectos, intentalo de nuevo.")
        clear_entries(user_entry, password_entry)


def validate_register(stock, barcode, name, brand):
    if stock.text() != "" or barcode.text() != "":  # comprueba si es entero
        try:
            int(stock.text())
            int(barcode.text())

        except ValueError:
            error_msg("Por favor introduce un valor correcto en el stock o código de barras")

    # ------------------------------------------------------------------------------------------------------------------
    # Si hay algun valor vacío entonces muestra el error
    if stock.text() == "" or barcode.text() == "" or name.text() == "" or brand.text() == "":
        error_msg("Por favor introduce los valores faltantes")

    # ------------------------------------------------------------------------------------------------------------------
    # Entra si estan todos los valores ingresados
    elif stock.text() != "" and barcode.text() != "" and name.text() != "" and brand.text() != "":
        new_session.close()
        try:
            add_product(barcode.text(), name.text(), brand.text(), stock.text())

        # comprobación para ver si ya existe el código de barras
        except sqlalchemy.exc.IntegrityError:
            error_msg("Ya existe este código de barras, intente nuevamente.")

        except sqlalchemy.exc.PendingRollbackError:
            error_msg("Ha ocurrido un error al insertar los datos en la base de datos.")

            # muestro una ventana con los valores ingresados
        else:
            new_session.close()
            info_msg("""Ha sido registrado exitosamente el repuesto:\n
                    Código de barras: {}\n
                    Nombre del repuesto: {}\n
                    Marca del repuesto: {}\n
                    Stock del repuesto: {}
                    """.format(barcode.text(), name.text(), brand.text(), stock.text()))
            clear_entries(barcode, name, brand, stock)


# Other functions ------------------------------------------------------------------------------------------------------

def add_to_table(table, horiz_labl):
    rows = new_session.query(Product).all()  # Hago un query para que me devuelva los datos de las filas
    cont_rows = 0

    # Reinicio
    # table.setRowCount(0)

    # Seteo la tabla
    table.setColumnCount(4)
    table.setHorizontalHeaderLabels(horiz_labl)
    table.setRowCount(len(rows))

    # Recorro las filas de la base de datos
    for row in rows:
        row_to_str = str(row)  # Transformo la fila en un str
        splitted_row = row_to_str.split(",")  # La separo en cada uno de los valores y la paso a una lista

        for column in range(0, 4):
            # Le defino los valores a introducir en la tabla
            table.setItem(cont_rows, column, QTableWidgetItem(splitted_row[column]))
        # cuento las filas

        cont_rows += 1


# DB functions ---------------------------------------------------------------------------------------------------------
def commit_to_database(var):
    new_session.add(var)
    new_session.commit()
    new_session.close()


# Encripto la contraseña para mayor seguridad
def encrypt_password(password):
    password = password.encode('utf-8')  # Transforms to bytes the hashed password
    salt = bcrypt.gensalt()  # genera el salt
    hashed_password = bcrypt.hashpw(password, salt)  # hashes the password to protect it
    return hashed_password


# verifica que la contraseña sea la correcta y devuelve un valor bool
def verification_DB(db_table, entered_user, entered_pass, comparable_value, type_username):
    # se conecta a la base de datos y trae al usuario específico buscado
    user = new_session.query(db_table).filter(getattr(db_table, type_username) == entered_user).first()

    return (entered_user == "%s" % comparable_value and user
            and bcrypt.checkpw(entered_pass, user.password.encode('utf-8')))


def add_employee(user_entry, password_entry):  # Añado un usuario con la contraseña encriptada
    new_employee = Employee(employee_username=user_entry, password=encrypt_password(password_entry))
    commit_to_database(new_employee)


def add_manager(user_entry, password_entry):
    new_manager = Manager(manager_username=user_entry, password=encrypt_password(password_entry))
    commit_to_database(new_manager)


def add_product(barcode, name, brand, total_stock):
    new_product = Product(product_barcode=barcode, product_name=name, employee_ID=1, product_brand=brand,
                          stock=total_stock)
    commit_to_database(new_product)


def add_supplier(name, address, contact):
    new_supplier = Supplier(supplier_name=name, address=address, contact=contact)
    commit_to_database(new_supplier)


def add_purchase_order(date, amount, total_price):
    new_purchase_order = PurchaseOrder(order_date=date, amount=amount, total_price=total_price)
    commit_to_database(new_purchase_order)


def sum_in_DB():  # TODO cambiar esto por otra cosa que se me ocurra
    return new_session.query(func.sum(Product.stock)).scalar()  # .scalar() sirve para que devuelva solo 1 resultado


def add_default_users():
    add_employee("empleado", "1234")
    add_manager("gerente", "Agussuper34")
