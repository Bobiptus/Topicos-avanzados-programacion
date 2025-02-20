from tkinter import *
import tkinter

ventana = tkinter.Tk()  # Crear una ventana
ventana.geometry("500x500")

# Definiendo los eventos del mouse
def click_izq(event):
    etiqueta.config(text=f"Click izquierdo en ({event.x}, {event.y})")

def click_der(event):
    etiqueta.config(text=f"Click derecho en ({event.x}, {event.y})")

def arrastrar(event):
    etiqueta.config(text=f"Arrastrando en ({event.x}, {event.y})")

# Asociando el mouse a las funciones
ventana.bind("<Button-1>", click_izq)
ventana.bind("<Button-3>", click_der)
ventana.bind("<B1-Motion>", arrastrar)

etiqueta = tkinter.Label(ventana, text = "Practica #2") # Crear una etiqueta
etiqueta.grid(row=1, column=2, padx=10, pady=10)

texto = tkinter.Label(ventana) # Desplegar el texto ingresado
texto.grid(row=2, column=1, padx=10, pady=10)

entrada = tkinter.Entry(ventana) # Crear una entrada de texto
entrada.grid(row=1, column=3, padx=10, pady=10)

boton_salir = tkinter.Button(ventana, text = "Salir", command=ventana.quit) # Crear un boton para salir
boton_salir.grid(row=3, column=1, padx=10, pady=10)

ventana.mainloop() # Mostrar la ventana