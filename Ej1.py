# EJERCICIO 1 TRABAJO PRACTICO 1 DE TKINTER
import tkinter as tk
from tkinter import ttk
import datetime as dt

class Ej1(tk.Tk):
    """_summary_

    Args:
        tk (tk): Clase de un boton de la GUI
    """    
    def __init__(self):
        """Datos de la GUI y boton fecha de hoy

        """        
        super().__init__()
        self.title("Ejercicio 1")
        self.geometry("300x300")
        self.boton = ttk.Button(self, text="Mostrar fecha", command=self.mostrar_fecha)
        self.boton.pack()
        self.mainloop()

    def mostrar_fecha(self):
        """Muestra la fecha actual mediante el import datetime al momento de usar el boton fecha de hoy de la GUI
        """        
        #print("Fecha del día", dt.datetime.now())
        ahora= dt.datetime.now()
        #print(f"Fecha del dia. Dia: {ahora.day}, mes: {ahora.month}, año: {ahora.year}")
        ahora_str= ahora.strftime("%d/%m/%y")
        print(f"Fecha del dia. {ahora_str}")
        


root = Ej1()
