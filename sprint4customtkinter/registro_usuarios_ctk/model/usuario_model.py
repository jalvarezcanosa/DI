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

class GestorUsuarios:
    def __init__(self):
        self._usuarios = []
        self._cargar_datos_de_ejemplo()


    def _cargar_datos_de_ejemplo(self):
        self._usuarios.append(Usuario("Ana García", 28, "F", "avatar1.png"))
        self._usuarios.append(Usuario("Luis Pérez", 35, "M", "avatar2.png"))
        self._usuarios.append(Usuario("Sofía Romero", 35, "F", "avatar3.png"))


    def listar(self):
        return list(self._usuarios)


    def obtener(self, indice):
        return self._usuarios[indice]