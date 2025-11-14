import customtkinter as ctk

class MainView:
    def __init__(self, master):
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.label = ctk.CTkLabel(self.frame, text="Panel de previsualización")
        self.label.pack(pady=10)

        self.nombre_label = ctk.CTkLabel(self.frame, text="Nombre:")
        self.nombre_label.pack(pady=10)
        self.nombre_entry = ctk.CTkEntry(self, width=250)
        self.nombre_entry.pack()

        self.edad_label = ctk.CTkLabel(self, text="Edad:")
        self.edad_label.pack(pady = 10)
        self.edad_entry = ctk.CTkEntry(self, width=250)
        self.edad_entry.pack()

        self.btn_add = ctk.CTkButton(self.frame, text="Añadir")
        self.btn_add.pack(pady=5)

        self.btn_eliminar = ctk.CTkButton(self.frame, text="Eliminar")
        self.btn_eliminar.pack(pady=5)

        self.btn_editar = ctk.CTkButton(self.frame, text="Editar")
        self.btn_editar.pack(pady=5)

        self.btn_salir = ctk.CTkButton(self.frame, text="Salir")
        self.btn_salir.pack(pady=5)

        self.avatar_label = ctk.CTkLabel(self, text="Avatar:")
        self.avatar_label.pack(pady=(10, 0))
        self.avatar_var = ctk.StringVar(value=self._avatares[0])

        self.lista_usuarios = ctk.CTkTextbox(self.frame, width=300)
        self.lista_usuarios.pack(pady=10, fill="x")

