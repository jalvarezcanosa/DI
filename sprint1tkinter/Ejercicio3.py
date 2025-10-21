import tkinter as tk

def saludar():
    nombre = entrada.get()
    etiqueta.config(text=f"Bienvenido, {nombre}")

root = tk.Tk()
root.title("Ejercicio3")

entrada = tk.Entry(root)
etiqueta = tk.Label(root, text="")
boton = tk.Button(root, text="Saludo personalizado", command=saludar)

entrada.pack()
etiqueta.pack()
boton.pack()

root.mainloop()
