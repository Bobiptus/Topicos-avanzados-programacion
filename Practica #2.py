from tkinter import *
import tkinter
import random

# Crear una ventana
ventana = tkinter.Tk() 
ventana.title("Eventos del mouse y teclado")
ventana.geometry("500x500")

# Función para cambiar el fondo de la ventana
def cambiar_fondo():
    colores = ["red", "blue", "green", "yellow", "orange", "purple"]
    color = random.choice(colores)
    ventana.config(bg = color)

# Definiendo los eventos del mouse
def click_izq(event):
    etiqueta_eventos.config(text=f"Click izquierdo en ({event.x}, {event.y})")
    
def double_click(event):
    etiqueta_eventos.config(text=f"Doble click en ({event.x}, {event.y})")
    color = random.choice(["red", "blue", "green", "yellow", "orange", "purple"])
    ventana.config(bg = color)
    
def click_der(event):
    etiqueta_eventos.config(text=f"Click derecho en ({event.x}, {event.y})")

def arrastrar(event):
    etiqueta_eventos.config(text=f"Arrastrando en ({event.x}, {event.y})")

# Asociando el mouse a las funciones
ventana.bind("<Button-1>", click_izq)
ventana.bind("<Button-3>", click_der)
ventana.bind("<Double-Button-1>", double_click)
ventana.bind("<B1-Motion>", arrastrar)

# Definiendo eventos del teclado

def tecla_presionada(event):
    etiqueta_eventos.config(text=f"Tecla presionada: {event.char}")
    
def tecla_espacio(event):
    etiqueta_eventos.config(text="Espacio presionado")
    
def tecla_escape(event):
    ventana.quit()

# Asociando el teclado a las funciones
ventana.bind("<Key>", tecla_presionada)
ventana.bind("<space>", tecla_espacio)
ventana.bind("<Escape>", tecla_escape)

# Etiqueta fija para el título (no se sobrescribe)
etiqueta_titulo = tkinter.Label(ventana, text="Practica #2", font=("Arial", 16), fg="blue")
etiqueta_titulo.pack(pady=10)

# Etiqueta específica para mostrar los eventos sin sobrescribir el título
etiqueta_eventos = tkinter.Label(ventana, text="Aquí se mostrarán los eventos", font=("Arial", 12), fg="green")
etiqueta_eventos.pack(pady=20)

# Crear un boton para salir
boton_salir = tkinter.Button(ventana, text = "Salir", command=ventana.quit) 
boton_salir.pack(pady=30)

# Mostrar la ventana
ventana.mainloop() 