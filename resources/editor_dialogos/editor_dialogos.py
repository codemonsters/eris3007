# Editor de diálogos del juego

# En Linux, requiere tener instalado TK (ej: "$ yay -S tk")

import tkinter as tk
from tkinter import ttk, Frame, Label, Y


def btn_new_character_pressed():
    pass


def btn_delete_character_pressed():
    pass


root = tk.Tk()
root.title("Editor de Diálogos")
root.geometry("800x600")

tab_control = ttk.Notebook(root)                        # Grupo de pestañas principales de la aplicación

tab_characters = ttk.Frame(tab_control)                 # Pestaña para gestionar los personajes
tab_dialogs = ttk.Frame(tab_control)                    # Pestaña para gestionar los diálogos

tab_control.add(tab_characters, text='Personajes')
tab_control.add(tab_dialogs, text='Diálogos')
tab_control.pack(expand=True, fill="both")

# Pestaña Personajes

# Pestaña Personajes / Parte izquierda: Botones crear, eliminar y lista para seleccionar personaje

frame_character_navigation = Frame(tab_characters)      # Frame para alojar todos los widgets de la navegación de personajes

frame_character_navigation.pack(side="left", expand=False, fill="y")

frame_buttons_select_character = Frame(frame_character_navigation)
frame_buttons_select_character.pack()
btn_new_character = ttk.Button(frame_buttons_select_character, text="Nuevo", command=btn_new_character_pressed)
btn_new_character.pack(side="left", anchor="nw")

btn_delete_character = ttk.Button(frame_buttons_select_character, text="Eliminar", command=btn_delete_character_pressed)
btn_delete_character.pack(side="left", anchor="nw")

lst_characters = tk.Listbox(frame_character_navigation)

lst_characters.pack(side="bottom", anchor="n", expand=True, fill=Y)

# Pestaña Personajes / Parte derecha: Campos para editar el personaje seleccionado o crear uno nuevo

frame_edit_character = Frame(tab_characters)            # Frame para alojar todos los widgets de la edición de los personajes

frame_edit_character.pack(side="left", expand=True, fill="both")

lbl_character_id = Label(frame_edit_character, text="Id: ").grid(row=0, column=0)
txt_character_id = Label(frame_edit_character, text="[VALOR DEL ID AQUI]").grid(row=0, column=1)
lbl_character_name = Label(frame_edit_character, text="Nombre: ").grid(row=1, column=0)
txt_character_name = Label(frame_edit_character, text="[VALOR DEL NOMBRE AQUI]").grid(row=1, column=1)
lbl_character_image = Label(frame_edit_character, text="Imagen: ").grid(row=2, column=0)
txt_character_image = Label(frame_edit_character, text="[NOMBRE DEL ARCHIVO IMAGEN AQUÍ]").grid(row=2, column=1)


#lbl_temp.pack()

# Pestaña Diálogos

# TODO: Implementar

# keep the window displaying
root.mainloop()

'''
ttk.Label(tabPersonajes, 
          text ="Tab de los personajes").grid(column = 0, 
                               row = 0,
                               padx = 30,
                               pady = 30)  
ttk.Label(tabDialogos,
          text ="Tab de los diálogos").grid(column = 0,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)

# place a label on the root window
message = tk.Label(root, text="Hello, World!")
message.pack()
'''
