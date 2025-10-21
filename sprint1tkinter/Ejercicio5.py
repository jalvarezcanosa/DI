import tkinter as tk

def cambiar_color():
    root.config(bg=color.get())

root = tk.Tk()
root.title("Ejercicio5")

color = tk.StringVar(value="white")

tk.Radiobutton(root, text="Rojo", variable=color, value="red", command=cambiar_color).pack()
tk.Radiobutton(root, text="Verde", variable=color, value="green", command=cambiar_color).pack()
tk.Radiobutton(root, text="Azul", variable=color, value="blue", command=cambiar_color).pack()

root.mainloop()