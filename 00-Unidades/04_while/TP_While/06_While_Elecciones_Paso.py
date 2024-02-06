import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Pablo
apellido: Jesus
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        flag=True
        flagnombre=True
        flagedad=True
        flagvotos=True
        minimo=25555555555
        maximo=0
        contador=0
        sumaedad=0
        sumavotos=0
        while(flag):
            while(flagnombre):
                nombre = prompt("Nombre", "Ingrese nombre: ")
                if(nombre!=None and nombre!=""):
                    contador+=1
                    flagnombre=False
                else:
                    promedio=sumaedad/contador
                    alert("Resultados", "El candidato mas votado fue: " + nombremaximo + "\nEl candidato con menos votos fue: "
                    + nombreminimo + " con " + str(edad) + " años." + "\nEl promedio de edades de los candidatos fue de: "
                    + str(promedio) + "\nEl total de los votos emitidos fue de: " + str(sumavotos))
                    return 0
            while(flagedad):
                edad = int(prompt("Edad", "Ingrese edad (mayor a 25)"))
                if(edad>=25):
                    sumaedad+=edad
                    flagedad=False
            while(flagvotos):
                votos = int(prompt("Votos", "Ingrese la cantidad de votos"))
                if(votos>=0):
                    sumavotos+=votos
                    flagvotos=False
            if(votos<minimo):
                nombreminimo=nombre
                edadminimo=edad
                minimo=votos
            if(votos>maximo):
                nombremaximo=nombre
                maximo=votos
            flagnombre=True
            flagvotos=True
            flagedad=True


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
