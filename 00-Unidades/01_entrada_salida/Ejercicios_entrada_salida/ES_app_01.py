import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: entradasalida01
---
Enunciado:
Al presionar el  botón, se debe mostrar un mensaje como el siguiente "Esto no anda, funciona".
'''

class App(customtkinter.CTk):

    def init(self):
        super().init()

        self.title("UTN FRA")

        self.btnmostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btnmostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        alert ("Primer Programa" ,"Esto no anda, funciona" )
        pass


if __name == "__main":
    app = App()
    app.geometry("300x300")
    app.mainloop()