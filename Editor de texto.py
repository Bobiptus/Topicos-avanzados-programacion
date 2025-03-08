from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser

# Funciones de los menús
def archivo_nuevo():
    texto.delete("1.0", END)
    root.title('Nuevo archivo - Editor de texto')
    barra_estatus.config(text="Nuevo archivo      ")

def archivo_abrir():
    texto.delete("1.0", END)
    archivo = filedialog.askopenfilename(initialdir = "C:/", title="Abrir archivo", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if archivo:
        global name
        name = archivo
    barra_estatus.config(text=f'{name}      ')
    name =  name.replace("C:/", "")
    root.title(f'{name} - Editor de texto')
    archivo = open(archivo, 'r')
    contenido = archivo.read()
    texto.insert(END, contenido)
    archivo.close()
    
def grabarcomo():
    texto_a_grabar = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/", title="Guardar archivo como", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))) 
    if texto_a_grabar:\
        nombre = texto_a_grabar
    nombre =  nombre.replace("C:/", "")
    root.title(f'{nombre} - Editor de texto')
    barra_estatus.config(text=f'{nombre}      ')
    texto_a_grabar = open(texto_a_grabar, 'w')
    texto_a_grabar.write(texto.get(1.0, END))
    texto_a_grabar.close()

def grabararchivo():
    global name
    if name:
        contenido = texto.get(1.0, END)
        archivo = open(name, 'w')
        archivo.write(contenido)
        archivo.close()
        barra_estatus.config(text=f'Archivo guardado: {name}      ')
    else:
        grabarcomo()
        
def cortartexto(e):
    global seleccionado
    if e:
        seleccionado = texto.selection_get()
    else:
        if texto.selection_get():
            seleccionado = texto.selection_get()
            texto.delete("sel.first", "sel.last")
        
def copiartexto(e):
    global seleccionado
    if e:
        seleccionado = root.clipboard_get()
    else:
        if texto.selection_get():
            seleccionado = texto.selection_get()
            root.clipboard_clear()
            root.clipboard_append(seleccionado)
        
def pegartexto(e):
    global seleccionado
    if e:
        seleccionado = root.clipboard_get()
    else:
        if seleccionado: 
            posicion = texto.index(INSERT)
            texto.insert(posicion, seleccionado)
    
def cambiocolortexto():
    micolor = colorchooser.askcolor()[1]
    if micolor:
        barra_estatus.config(text=f'Color seleccionado: {micolor[1]}      ')
        color_texto = font.Font(texto,texto.cget("font"))
        texto.tag_configure("colortexto", font=color_texto, foreground=micolor)
        actualseleccion = texto.tag_ranges("sel")
        if "colored" in actualseleccion:
            texto.tag_remove("colored", "sel.first", "sel.last")
        else:
            texto.tag_add("colortexto", "sel.first", "sel.last")
        
def cambiocolorfondo():
    micolor = colorchooser.askcolor()[1]
    if micolor:
        texto.config(bg=micolor)

def cambiotodofondo():
    micolor = colorchooser.askcolor()[1]
    if micolor:
        texto.config(fg=micolor)       

# Crear la ventana raíz
root = Tk()
root.title("Editor de texto")
root.geometry("700x650")

# Marco de botones
marco_de_botones = Frame(root)
marco_de_botones.pack(fill=X)

# Crear un marco
mi_marco = Frame(root)
mi_marco.pack(pady=5)

# Crear una barra de desplazamiento
texto_scroll = Scrollbar(mi_marco)
texto_scroll.pack(side=RIGHT, fill=Y)

texto_scrollx = Scrollbar(mi_marco, orient="horizontal")
texto_scrollx.pack(side=BOTTOM, fill=X)

# Crear un cuadro de texto
texto = Text(mi_marco, width=97, height=25, selectbackground="blue", selectforeground="black", undo=True, yscrollcommand=texto_scroll.set, font = "Helvetica 14", wrap="none", xscrollcommand=texto_scrollx.set)  
texto.pack()

# Agrgarmos una barra de status
barra_estatus = Label(root, text="Preparado      ", anchor=E)
barra_estatus.pack(fill=X, side=BOTTOM, ipady=5)


# Configurar la barra de desplazamiento
texto_scroll.config(command=texto.yview)
texto_scrollx.config(command=texto.xview)

global name
name = False

global seleccionado
seleccionado = False
       
# Crear un menú
mi_menu = Menu(root)
root.config(menu=mi_menu)

# Menu Archivo
menu_archivo = Menu(mi_menu, tearoff=False)
mi_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Nuevo", command=archivo_nuevo)
menu_archivo.add_command(label="Abrir", command=archivo_abrir)
menu_archivo.add_command(label="Guardar", command=grabararchivo)
menu_archivo.add_command(label="Guardar como", command=grabarcomo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir")

# Menu Editar
menu_editar = Menu(mi_menu, tearoff=False)
mi_menu.add_cascade(label="Editar", menu=menu_editar)
menu_editar.add_command(label="Cortar   Ctrl+X", command=lambda: cortartexto(False))
menu_editar.add_command(label="Copiar   Ctrl+C", command=lambda: copiartexto(False))
menu_editar.add_command(label="Pegar   Ctrl+V", command=lambda: pegartexto(False))
menu_editar.add_separator()
menu_editar.add_command(label="Deshacer", command =texto.edit_undo, accelerator="Ctrl+Z") 
menu_editar.add_command(label="Rehacer", command =texto.edit_redo, accelerator="Ctrl+Y")

root.bind("<Control-x>", cortartexto)
root.bind("<Control-c>", copiartexto)
root.bind("<Control-v>", pegartexto)

# Botones
cambiocolor_texto = Button(marco_de_botones, text="Cambiar color de texto", command=cambiocolortexto)
cambiocolor_texto.grid(row=0, column=1, sticky=W)

cambiofondo_texto = Button(marco_de_botones, text="Cambiar color de fondo", command=cambiocolorfondo)
cambiofondo_texto.grid(row=0, column=2)

cambiotodo_texto = Button(marco_de_botones, text="Cambiar todo el color de fondo", command=cambiotodofondo)
cambiotodo_texto.grid(row=0, column=3)


root.mainloop()