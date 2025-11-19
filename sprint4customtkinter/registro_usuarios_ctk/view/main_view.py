from pathlib import Path
import tkinter
import customtkinter as ctk

class AddUserView:
    def __init__(self, master):
        self.window = ctk.CTkToplevel(master)
        self.window.title("Añadir Nuevo Usuario")
        self.window.geometry("350x600")
        self.window.grab_set()  # La vuelve modal

        # Base dir para rutas de avatares
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.ASSETS_PATH = self.BASE_DIR / "assets"

        # ----------- Widgets -----------
        ctk.CTkLabel(self.window, text="Nombre:").pack(pady=5)
        self.nombre_entry = ctk.CTkEntry(self.window, width=200)
        self.nombre_entry.pack(pady=5)

        ctk.CTkLabel(self.window, text="Edad:").pack(pady=5)
        self.edad_entry = ctk.CTkEntry(self.window, width=200)
        self.edad_entry.pack(pady=5)

        ctk.CTkLabel(self.window, text="Género:").pack(pady=(10, 5))
        self.genero_var = ctk.StringVar(value="Otro")
        
        for genero in ["Masculino", "Femenino", "Otro"]:
            ctk.CTkRadioButton(
                self.window,
                text=genero,
                variable=self.genero_var,
                value=genero
            ).pack(anchor="w", padx=20, pady=2)

        ctk.CTkLabel(self.window, text="Avatar:").pack(pady=(10, 5))
        self.avatar_var = ctk.StringVar(value="avatar1")
        
        for i in range(1, 4):
            ctk.CTkRadioButton(
                self.window,
                text=f"Avatar {i}",
                variable=self.avatar_var,
                value=f"avatar{i}"
            ).pack(anchor="w", padx=20, pady=2)

        self.guardar_button = ctk.CTkButton(
            self.window,
            text="Guardar"
        )
        self.guardar_button.pack(pady=20)

    def get_data(self):
        avatar_seleccionado = self.avatar_var.get()
        avatar_path = str(self.ASSETS_PATH / f"{avatar_seleccionado}.png")
        
        return {
            "nombre": self.nombre_entry.get(),
            "edad": self.edad_entry.get(),
            "genero": self.genero_var.get(),
            "avatar": avatar_path
        }

class EditUserView:
    def __init__(self, master, usuario):
        self.window = ctk.CTkToplevel(master)
        self.window.title("Editar Usuario")
        self.window.geometry("350x600")
        self.window.grab_set()

        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.ASSETS_PATH = self.BASE_DIR / "assets"
        self.usuario = usuario

        # ----------- Widgets -----------
        ctk.CTkLabel(self.window, text="Nombre:").pack(pady=5)
        self.nombre_entry = ctk.CTkEntry(self.window, width=200)
        self.nombre_entry.pack(pady=5)
        self.nombre_entry.insert(0, usuario.nombre)

        ctk.CTkLabel(self.window, text="Edad:").pack(pady=5)
        self.edad_entry = ctk.CTkEntry(self.window, width=200)
        self.edad_entry.pack(pady=5)
        self.edad_entry.insert(0, str(usuario.edad))

        ctk.CTkLabel(self.window, text="Género:").pack(pady=(10, 5))
        self.genero_var = ctk.StringVar(value=usuario.genero)
        
        for genero in ["Masculino", "Femenino", "Otro"]:
            ctk.CTkRadioButton(
                self.window,
                text=genero,
                variable=self.genero_var,
                value=genero
            ).pack(anchor="w", padx=20, pady=2)

        ctk.CTkLabel(self.window, text="Avatar:").pack(pady=(10, 5))
        avatar_actual = Path(usuario.avatar).stem
        self.avatar_var = ctk.StringVar(value=avatar_actual)
        
        for i in range(1, 4):
            ctk.CTkRadioButton(
                self.window,
                text=f"Avatar {i}",
                variable=self.avatar_var,
                value=f"avatar{i}"
            ).pack(anchor="w", padx=20, pady=2)

        # Botones
        buttons_frame = ctk.CTkFrame(self.window)
        buttons_frame.pack(pady=20)

        self.guardar_button = ctk.CTkButton(
            buttons_frame,
            text="Guardar"
        )
        self.guardar_button.pack(side="left", padx=5)

        self.cancelar_button = ctk.CTkButton(
            buttons_frame,
            text="Cancelar",
            command=self.window.destroy
        )
        self.cancelar_button.pack(side="left", padx=5)

    def get_data(self):
        avatar_seleccionado = self.avatar_var.get()
        avatar_path = str(self.ASSETS_PATH / f"{avatar_seleccionado}.png")
        
        return {
            "nombre": self.nombre_entry.get(),
            "edad": self.edad_entry.get(),
            "genero": self.genero_var.get(),
            "avatar": avatar_path
        }

