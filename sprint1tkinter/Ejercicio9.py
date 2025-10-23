import tkinter as tk
from tkinter import messagebox

def mostrar_acerca_de():


root = tk.Tk()
root.title("Ejercicio9")

barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

menu_archivo = tk.Menu(barra_menu)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Salir", command=root.quit)

menu_ayuda = tk.Menu(root)

root.mainloop()