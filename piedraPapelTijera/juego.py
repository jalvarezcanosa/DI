import random
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

def jugar(opcion_elegida):
    opciones = ["piedra", "papel", "tijera"]

    opcion_maquina = random.choice(opciones)

    eleccion_jugador.set(f"Elegiste: {opcion_elegida.upper()}")
    eleccion_maquina.set(f"Tu rival eligió: {opcion_maquina.upper()}")

    if opcion_elegida == opcion_maquina:
        resultado_ronda.set("Es un empate")

    elif (opcion_elegida == "piedra" and opcion_maquina == "tijera") or \
            (opcion_elegida == "papel" and opcion_maquina == "piedra") or \
            (opcion_elegida == "tijera" and opcion_maquina == "papel"):
        resultado_ronda.set("Ganaste la ronda")
        puntos_actuales = marcador_jugador.get()
        marcador_jugador.set(puntos_actuales + 1)
    else:
        resultado_ronda.set("¡Tu rival gana la ronda!")
        puntos_actuales = marcador_maquina.get()
        marcador_maquina.set(puntos_actuales + 1)

    verificar_ganador()

def verificar_ganador():
    if marcador_jugador.get() == 3:
        messagebox.showinfo("Fin de la Partida", "¡FELICIDADES, GANASTE EL JUEGO!")

    elif marcador_maquina.get() == 3:
        messagebox.showinfo("Fin de la Partida", "¡OH NO! PERDISTE")

def reiniciar_juego():
    marcador_jugador.set(0)
    marcador_maquina.set(0)
    eleccion_jugador.set("")
    eleccion_maquina.set("")
    resultado_ronda.set("¡Haz tu jugada para empezar!")

root = tk.Tk()
img_piedra = tk.PhotoImage(file="piedra.png")
img_papel = tk.PhotoImage(file="papel.png")
img_tijera = tk.PhotoImage(file="tijera.png")
root.title("Piedra, Papel o Tijera")

marcador_jugador = tk.IntVar(value=0)
marcador_maquina = tk.IntVar(value=0)

eleccion_jugador = tk.StringVar()
eleccion_maquina = tk.StringVar()
resultado_ronda = tk.StringVar()

frame_titulo = tk.Frame(root)
frame_titulo.pack(fill="x")

tk.Label(frame_titulo, text="Piedra, Papel o Tijera").pack()
tk.Label(frame_titulo, text= "EL QUE LLEGUE A TRES GANARÁ").pack()

frame_marcador = tk.LabelFrame(root, text="Marcador")
frame_marcador.pack(fill="x")

tk.Label(frame_marcador, text="Jugador").pack()
tk.Label(frame_marcador, textvariable=marcador_jugador).pack()

tk.Label(frame_marcador, text="Rival").pack()
tk.Label(frame_marcador, textvariable=marcador_maquina).pack()

frame_juego = tk.Frame(root)
frame_juego.pack(fill="x")

tk.Label(frame_juego, textvariable=eleccion_jugador).pack()
tk.Label(frame_juego, textvariable=eleccion_maquina).pack()

tk.Label(frame_juego, textvariable=resultado_ronda).pack()

boton_piedra = tk.Button(frame_juego, image=img_piedra, command=lambda: jugar("piedra"))
boton_papel = tk.Button(frame_juego, image=img_papel, command=lambda: jugar("papel"))
boton_tijera = tk.Button(frame_juego, image=img_tijera, command=lambda: jugar("tijera"))

boton_piedra.pack()
boton_papel.pack()
boton_tijera.pack()

frame_opciones = tk.Frame(root)
frame_opciones.pack(fill="x", pady=10)

boton_nuevo_juego = tk.Button(frame_opciones, text="Nuevo juego", command=reiniciar_juego)
boton_nuevo_juego.pack()
boton_salir = tk.Button(frame_opciones, text="Salir", command=root.destroy)
boton_salir.pack()

root.mainloop()