class MainView:
    def __init__(self, master: ctk.CTk):
        self.master = master

        #Barra de Menú
        self.menubar = tkinter.Menu(master)
        master.config(menu=self.menubar)
        
        self.menu_archivo = tkinter.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Archivo", menu=self.menu_archivo)

        master.grid_rowconfigure(1, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=3)

        #Panel superior
        self.top_frame = ctk.CTkFrame(master)
        self.top_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

        ctk.CTkLabel(self.top_frame, text="Buscar:").pack(side="left", padx=5)
        self.busqueda_var = ctk.StringVar()
        self.busqueda_entry = ctk.CTkEntry(
            self.top_frame,
            textvariable=self.busqueda_var,
            width=200
        )
        self.busqueda_entry.pack(side="left", padx=5)

        ctk.CTkLabel(self.top_frame, text="Género:").pack(side="left", padx=5)
        self.genero_filtro_var = ctk.StringVar(value="Todos")
        self.genero_filtro_menu = ctk.CTkComboBox(
            self.top_frame,
            values=["Todos", "Masculino", "Femenino", "Otro"],
            variable=self.genero_filtro_var,
            state="readonly",
            width=150
        )
        self.genero_filtro_menu.pack(side="left", padx=5)

        #Panel izquierdo
        self.left_frame = ctk.CTkFrame(master)
        self.left_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.title_usuarios = ctk.CTkLabel(
            self.left_frame,
            text="Usuarios",
            font=("Arial", 22, "bold")
        )
        self.title_usuarios.pack(pady=(5, 10))

        self.lista_frame = ctk.CTkScrollableFrame(self.left_frame)
        self.lista_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.label_usuarios = ctk.CTkLabel(self.lista_frame)

        #Panel derecho
        self.detalles_frame = ctk.CTkFrame(master)
        self.detalles_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

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

        # Barra de estado
        self.status_frame = ctk.CTkFrame(master)
        self.status_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=5)

        self.status_label = ctk.CTkLabel(
            self.status_frame,
            text="Listos",
            anchor="center",
            text_color="gray"
        )
        self.status_label.pack(side="left", fill="x", expand=True)

        #Panel inferior
        self.botones_frame = ctk.CTkFrame(master)
        self.botones_frame.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

        self.btn_add_user = ctk.CTkButton(
            self.botones_frame,
            text="Añadir usuario"
        )
        self.btn_add_user.pack(side="left", padx=5, pady=10)

        self.btn_autosave = ctk.CTkButton(
            self.botones_frame,
            text="Auto-guardado(10s): OFF",
            fg_color="gray"
        )
        self.btn_autosave.pack(side="left", padx=5, pady=10)

        # Botón Salir a la derecha
        self.btn_exit = ctk.CTkButton(
            self.botones_frame,
            text="Salir"
        )
        self.btn_exit.pack(side="right", padx=5, pady=10)

    def actualizar_lista_usuarios(self, usuarios, on_seleccionar_callback, on_doble_clic_callback=None):
        for widget in self.lista_frame.winfo_children():
            widget.destroy()

        for i, usuario in enumerate(usuarios):
            btn = ctk.CTkButton(
                self.lista_frame,
                text=usuario.nombre,
                command=lambda idx=i: on_seleccionar_callback(idx)
            )
            btn.pack(fill="x", pady=4)
            
            if on_doble_clic_callback:
                btn.bind("<Double-Button-1>", lambda event, idx=i: on_doble_clic_callback(idx))

    def mostrar_detalles_usuario(self, usuario):
        self.label_nombre.configure(text=f"Nombre: {usuario.nombre}")
        self.label_edad.configure(text=f"Edad: {usuario.edad}")
        self.label_genero.configure(text=f"Género: {usuario.genero}")

    def bind_add_user_button(self, callback):
        self.btn_add_user.configure(command=callback)

    def bind_autosave_button(self, callback):
        self.btn_autosave.configure(command=callback)

    def bind_exit_button(self, callback):
        self.btn_exit.configure(command=callback)

    def actualizar_boton_autosave(self, activo: bool):
        if activo:
            self.btn_autosave.configure(text="Auto-guardado: ON", fg_color="green")
        else:
            self.btn_autosave.configure(text="Auto-guardado: OFF", fg_color="gray")

    def actualizar_status(self, mensaje: str, color: str = "gray"):
        self.status_label.configure(text=mensaje, text_color=color)

        