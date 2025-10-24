import tkinter as tk

root = tk.Tk()
root.title("Ejercicio10")
root.geometry("300x300")

frame= tk.Frame(root)
frame.pack(fill="both", expand=True)

texto_largo="Albion online es un mmorpg no lineal, en el que escribes tu propia historia" \
            "sin limitarte a seguir un camino prefijado, explora un amplio mundo abierto con 5 biomas únicos,"\
            " todo cuanto hagas tendrá su repercusión en el mundo, con la economía orientada al jugador de Albión,"\
            " los jugadores crean prácticamente todo el equipo a partir de los recursos que consiguen,"\
            " el equipo que llevas define quien eres, cambia de arma y armadura para pasar de caballero a mago,"\
            " o juega como una mezcla de ambas clases, aventúrate en el mundo abierto frente a los habitantes y las criaturas de Albión,"\
            " inicia expediciones o adéntrate en mazmorras en las que encontrarás enemigos aún más difíciles,"\
            " enfréntate a otros jugadores en encuentros en el mundo abierto, lucha por los territorios o por ciudades enteras en batallas tácticas,"\
            " relájate en tu isla privada, donde podrás construir un hogar cultivar cosechas y criar animales, únete a un gremio, todo es mejor cuando se trabaja en grupo,"\
            " adéntrate ya en el mundo de Albión y escribe tu propia historia"
scrollbar = tk.Scrollbar(frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

text = tk.Text(frame)
text.insert(tk.INSERT, texto_largo)
text.pack()

text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)

root.mainloop()