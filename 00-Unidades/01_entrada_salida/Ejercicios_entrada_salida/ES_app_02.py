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
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        #Inicializacion de variables
        bandera_while = True
        bandera_mayor_ganador = True
        bandera_mayor_ganador_poker = True
        contador_poker = 0
        contador_ruleta = 0
        contador_tragamonedas = 0
        acumulador_ruleta = 0
        total_personas = 0
        nombre_mayor_ganador = ""
        genero_mayor_ganador = ""
        promedio_ruleta = 0

        while bandera_while:
            #ingreso de datos
            nombre = input("Ingrese su nombre: ")
            while nombre == "" or nombre == None or nombre:
                nombre = input ("Ingrese un nombre valido")
            importe = input("Ingrese importe ganado: ")
            while not importe.isdigit() or int(importe) < 1000:
                importe = input("Ingrese un importe valido: ")
            importe = int(importe)
            genero = input("Ingrese genero: ")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = input ("Ingrese genero valido: ")
            juego = input ("Ingrese juego: ")
            while juego != "Ruleta" and juego != "Poker" and juego != "Tragamonedas":
                juego = input ("Ingrese juego valido: ")
            total_personas += 1
            #fin ingreso de datos
            #Nombre y genero de la persona que mas gano    
            if bandera_mayor_ganador == True or importe > monto_maximo:
                bandera_mayor_ganador = False
                monto_maximo = importe
                nombre_mayor_ganador = nombre
                genero_mayor_ganador = genero
            #Promedio de dinero ganado en ruleta
            match juego:
                case "Poker":
                    contador_poker +=1
                    if contador_poker == 1 or contador_poker > mayor_ganador_poker:
                        bandera_mayor_ganador_poker = False
                        mayor_ganador_poker = contador_poker
                        nombre_mayor_ganador_poker = nombre
                case "Ruleta":
                    contador_ruleta += 1
                    acumulador_ruleta += importe

                case "Tragamonedas":
                    contador_tragamonedas += 1

        #Calculo promedio ganado en la ruleta
        if contador_ruleta > 0:
            promedio_ruleta = acumulador_ruleta / contador_ruleta
        #Calculo porcentaje de personas que jugaron al tragamonedas
        if total_personas > 0:
            porcentaje_personas_tragamonedas = contador_tragamonedas * 100 / total_personas
        #Verificacion juego menos elegido
        if contador_poker < contador_ruleta and contador_poker < contador_tragamonedas:
            juego_menos_elegido = "Poker"
        elif contador_ruleta < contador_tragamonedas:
            juego_menos_elegido = "Ruleta"
        else:
            juego_menos_elegido = "Tragamonedas"
        #Impresion en pantalla
        if nombre_mayor_ganador != "" and genero_mayor_ganador != "":
            print (f"El mayor ganador se llama {nombre_mayor_ganador} y su genero es {genero_mayor_ganador}")
        else:
            print (f"No hubo ningun ganador")
        if promedio_ruleta > 0:
            print (f"El promedio del dinero ganado en la ruleta es de {promedio_ruleta}")
        else:
            print ("Nadie ha ganado en la ruleta")
        if total_personas > 0:
            print (f"El porcentaje de las personas que jugaron al tragamonedas fue %{porcentaje_personas_tragamonedas}")
            print (f"El juego menos elegido fue el {juego_menos_elegido}")
        if contador_poker > 0:
            print (f"El nombre del jugador que mas gano jugando al Poker es {nombre_mayor_ganador_poker}")
        else:
            print ("No hubo ganadores en poker")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()