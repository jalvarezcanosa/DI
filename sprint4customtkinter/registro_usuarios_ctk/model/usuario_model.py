import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "usuarios.csv"

class Usuario:
    def __init__(self, nombre: str, edad: int, genero: str, avatar: str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar

class GestorUsuarios:
    def __init__(self):
        self._usuarios = []
        self._cargar_datos_de_ejemplo()

    def _cargar_datos_de_ejemplo(self):
        self._usuarios.append(Usuario("Ana García", 28, "F", str(BASE_DIR / "assets/avatar1.png")))
        self._usuarios.append(Usuario("Luis Pérez", 35, "M", str(BASE_DIR / "assets/avatar2.png")))
        self._usuarios.append(Usuario("Sofía Romero", 35, "F", str(BASE_DIR / "assets/avatar3.png")))

    def listar(self):
        return list(self._usuarios)

    def obtener(self, indice):
        return self._usuarios[indice]

    def añadir(self, usuario):
        self._usuarios.append(usuario)

    def guardar_csv(self):
        """Guarda la lista de usuarios en un archivo CSV."""
        try:
            with open(CSV_PATH, 'w', newline='', encoding='utf-8') as archivo:
                writer = csv.writer(archivo)
                writer.writerow(["Nombre", "Edad", "Género", "Avatar"])
                for usuario in self._usuarios:
                    writer.writerow([usuario.nombre, usuario.edad, usuario.genero, usuario.avatar])
        except Exception as e:
            print(f"Error al guardar CSV: {e}")

    def cargar_csv(self):
        """Carga la lista de usuarios desde un archivo CSV."""
        try:
            with open(CSV_PATH, 'r', encoding='utf-8') as archivo:
                lector = csv.reader(archivo)
                next(lector)
                self._usuarios.clear()
                for fila in lector:
                    try:
                        if len(fila) == 4:
                            nombre, edad, genero, avatar = fila
                            usuario = Usuario(nombre, int(edad), genero, avatar)
                            self._usuarios.append(usuario)
                    except (ValueError, IndexError) as e:
                        print(f"Error al procesar fila: {fila} - {e}")
                        continue
        except FileNotFoundError:
            print(f"Archivo {CSV_PATH} no encontrado. Usando datos de ejemplo.")
        except Exception as e:
            print(f"Error al cargar CSV: {e}")
