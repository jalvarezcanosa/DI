import tkinter as tk
from tkinter import messagebox

def add_usuario():
    nombre = entry.get()
    edad = scale_edad.get()
    genero = genero.get()

    usuario_info = f"Nombre: {nombre}, \nEdad: {edad}, \nGenero: {genero}"
    listbox.insert(tk.END, usuario_info)

def eliminar_usuario():
    selected = listbox.curselection()
    selected.delete()

root = tk.Tk()
root.title("Ejercicio12")

entry = tk.Entry(root)
entry.pack()

scale_edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
scale_edad.pack()


tk.Radiobutton(root, text="Masculino").pack()
tk.Radiobutton(root, text="Femenino").pack()
tk.Radiobutton(root, text="Otro").pack()

boton_add = tk.Button(root, text="Añadir")
boton_add.pack()

boton_eliminar = tk.Button(root, text="Eliminar")
boton_eliminar.pack()

listbox = tk.Listbox(root)
listbox.pack()

boton_salir = tk.Button(root, text="Salir")

barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

menu = tk.Menu(barra_menu)
barra_menu.add_cascade(label="Salir", menu=menu)
menu.add_command(label="Salir", command=root.quit)

root.mainloop()