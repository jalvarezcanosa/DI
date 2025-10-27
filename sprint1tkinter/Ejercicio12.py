import tkinter as tk
from tkinter import messagebox

def add_usuario():
    nombre = entry.get()
    edad = scale_edad.get()
    genero = var_genero.get()

    usuario_info = f"Nombre: {nombre}, \nEdad: {edad}, \nGenero: {genero}"
    listbox.insert(tk.END, usuario_info)

def eliminar_usuario():
    indices = listbox.curselection()
    if indices:
        listbox.delete(indices[0])

root = tk.Tk()
root.title("Ejercicio12")

entry = tk.Entry(root)
entry.pack()

scale_edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
scale_edad.pack()

var_genero = tk.StringVar(value="Otro")

tk.Radiobutton(root, text="Masculino", variable=var_genero, value="Masculino").pack()
tk.Radiobutton(root, text="Femenino", variable=var_genero, value="Femenino").pack()
tk.Radiobutton(root, text="Otro", variable=var_genero, value="Otro").pack()

boton_add = tk.Button(root, text="Añadir", command=add_usuario)
boton_add.pack()

boton_eliminar = tk.Button(root, text="Eliminar", command=eliminar_usuario)
boton_eliminar.pack()

frame_lista = tk.Frame(root)
frame_lista.pack(expand=True, fill="both")

scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side="right", fill="y")

listbox = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set)
listbox.pack()

scrollbar.config(command=listbox.yview)

boton_salir = tk.Button(root, text="Salir", command=root.destroy)
boton_salir.pack()

root.mainloop()