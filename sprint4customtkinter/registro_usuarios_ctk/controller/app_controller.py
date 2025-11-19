from pathlib import Path
from tkinter import messagebox

from PIL import Image, ImageTk

from model.usuario_model import GestorUsuarios, Usuario
from view.main_view import MainView, AddUserView

class AppController:
    def __init__(self, master):
        self.master = master

        self.modelo = GestorUsuarios()
        self.view = MainView(master)

        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.ASSETS_PATH = self.BASE_DIR / "assets"

        self.avatar_images = {}

        self.view.bind_add_user_button(self.abrir_ventana_añadir)

        self.refrescar_lista_usuarios()

    def abrir_ventana_añadir(self):
        add_view = AddUserView(self.master)

        add_view.guardar_button.configure(
            command=lambda: self.añadir_usuario(add_view)
        )



    def refrescar_lista_usuarios(self):
        usuarios = self.modelo.listar()
        self.view.actualizar_lista_usuarios(
            usuarios,
            self.seleccionar_usuario
        )

    def seleccionar_usuario(self, indice):
        usuario = self.modelo.obtener(indice)
        self.view.mostrar_detalles_usuario(usuario)

        if usuario.avatar:
            img = Image.open(usuario.avatar)
            img = img.resize((150, 150))

            tk_img = ImageTk.PhotoImage(img)

            # guardar referencia para que no desaparezca
            self.avatar_images[usuario.nombre] = tk_img

            self.view.avatar_label.configure(image=tk_img)
        else:
            self.view.avatar_label.configure(image="")

    def añadir_usuario(self, add_view: AddUserView):
        datos = add_view.get_data()

        # Validación básica
        if datos["nombre"].strip() == "":
            messagebox.showerror("Error", "El nombre no puede estar vacío.")
            return

        try:
            edad = int(datos["edad"])
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número.")
            return

        # Crear usuario
        nuevo = Usuario(
            nombre=datos["nombre"],
            edad=edad,
            genero=datos["genero"],
            avatar=datos["avatar"]
        )

        self.modelo.añadir(nuevo)
        self.refrescar_lista_usuarios()

        add_view.window.destroy()