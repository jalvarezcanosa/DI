from tkinter import filedialog

import customtkinter as ctk

class AddUserView:
    def __init__(self, master):
        self.window = ctk.CTkToplevel(master)
        self.window.title("Añadir Nuevo Usuario")
        self.window.geometry("300x400")
        self.window.grab_set()  # La vuelve modal

        # ----------- Widgets -----------
        ctk.CTkLabel(self.window, text="Nombre:").pack(pady=5)
        self.nombre_entry = ctk.CTkEntry(self.window, width=200)
        self.nombre_entry.pack(pady=5)

        ctk.CTkLabel(self.window, text="Edad:").pack(pady=5)
        self.edad_entry = ctk.CTkEntry(self.window, width=200)
        self.edad_entry.pack(pady=5)

        ctk.CTkLabel(self.window, text="Avatar:").pack(pady=5)
        self.avatar_path = None
        self.avatar_button = ctk.CTkButton(
            self.window,
            text="Seleccionar Imagen",
            command=self.seleccionar_avatar
        )
        self.avatar_button.pack(pady=5)

        self.guardar_button = ctk.CTkButton(
            self.window,
            text="Guardar"
        )
        self.guardar_button.pack(pady=20)

    def get_data(self):
        return {
            "nombre": self.nombre_entry.get(),
            "edad": self.edad_entry.get(),
            "avatar": self.avatar_path
        }

    def seleccionar_avatar(self):
        path = filedialog.askopenfilename(
            filetypes=[("avatar", "*.png")]
        )
        if path:
            self.avatar_path = path
            self.avatar_button.configure(text="Imagen seleccionada")

class MainView:
    def __init__(self, master: ctk.CTk):
        self.master = master

        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=3)

        #Panel izquierdo
        self.left_frame = ctk.CTkFrame(master)
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.title_usuarios = ctk.CTkLabel(
            self.left_frame,
            text="Usuarios",
            font=("Arial", 22, "bold")
        )
        self.title_usuarios.pack(pady=(5, 10))

        self.lista_frame = ctk.CTkScrollableFrame(self.left_frame)
        self.lista_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.label_usuarios = ctk.CTkLabel(self.lista_frame)

        self.btn_add_user = ctk.CTkButton(
            self.left_frame,
            text="Añadir usuario"
        )
        self.btn_add_user.pack(pady=10)

        #Panel derecho
        self.detalles_frame = ctk.CTkFrame(master)
        self.detalles_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.title_detalles = ctk.CTkLabel(
            self.detalles_frame,
            text="Detalles del usuario",
            font=("Arial", 22, "bold")
        )
        self.title_detalles.pack()

        self.avatar_label = ctk.CTkLabel(self.detalles_frame, text="")
        self.avatar_label.pack(pady=10)

        self.label_nombre = ctk.CTkLabel(self.detalles_frame, text="Nombre: ")
        self.label_nombre.pack(anchor="w", pady=5)

        self.label_edad = ctk.CTkLabel(self.detalles_frame, text="Edad: ")
        self.label_edad.pack(anchor="w", pady=5)

        self.label_genero = ctk.CTkLabel(self.detalles_frame, text="Género: ")
        self.label_genero.pack(anchor="w", pady=5)

    def actualizar_lista_usuarios(self, usuarios, on_seleccionar_callback):
        for widget in self.lista_frame.winfo_children():
            widget.destroy()

            for i, usuario in enumerate(usuarios):
                btn = ctk.CTkButton(
                    self.lista_frame,
                    text=usuario.nombre,
                    command=lambda idx=i: on_seleccionar_callback(idx)
                )
                btn.pack(fill="x", pady=4)

    def mostrar_detalles_usuario(self, usuario):
        self.label_nombre.configure(text=f"Nombre: {usuario.nombre}")
        self.label_edad.configure(text=f"Edad: {usuario.edad}")
        self.label_genero.configure(text=f"Género: {usuario.genero}")

    def bind_add_user_button(self, callback):
        self.btn_add_user.configure(command=callback)