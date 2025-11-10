import tkinter as tk

def actualizar_valor(valor):
    etiqueta.config(text=f"Valor: {valor}")

root = tk.Tk()
root.title("Ejercicio11")

scale = tk.Scale(root, from_=0, to=100, orient="horizontal", command=actualizar_valor)
scale.pack()

etiqueta = tk.Label(root, text="Valor: 0")
etiqueta.pack()

root.mainloop()