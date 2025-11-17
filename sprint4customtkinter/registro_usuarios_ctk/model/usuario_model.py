import csv
#from PIL import Image
import customtkinter as ctk
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ruta_avatar1 = BASE_DIR / "assets" / "avatar1.png"

app = ctk.CTk()

#avatar1 = ctk.CTkImage(
#    light_image=Image.open(ruta_avatar1),
#    dark_image=Image.open(ruta_avatar1),
#    size=(120, 120)
#)

class Usuario:
    def __init__(self, nombre: str, edad: int, genero: str, avatar: str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar #"../assets/avatar1.png"  # ruta relativa en assets/

class UsuariosModel:
    def __init__(self):
        self._usuarios = []  # lista de Usuario

    def listar(self):
        return list(self._usuarios)

    def añadir(self, usuario: Usuario):
        # validaciones mínimas (nombre no vacío, edad en rango, genero permitido)
        self._usuarios.append(usuario)

    def eliminar(self, indice: int):
        # controlar índices fuera de rango
        ...

    def actualizar(self, indice: int, usuario_actualizado: Usuario):
        ...

    def guardar_csv(self, ruta: str = "usuarios.csv"):
        with open('usuarios.csv', 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            escritor.writerows(["nombre", "edad", "genero", "avatar"])

    def cargar_csv(self, ruta: str = "usuarios.csv"):
        with open('usuarios.csv', 'r', encoding='utf-8') as f:
            lector = csv.reader(f)
            for fila in lector:
                print(fila)

app.mainloop()