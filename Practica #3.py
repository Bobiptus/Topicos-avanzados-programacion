from tkinter import *
import tkinter
import tkinter.messagebox

# Crear una ventana
ventana = tkinter.Tk() 
ventana.title("Formulario")
ventana.geometry("250x300")

#creacion variables
nombre = tkinter.StringVar()
correo = tkinter.StringVar()
edad = tkinter.StringVar()
escolaridad = tkinter.StringVar()
escolaridad.set("Seleccione la escolaridad")

opciones_escolaridad = ["Primaria", "Secundaria", "Preparatoria", "Universidad"]

# Limpiar los campos
def limpiar():
    nombre.set("")
    correo.set("")
    edad.set("")
    escolaridad.set("Seleccione la escolaridad")
    
# Crear una funcion para validar los datos
def validar():
    if not nombre.get():
        tkinter.messagebox.showerror("Error", "El nombre es requerido")
        return
    elif "@" not in correo.get() or "." not in correo.get():
        tkinter.messagebox.showerror("Error", "El correo no es valido")
        return
    elif not edad.get().isdigit():
        tkinter.messagebox.showerror("Error", "Edad debe ser numero")
        return
    elif escolaridad.get() == "Seleccione la escolaridad":
        tkinter.messagebox.showerror("Error", "Seleccione la escolaridad")
        return
    tkinter.messagebox.showinfo("Exito", "Datos validados correctamente")
    
tkinter.Label(ventana, text="Nombre:").pack()
tkinter.Entry(ventana, textvariable=nombre).pack()

tkinter.Label(ventana, text="Correo:").pack()
tkinter.Entry(ventana, textvariable=correo).pack()

tkinter.Label(ventana, text="Edad:").pack()
tkinter.Entry(ventana, textvariable=edad).pack()

tkinter.Label(ventana, text="Escolaridad:").pack()
tkinter.OptionMenu(ventana, escolaridad, *opciones_escolaridad).pack(pady=10)

# Crear un boton para validar
boton_validar = tkinter.Button(ventana, text = "Validar", command=validar)
boton_validar.pack(padx=10)

# Crear un boton para limpiar
boton_limpiar = tkinter.Button(ventana, text = "Limpiar", command=limpiar) 
boton_limpiar.pack(padx=10)

# Crear un boton para salir
boton_salir = tkinter.Button(ventana, text = "Salir", command=ventana.quit) 
boton_salir.pack(pady=20)

# Mostrar la ventana
ventana.mainloop() 