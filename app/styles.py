def label_config(label):
    label.setStyleSheet("""
    QLabel{
                    font-size: 24px;      
                    font-family: Helvetica;
        }
                        """)
    label.setFixedSize(280, 50)


def entry_config(entry):
    entry.setStyleSheet("""
    QLineEdit {
                    font-size: 22px;    
                    font-family: Helvetica;
                    border-radius: 5px;
                    border: 2px Inset #A6C9A5;
                    background-color: white;
        }
                        """)
    entry.setFixedSize(280, 45)


def button_config(button):
    button.setStyleSheet("""
        QPushButton{
                    font-size: 22px;
                    font-family: Helvetica;
                    background-color: #fff2cc;
                    border: 2px Outset #A6C9A5;
                    border-radius: 10px;
        }
        QPushButton:hover {
                    background-color: #FBDC83;
        }
        QPushButton:pressed {
                    background-color: #A18B4D;
                    border-style: Inset
        }           
                        """)
    button.setFixedSize(280, 50)


def combobox_config(combobox):
    combobox.setStyleSheet("""
        QComboBox{
                    font-size: 19px;
                    font-family: Helvetica;
                    background-color: #DFCCFF;
                    border: 2px Inset #C0A5C9;
                    border-radius: 8px;
        }
        QComboBox::down-arrow{
                    image: url(C:/Users/agust/Desktop/DotaSYS - PySide/resources/images/combobox_arrow.png);
        }
                        """)

    combobox.setFixedSize(280, 50)


def main_button_config(button):
    button.setStyleSheet("""
        QPushButton{
                    font-size: 18px;
                    font-family: Helvetica;
                    background-color: #fff2cc;
                    border: 2px Outset #A6C9A5;
                    border-radius: 10px;
        }
        QPushButton:hover {
                    background-color: #FBDC83;
        }
        QPushButton:pressed {
                    background-color: #A18B4D;
                    border-style: Inset
        }           
                        """)
    button.setFixedSize(180, 50)


def main_window_config(label, combobox):
    label.setStyleSheet("""
        QLabel{
                    font-size: 18px;    
                    font-family: Helvetica;
                    color: white;
                    border-radius: 5px;
                    border: 2px Inset #487A46;
                    background-color: #458543;
        }
                        """)

    combobox.setStyleSheet("""
        QComboBox{
                    font-size: 18px;
                    font-family: Helvetica;
                    background-color: #DFCCFF;
                    border: 2px Inset #C0A5C9;
                    border-radius: 8px;
        }                    
                        """)

    label.setFixedSize(240, 50)
    combobox.setFixedSize(240, 50)


def main_table_config(table, header):
    table.setStyleSheet("""
        QTableWidget{
                    background-color: white;
                    font-size: 18px;
                    font-family: Helvetica
                    
        }
        QScrollBar:Vertical{
                    background: transparent;
                    width: 20px;
                    background-color: lightgray;
                    
        }
    """)
    header.setStyleSheet("""
        QHeaderView::section {
                    background-color: #647687;
                    color: white;
                    font-size: 20px;
                    font-family: Helvetica
        }
    """)
    table.setFixedSize(960, 605)
    header.setDefaultSectionSize(229)


def reload_button_config(button):
    button.setStyleSheet("""
        QPushButton{
                    background-color: white;
                    border: 2px Outset #C0A5C9;
                    border-radius: 8px;
        }
        QPushButton:hover{
                    background-color: #A96BBE
        }
        QPushButton:pressed{
                    background-color: #54335F;
                    border-style: Inset
        }
    """)

    button.setFixedSize(30, 30)
