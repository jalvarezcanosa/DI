import customtkinter as ctk
from registro_usuarios_ctk.controller.app_controller import AppController
from registro_usuarios_ctk.view.main_view import MainView

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Registro de Usuarios (CTk + MVC)")
    app.geometry("900x600")

    main_view = MainView(app)
    app.mainloop()