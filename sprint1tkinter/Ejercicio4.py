import tkinter as tk

def actualizar_aficiones():
    aficiones = []
    if leer.get(): aficiones.append("Leer")
    if deporte.get(): aficiones.append("Deporte")
    if musica.get(): aficiones.append("Música")
    etiqueta.config(text="Aficiones: " + ", ".join(aficiones))

root = tk.Tk()
root.title("Ejercicio4")

leer = tk.IntVar()
deporte = tk.IntVar()
musica = tk.IntVar()

tk.Checkbutton(root, text="Leer", variable=leer, command=actualizar_aficiones).pack()

tk.Checkbutton(root, text="Deporte", variable=deporte, command=actualizar_aficiones).pack()

tk.Checkbutton(root, text="Musica", variable=musica, command=actualizar_aficiones).pack()

etiqueta = tk.Label(root, text="")
etiqueta.pack()

root.mainloop()