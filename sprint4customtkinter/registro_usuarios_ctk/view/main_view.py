import customtkinter as ctk
import tkinter as tk

from registro_usuarios_ctk.app import app


class MainView:
    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.title("Registro de Usuarios")
        self.master.geometry("900x600")

        self.menubar = tk.Menu(self.master)

        self.file_menu = tk.Menu(self.menubar)
        self.file_menu.add_command(label="Guardar")
        self.file_menu.add_command(label="Cargar")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir")
        self.menubar.add_cascade(label="Archivo", menu=self.file_menu)

        self.help_menu = tk.Menu(self.menubar, tearoff=0)
        self.help_menu.add_command(label="Acerca de")
        self.menubar.add_cascade(label="Ayuda", menu=self.help_menu)

        self.master.config(menu=self.menubar)

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=2)
        self.master.grid_rowconfigure(1, weight=1)

        # ---------------- TOP FRAME ----------------------#
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        ctk.CTkLabel(self.top_frame, text="Buscar").pack(side="left", padx=10, pady=10)
        self.search_entry = ctk.CTkEntry(self.top_frame)
        self.search_entry.pack(side="left", padx=5, pady=10)

        ctk.CTkLabel(self.top_frame, text="Género").pack(side="left", padx=10, pady=10)
        self.gender_filter_var = ctk.StringVar(value="Todos")
        self.gender_filter_menu = ctk.CTkOptionMenu(self.top_frame, values=["Todos", "masculino", "femenino", "otro"],variable=self.gender_filter_var)
        self.gender_filter_menu.pack(side="left", padx=5, pady=10)

        self.delete_button = ctk.CTkButton(self.top_frame, text="Eliminar", width=80, fg_color="#D32F2F")
        self.delete_button.pack(side="right", padx=5, pady=10)

        self.add_button = ctk.CTkButton(self.top_frame, text="Añadir", width=80)
        self.add_button.pack(side="right", padx=(20, 5), pady=10)

        #---------------- LEFT FRAME ----------------------#
        self.left_frame = ctk.CTkFrame(self.master)
        self.left_frame.grid(row=1, column=0, padx=(10, 5), pady=10)
        self.left_frame.grid_rowconfigure(0, weight=1)
        self.left_frame.grid_columnconfigure(0, weight=1)

        self.user_list_frame = ctk.CTkScrollableFrame(self.left_frame, label_text="Usuarios")
        self.user_list_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.user_widgets = []

        # ---------------- RIGHT FRAME ----------------------#
        self.right_frame = ctk.CTkFrame(self.master)
        self.right_frame.grid(row=1, column=1, padx=(5, 10), pady=10)
        self.right_frame.grid_columnconfigure(0, weight=1)

        self.avatar_var = ctk.StringVar(value=self._avatares[0])

        self.nombre_label = ctk.CTkLabel(self.right_frame, text="Nombre: ")
        self.nombre_label.pack(pady=10)

        self.edad_label = ctk.CTkLabel(self.right_frame, text="Edad: ")
        self.edad_label.pack(pady = 10)

        self.genero_label = ctk.CTkLabel(self.right_frame, text="Género: ")
        self.genero_label.pack(pady = 10)

app.mainloop()
