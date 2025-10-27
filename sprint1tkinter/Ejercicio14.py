import tkinter as tk
class RegistroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicio14")

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.scale_edad = tk.Scale(self.root, from_=0, to=100, orient="horizontal")
        self.scale_edad.pack()

        self.var_genero = tk.StringVar(value="Otro")

        tk.Radiobutton(self.root, text="Masculino", variable=self.var_genero, value="Masculino").pack()
        tk.Radiobutton(self.root, text="Femenino", variable=self.var_genero, value="Femenino").pack()
        tk.Radiobutton(self.root, text="Otro", variable=self.var_genero, value="Otro").pack()

        self.boton_add = tk.Button(self.root, text="Añadir", command=self.add_usuario)
        self.boton_add.pack()

        self.boton_eliminar = tk.Button(self.root, text="Eliminar", command=self.eliminar_usuario)
        self.boton_eliminar.pack()

        self.frame_lista = tk.Frame(self.root)
        self.frame_lista.pack(expand=True, fill="both")

        self.scrollbar = tk.Scrollbar(self.frame_lista)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(self.frame_lista, yscrollcommand=self.scrollbar.set)
        self.listbox.pack()

        self.scrollbar.config(command=self.listbox.yview)

        self.boton_salir = tk.Button(self.root, text="Salir", command=self.salir)
        self.boton_salir.pack()

    def add_usuario(self):
            nombre = self.entry.get()
            edad = self.scale_edad.get()
            genero = self.var_genero.get()

            usuario_info = f"Nombre: {nombre}, \nEdad: {edad}, \nGenero: {genero}"
            self.listbox.insert(tk.END, usuario_info)

    def eliminar_usuario(self):
            indices = self.listbox.curselection()
            if indices:
                self.listbox.delete(indices[0])

    def salir(self):
            self.root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = RegistroApp(root)
    root.mainloop()