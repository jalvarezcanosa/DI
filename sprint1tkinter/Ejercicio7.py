import tkinter as tk

root = tk.Tk()
root.title("Ejercicio7")

canvas = tk.Canvas(root, width = 500, height= 500, bg= "white")

x1 = 50
y1 = 50
x2 = 300
y2 = 300
canvas.create_rectangle(x1, y1, x2, y2, fill = "red")

canvas.pack()

root.mainloop()