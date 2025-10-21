import tkinter as tk

def cambiar_texto():
    etiqueta3.config(text="Borrando system32...     Borrado")

root = tk.Tk()
root.title("Ejercicio 1")

etiqueta1 = tk.Label(root, text="Buenos días ciudadano")
etiqueta1.pack()

etiqueta2 = tk.Label(root, text="Jorge Álvarez Canosa")
etiqueta2.pack()

etiqueta3 = tk.Label(root, text="Texto original")
etiqueta3.pack()

boton = tk.Button(root, text="Cambiar texto", command=cambiar_texto)
boton.pack()

root.mainloop()