from tkinter import *

from txted import (archivo_abrir, archivo_nuevo, buscar_texto,
                   cambiocolorfondo, cambiocolortextopredeterminado,
                   copiartexto, cortartexto, grabararchivo, grabarcomo,
                   pegartexto, reemplazar_texto)

# import txted

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
texto = Text(
    mi_marco,
    width=97,
    height=25,
    selectbackground="blue",
    selectforeground="black",
    undo=True,
    yscrollcommand=texto_scroll.set,
    font="Helvetica 14",
    wrap="none",
    xscrollcommand=texto_scrollx.set,
)
texto.pack()

# Agregar una barra de estado
barra_estatus = Label(root, text="Preparado      ", anchor=E)
barra_estatus.pack(fill=X, side=BOTTOM, ipady=5)

# Configurar la barra de desplazamiento
texto_scroll.config(command=texto.yview)
texto_scrollx.config(command=texto.xview)

name = False
seleccionado = ""

# Crear un menú
mi_menu = Menu(root)
root.config(menu=mi_menu)

# Menú Archivo
menu_archivo = Menu(mi_menu, tearoff=False)
mi_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(
    label="Nuevo", command=lambda: archivo_nuevo(texto, root, barra_estatus)
)
menu_archivo.add_command(
    label="Abrir", command=lambda: archivo_abrir(texto, root, barra_estatus)
)
menu_archivo.add_command(
    label="Guardar", command=lambda: grabararchivo(texto, name, barra_estatus)
)
menu_archivo.add_command(
    label="Guardar como", command=lambda: grabarcomo(texto, root, barra_estatus)
)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)

# Menú Editar
menu_editar = Menu(mi_menu, tearoff=False)
mi_menu.add_cascade(label="Editar", menu=menu_editar)
menu_editar.add_command(
    label="Cortar   Ctrl+X", command=lambda: cortartexto(texto, False)
)
menu_editar.add_command(
    label="Copiar   Ctrl+C", command=lambda: copiartexto(root, texto, False)
)
menu_editar.add_command(
    label="Pegar   Ctrl+V", command=lambda: pegartexto(root, texto, seleccionado, False)
)
menu_editar.add_separator()
menu_editar.add_command(label="Deshacer", command=texto.edit_undo, accelerator="Ctrl+Z")
menu_editar.add_command(label="Rehacer", command=texto.edit_redo, accelerator="Ctrl+Y")
menu_editar.add_command(
    label="Buscar", command=lambda: buscar_texto(texto), accelerator="Ctrl+B"
)
menu_editar.add_command(
    label="Reemplazar", command=lambda: reemplazar_texto(texto), accelerator="Ctrl+R"
)

root.bind("<Control-x>", lambda e: cortartexto(texto, e))
root.bind("<Control-c>", lambda e: copiartexto(root, texto, e))
root.bind("<Control-v>", lambda e: pegartexto(root, texto, seleccionado, e))

# Botones
cambiofondo_texto = Button(
    marco_de_botones,
    text="Cambiar color de fondo",
    command=lambda: cambiocolorfondo(texto),
)
cambiofondo_texto.grid(row=0, column=2)

cambiotodo_texto = Button(
    marco_de_botones,
    text="Cambiar color predeterminado texto",
    command=lambda: cambiocolortextopredeterminado(texto),
)
cambiotodo_texto.grid(row=0, column=3)

root.mainloop()
