from registro_usuarios_ctk.model.usuario_model import UsuariosModel
from registro_usuarios_ctk.view.main_view import MainView

class AppController:
    def __init__(self, root):
        self.root = root()
        self.view = MainView(root)
        self.model = UsuariosModel()