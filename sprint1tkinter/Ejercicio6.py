import tkinter as tk

def mostrar_fruta():
    seleccion = listbox.curselection()
    if seleccion:
        fruta = listbox.get(seleccion[0])
        etiqueta.config(text=f"{fruta}")

root = tk.Tk()
root.title("Ejercicio6")

frutas = ["Manzana", "Banana", "Naranja"]

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
for fruta in frutas:
    listbox.insert(tk.END, fruta)

boton = tk.Button(root, text="Mostrar fruta", command=mostrar_fruta)
etiqueta = tk.Label(root, text="")

etiqueta.pack()
boton.pack()
listbox.pack()

root.mainloop()