# Loading GUI
from PySide6.QtWidgets import QWidget


class LoadingTopLevel(QWidget):
    def __init__(self):
        super().__init__()

        # Labels -------------------------------------------------------------------------------------------------------

        # GIF ----------------------------------------------------------------------------------------------------------
        gif_path = "/Users/agust/Desktop/DotaSYS/resources/icons/loading_logo.gif"  # localizacion del gif
        self.frames = 12  # frames del gif

        # Lista todas las imágenes del gif y especifica que cada indice va a ser una imagen
        # self.loading_gif_list = [tk.PhotoImage(file=gif_path, format="gif -index %i" % i) for i in range(self.frames)]
        # self.gif_label = tk.Label(self, pady=5, bg="#d5e8d4")
        self.init_gui()

    def init_gui(self):
        # TopLevel config. ---------------------------------------------------------------------------------------------

        # Widget config. -----------------------------------------------------------------------------------------------
        pass

    # TODO arreglar problema al ejecutarse esto
    """def update_gif(self, index=0):
        # comprueba si existe la ventana
        if self.winfo_exists():
            frame = self.loading_gif_list[index]  # creo una variable para pasar un frame singular
            index += 1

            if index == self.frames:
                index = 0

            self.gif_label.config(image=frame)  # añado el frame al label
            self.after(60, self.update_gif, index)  # despues de ese tiempo reinicia la funcion"""
