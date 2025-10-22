import tkinter as tk


def mostrar_etiqueta():
    texto_entrada = entrada.get()
    etiqueta1.config(text=f"{texto_entrada}")

def borrar_etiqueta():
    entrada.delete(0, tk.END)

root = tk.Tk()
root.title("Ejercicio8")

frame1 = tk.Frame(root, bg="white")
frame1.pack()

frame2 = tk.Frame(root, bg= "grey")
frame2.pack()

boton_mostrar = tk.Button(frame2, text="Mostrar etiqueta", command=mostrar_etiqueta)
boton_mostrar.pack()

boton_borrar = tk.Button(frame2, text="Borrar", command=borrar_etiqueta)
boton_borrar.pack()

etiqueta1 = tk.Label(frame1, text="HOLA")
etiqueta1.pack()

etiqueta2 = tk.Label(frame1, text="ESCRIBE LO QUE QUIERAS")
etiqueta2.pack()

entrada = tk.Entry(frame1)
entrada.pack()

root.mainloop()