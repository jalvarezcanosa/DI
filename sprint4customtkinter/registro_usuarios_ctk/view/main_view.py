import customtkinter as ctk
import tkinter as tk

from registro_usuarios_ctk.app import app


class MainView:
    def __init__(self, master: ctk.CTk):
        self.master = master

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=3)

        #Panel izquierdo
        self.lista_frame = ctk.CTkScrollableFrame(master)
        self.lista_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        #Panel derecho
        self.detalles_frame = ctk.CTkFrame(master)
        self.detalles_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

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


app.mainloop()
