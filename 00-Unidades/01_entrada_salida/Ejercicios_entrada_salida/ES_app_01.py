import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Pablo
apellido: Jesus
---
Simulacro Turno Noche

Un famoso casino de mar del plata,  requiere una app para controlar el egreso de dinero durante una jornada. Para ello se ingresa por cada ganador:

Nombre

Importe ganado (mayor o igual $1000)

Género (“Femenino”, “Masculino”, “Otro”)

Juego (Ruleta, Poker, Tragamonedas)

Necesitamos saber:

Nombre y género de la persona que más ganó.

Promedio de dinero ganado en Ruleta.

Porcentaje de personas que jugaron en el Tragamonedas.

Cuál es el juego menos elegido por los ganadores.

El nombre del jugador que ganó más dinero jugando Poker
'''

class App(customtkinter.CTk):

    def init(self):
        super().init()

        self.title("UTN FRA")

        self.btnmostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btnmostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        
        while True:
            nombre = input("Ingrese su nombre")
            if nombre == None:
                break


if __name__ == "__main":
    app = App()
    app.geometry("300x300")
    app.mainloop()