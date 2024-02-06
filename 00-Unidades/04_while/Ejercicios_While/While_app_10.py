import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Pablo
apellido: Jesus
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        flag=True
        sumap=0
        suman=0
        contadorp=0
        contadorn=0
        contadorc=0
        while(flag):
            numero = prompt(title="Numero", prompt="Ingrese numeros hasta que usted desee: ", initialvalue="0")
            if(numero==None):
                flag=False
            elif(numero=="0"):
                contadorc+=1
            elif(int(numero)<0):
                suman+=int(numero)
                contadorn+=1
            else:
                sumap+=int(numero)
                contadorp+=1
        alert(title="Resultados", message="Suma acumuladada de negativos: " + str(suman) +
              "\nSuma acumulada de positivos: " + str(sumap)+"\nCantidad de numeros positivos ingresados: " + str(contadorp) +
              "\nCantidad de numeros negativos ingresados: " + str(contadorn) + "\nCantidad de ceros: " + str(contadorc) + 
              "\nDiferencia entre positivos y negativos: " + str(contadorp-contadorn))
        pass

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
