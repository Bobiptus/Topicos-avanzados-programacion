from tkinter import filedialog, colorchooser, simpledialog
from tkinter import END, INSERT

def archivo_nuevo(texto, root, barra_estatus):
    texto.delete("1.0", END)
    root.title('Nuevo archivo - Editor de texto')
    barra_estatus.config(text="Nuevo archivo      ")

def archivo_abrir(texto, root, barra_estatus):
    texto.delete("1.0", END)
    archivo = filedialog.askopenfilename(initialdir="C:/", title="Abrir archivo", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
    if archivo:
        name = archivo.replace("C:/", "")
        root.title(f'{name} - Editor de texto')
        barra_estatus.config(text=f'{name}      ')
        with open(archivo, 'r') as file:
            contenido = file.read()
        texto.insert(END, contenido)
    return archivo

def grabarcomo(texto, root, barra_estatus):
    texto_a_grabar = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/", title="Guardar archivo como", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
    if texto_a_grabar:
        nombre = texto_a_grabar.replace("C:/", "")
        root.title(f'{nombre} - Editor de texto')
        barra_estatus.config(text=f'{nombre}      ')
        with open(texto_a_grabar, 'w') as file:
            file.write(texto.get("1.0", END))
    return texto_a_grabar

def grabararchivo(texto, name, barra_estatus):
    if name:
        with open(name, 'w') as file:
            file.write(texto.get("1.0", END))
        barra_estatus.config(text=f'Archivo guardado: {name}      ')
    else:
        return grabarcomo(texto, name, barra_estatus)

def cortartexto(texto, e):
    if e:
        return texto.selection_get()
    elif texto.selection_get():
        seleccionado = texto.selection_get()
        texto.delete("sel.first", "sel.last")
        return seleccionado

def copiartexto(root, texto, e):
    if e:
        return root.clipboard_get()
    elif texto.selection_get():
        seleccionado = texto.selection_get()
        root.clipboard_clear()
        root.clipboard_append(seleccionado)
        return seleccionado

def pegartexto(root, texto, seleccionado, e):
    if e:
        seleccionado = root.clipboard_get()
    if seleccionado:
        texto.insert(INSERT, seleccionado)

def cambiocolorfondo(texto):
    micolor = colorchooser.askcolor()[1]
    if micolor:
        texto.config(bg=micolor)

def cambiocolortextopredeterminado(texto):
    micolor = colorchooser.askcolor()[1]
    if micolor:
        texto.config(fg=micolor)

def buscar_texto(texto):
    texto.tag_remove("highlight", "1.0", END)
    buscar = simpledialog.askstring("Buscar", "Ingrese el texto a buscar:")
    if buscar:
        indice_inicio = "1.0"
        while True:
            indice_inicio = texto.search(buscar, indice_inicio, stopindex=END)
            if not indice_inicio:
                break
            indice_fin = f"{indice_inicio}+{len(buscar)}c"
            texto.tag_add("highlight", indice_inicio, indice_fin)
            texto.tag_config("highlight", background="yellow", foreground="black")
            indice_inicio = indice_fin

def reemplazar_texto(texto):
    buscar = simpledialog.askstring("Buscar", "Ingrese el texto a buscar:")
    reemplazo = simpledialog.askstring("Reemplazar", "Ingrese el nuevo texto:")
    if buscar and reemplazo:
        contenido = texto.get("1.0", END)
        nuevo_contenido = contenido.replace(buscar, reemplazo)
        texto.delete("1.0", END)
        texto.insert("1.0", nuevo_contenido)