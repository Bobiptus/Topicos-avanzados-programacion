from tkinter import *
import tkinter

# Crear una ventana
ventana = tkinter.Tk() 
ventana.title("Eventos formulario")
ventana.geometry("500x500")



# Crear un boton para salir
boton_salir = tkinter.Button(ventana, text = "Salir", command=ventana.quit) 
boton_salir.pack(pady=30)

# Mostrar la ventana
ventana.mainloop() 