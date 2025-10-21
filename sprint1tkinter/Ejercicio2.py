import tkinter as tk

def mostrar_mensaje():
    etiqueta.config(text="QUE PUNTERÍA")

root = tk.Tk()
root.title("Ejercicio 2")

etiqueta = tk.Label(root, text="")

boton_mostrar = tk.Button(root, text="Botón Mostar", command=mostrar_mensaje)

boton_cerrar = tk.Button(root, text="Salir", command=root.quit)

etiqueta.pack()
boton_mostrar.pack()
boton_cerrar.pack()

root.mainloop()