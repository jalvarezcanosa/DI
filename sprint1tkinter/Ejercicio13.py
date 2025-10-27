import tkinter as tk

def dibujar_circulo(event):
    x, y = event.x, event.y
    radio=15

    canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="red", outline="black")

def borrar_canvas(event):
    canvas.delete("all")

root = tk.Tk()
root.title("Ejercicio13")

canvas = tk.Canvas(root, bg="white", borderwidth=2)
canvas.pack()

canvas.bind("<Button-1>", dibujar_circulo)

root.bind("<c>", borrar_canvas)

root.mainloop()