import csv


class Usuario:
    def __init__(self, nombre: str, edad: int, genero: str, avatar: str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar #"../assets/avatar1.png"  # ruta relativa en assets/

class GestorUsuarios:
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