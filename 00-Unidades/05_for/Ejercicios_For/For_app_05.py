import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Pablo
apellido: Jesus
---
Ejercicio: for_05
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        pares=int(prompt("Ingrese numero", "Ingrese numero"))
        resultados=""
        for i in range(1,pares+1,1):
            if(i%2==0):
                resultados+=(str(i) + ", ")
        alert("Resultado","Los numeros pares son {0}y fueron {1} en total".format(resultados,int(pares/2)))
            
            
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()