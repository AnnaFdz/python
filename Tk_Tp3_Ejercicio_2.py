import tkinter as tk
from tkinter import ttk, messagebox
class App(ttk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent= parent
        parent.title("Ejercicio 2")
        parent.geometry("200x200")
        ttk.Button(self, text="info", command=self.info).grid()
        ttk.Button(self, text="Advertencia", command=self.advertencia).grid()

    def advertencia(self, msj='Apretaste el boton Advertencia!'):
        messagebox.showinfo(message=msj)

    def info(self, msj='Apretaste el boton info!'):
        messagebox.showinfo(message=msj)    

root = tk.Tk()
App(root).grid()
root.mainloop()        