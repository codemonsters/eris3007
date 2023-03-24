# Editor de diálogos del juego

# En Linux, requiere tener instalado TK (ej: "$ yay -S tk")

import json
import tkinter as tk
from tkinter import ttk, Entry, Frame, Label, Y, filedialog

JSON_FILE="../../src/assets/dialogs.json"


def load_json():
    f = open(JSON_FILE)
    data = json.load(f)
    f.close()
    return data


def save_json(data):
    # Serializing json
    json_object = json.dumps(data, indent=4)
    with open(JSON_FILE, "w") as json_file:
        json_file.write(json_object)


def disable_character_edit_controls():
    txt_character_id.config(state="disabled")
    txt_character_name.config(state="disabled")
    txt_character_image.config(state="disabled")
    btn_choose_character_image.config(state="disabled")
    btn_character_edit_apply.config(state="disabled")
    btn_character_edit_cancel.config(state="disabled")


def enable_character_edit_controls():
    txt_character_id.config(state="normal")
    txt_character_name.config(state="normal")
    txt_character_image.config(state="normal")
    btn_choose_character_image.config(state="normal")
    btn_character_edit_apply.config(state="normal")
    btn_character_edit_cancel.config(state="normal")


def btn_new_character_pressed():
    enable_character_edit_controls()
    txt_character_id.focus_set()


def btn_delete_character_pressed():
    pass


def btn_choose_character_image_pressed():
    filetypes= (('text files', '*.txt'), ('All files', '*.*'))
    #filename = filedialog.askopenfilename(filetypes=filetypes)
    #print(f"->{filename}<-")
    pass


def btn_character_edit_cancel_pressed():
    pass


def btn_character_edit_apply_pressed():
    pass


try:
    data = load_json()
except FileNotFoundError:
    print(f"Creando nuevo archivo JSON en: {JSON_FILE}")
    data = {
        "characters": {},
        "dialogs": {}
    }
    save_json(data)
    data = load_json()


root = tk.Tk()

root.title("Editor de Diálogos")
root.geometry("800x600")

tab_control = ttk.Notebook(root)            # Grupo de pestañas principales

tab_characters = ttk.Frame(tab_control)     # Pestaña para gestionar personajes
tab_dialogs = ttk.Frame(tab_control)        # Pestaña para gestionar diálogos

tab_control.add(tab_characters, text='Personajes')
tab_control.add(tab_dialogs, text='Diálogos')
tab_control.pack(expand=True, fill="both")

# Pestaña Personajes (parte izquierda): crear, eliminar y lista de personajes

# Frame para widgets de navegación de personajes
frame_character_navigation = Frame(tab_characters)

frame_character_navigation.pack(side="left", expand=False, fill="y")

frame_buttons_select_character = Frame(frame_character_navigation)
frame_buttons_select_character.pack()
btn_new_character = ttk.Button(frame_buttons_select_character,
                               text="Nuevo",
                               command=btn_new_character_pressed)
btn_new_character.pack(side="left", anchor="nw")

btn_delete_character = ttk.Button(
    frame_buttons_select_character,
    text="Eliminar",
    command=btn_delete_character_pressed)
btn_delete_character.pack(side="left", anchor="nw")

lst_characters = tk.Listbox(frame_character_navigation)

lst_characters.pack(side="bottom", anchor="n", expand=True, fill=Y)

# Pestaña Personajes (parte derecha): campos edición personaje seleccionado

# Frame para alojar todos los widgets de la edición de los personajes
frame_edit_character = Frame(tab_characters)

frame_edit_character.pack(side="left", expand=True, fill="both")

lbl_character_id = Label(frame_edit_character, text="Id: ")
lbl_character_id.grid(row=0, column=0)

txt_character_id = Entry(frame_edit_character)
txt_character_id.grid(row=0, column=1)

lbl_character_name = Label(frame_edit_character, text="Nombre: ")
lbl_character_name.grid(row=1, column=0)
txt_character_name = Entry(frame_edit_character)
txt_character_name.grid(row=1, column=1)

lbl_character_image = Label(frame_edit_character,text="Imagen: ")
lbl_character_image.grid(row=2, column=0)

frame_character_image = ttk.Frame(frame_edit_character)
frame_character_image.grid(row=2, column=1)
txt_character_image = Entry(frame_character_image)
txt_character_image.pack(side="left")
btn_choose_character_image = ttk.Button(frame_character_image, text="Examinar", command=btn_choose_character_image_pressed())
btn_choose_character_image.pack(side="left")

frame_character_edit_apply_or_cancel = ttk.Frame(frame_edit_character)
frame_character_edit_apply_or_cancel.grid(row=3, column=1)
btn_character_edit_apply = ttk.Button(frame_character_edit_apply_or_cancel, text="Apply", command=btn_character_edit_apply_pressed())
btn_character_edit_apply.pack(side="left")
btn_character_edit_cancel = ttk.Button(frame_character_edit_apply_or_cancel, text="Cancel", command=btn_character_edit_cancel_pressed())
btn_character_edit_cancel.pack(side="left")

# Pestaña Diálogos

# TODO: Implementar

disable_character_edit_controls()

# keep the window displaying
root.mainloop()
