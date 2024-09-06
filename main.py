#Tkinter
import tkinter as tk


#CREAR UNA VENTANA
mi_ventana = tk.Tk()
mi_ventana.title("Erick Aguilar")
mi_ventana.geometry("500x600")

#Crear un texto
etiqueta = tk.Label(mi_ventana, text="Hola mundo")
etiqueta.pack(side=50)
mi_ventana.mainloop()
 