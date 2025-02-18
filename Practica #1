from tkinter import *
import tkinter
import random

def mostrar():
    texto = entrada.get()
    etiqueta.config(text = texto)

def cambiar_fondo():
    colores = ["red", "blue", "green", "yellow", "orange", "purple"]
    color = random.choice(colores)
    ventana.config(bg = color)

ventana = tkinter.Tk()  # Crear una ventana
ventana.geometry("400x300")

boton = tkinter.Button(ventana, text = "Cambia la bienvenida", command=mostrar) # Crear un boton
boton.grid(row=1, column=1, padx=10, pady=10)

boton2 = tkinter.Button(ventana, text = "Cambiar color", command=cambiar_fondo) # Crear un boton para cambiar el color
boton2.grid(row=2, column=1, padx=10, pady=10)

boton_salir = tkinter.Button(ventana, text = "Salir", command=ventana.quit) # Crear un boton para salir
boton_salir.grid(row=3, column=1, padx=10, pady=10)

etiqueta = tkinter.Label(ventana, text = "Bienvenido") # Crear una etiqueta
etiqueta.grid(row=1, column=2, padx=10, pady=10)

texto = tkinter.Label(ventana) # Desplegar el texto ingresado
texto.grid(row=2, column=1, padx=10, pady=10)

entrada = tkinter.Entry(ventana) # Crear una entrada de texto
entrada.grid(row=1, column=3, padx=10, pady=10)

ventana.mainloop() # Mostrar la ventana