import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Pablo
apellido: Jesus
---
Ejercicio: for_06
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador=0
        resultado=""
        numero= int(prompt("Ver divisores", "Ingrese un numero"))
        for divisores in range(1, numero+1, 1):
            if numero%divisores==0:
                contador+=1
                resultado+=str(divisores) + ", "
        alert( "Resultado", "Lo numeros divisores de {0} son {1}y la cantidad es {2}".format(numero,resultado,contador)) 
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()