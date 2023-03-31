# Editor de diálogos del juego

# En Linux, requiere tener instalado TK (ej: "$ yay -S tk")

import json
import os
import tkinter as tk
from tkinter import filedialog, Entry, Frame, Label, messagebox, ttk, Y

IMAGE_ROOT_FOLDER = "../../src/assets"
JSON_FILE = "../../src/assets/dialogs.json"

CHARACTER_NOT_BEING_EDITED = 0
INSERTING_CHARACTER = 1
EDITING_CHARACTER = 2


character_edit_mode = CHARACTER_NOT_BEING_EDITED


# lee la lista de personajes desde data y refresca el widget Listbox lst_characters
def refresca_lista_personajes():
    lst_characters.delete(0, tk.END)
    for character in data["characters"]:
        lst_characters.insert(0, character)


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


def clear_character_edit_fields():
    txt_character_id.delete(0, tk.END)
    txt_character_name.delete(0, tk.END)
    txt_character_image.delete(0, tk.END)


def disable_character_edit_controls():
    txt_character_id.config(state="disabled")
    txt_character_name.config(state="disabled")
    txt_character_image.config(state="disabled")
    btn_choose_character_image.config(state="disabled")
    btn_character_edit_accept.config(state="disabled")
    btn_character_edit_cancel.config(state="disabled")


def enable_character_edit_controls():
    txt_character_id.config(state="normal")
    txt_character_name.config(state="normal")
    txt_character_image.config(state="normal")
    btn_choose_character_image.config(state="normal")
    btn_character_edit_accept.config(state="normal")
    btn_character_edit_cancel.config(state="normal")


def btn_new_character_pressed():
    global character_edit_mode
    if character_edit_mode == EDITING_CHARACTER:
        messagebox.showerror(message="Finaliza la edición del personaje actual antes de insertar uno nuevo", title="Error")
        return
    elif character_edit_mode == INSERTING_CHARACTER:
        messagebox.showerror(message="Ya estabas creando un personaje", title="Error")
        return
    character_edit_mode = INSERTING_CHARACTER
    enable_character_edit_controls()
    txt_character_id.focus_set()


def btn_delete_character_pressed():
    pass


def btn_choose_character_image_pressed():
    filetypes= (('png files', '*.png'), ('All files', '*.*'))
    filename = filedialog.askopenfilename(initialdir=IMAGE_ROOT_FOLDER, filetypes=filetypes).strip()
    if len(filename) > 0:
        # Si el path es absoluto, lo convertimos a un path relativo a partir de IMAGE_ROOT_FOLDER
        if os.path.isabs(filename):
            image_root_path = os.path.abspath(IMAGE_ROOT_FOLDER)
            filename = os.path.relpath(filename, image_root_path)
        txt_character_image.delete(0, tk.END)
        txt_character_image.insert(0, filename)


def btn_character_edit_cancel_pressed():
    global character_edit_mode
    clear_character_edit_fields()
    disable_character_edit_controls()
    character_edit_mode = CHARACTER_NOT_BEING_EDITED


def btn_character_edit_accept_pressed():
    global character_edit_mode
    character_id = txt_character_id.get()
    character_name = txt_character_name.get()
    character_img = txt_character_image.get()

    # Comprobamos si tenemos todos los datos
    if len(character_id) < 1:
        messagebox.showerror(message="Falta el id del personaje", title="Error")
        return
    if len(character_name) < 1:
        messagebox.showerror(message="Falta el nombre del personaje", title="Error")
        return
    if len(character_img) < 1:
        messagebox.showerror(message="Falta la imagen del personaje", title="Error")
        return
    
    if character_edit_mode == INSERTING_CHARACTER:
        # Comprueba si ya existe un personaje con el mismo ID
        # TODO: Implementar
        ya_existia = False
        print("Comprobando si el id ya existía")
        for character in data["characters"]:
            print("Comprobando si el id a insertar coincide con", character)
    
    
    if os.path.isabs(character_img):
            messagebox.showerror(message="No se permiten rutas absolutas para indicar la imagen", title="Error")
            return
    # Comprobar si el archivo de la imagen existe
    image_root_path = os.path.abspath(IMAGE_ROOT_FOLDER)
    absolute_image_path = os.path.join(image_root_path, character_img)
    if not os.path.isfile(absolute_image_path) or not os.access(absolute_image_path, os.R_OK):
        messagebox.showerror(message="No se puede leer la imagen indicada", title="Error")
        return

    # Datos ok, insertar o editar el personaje
    data["characters"][character_id] = {
        "name" : character_name,
        "img" : character_img
    }
    print(data)
    refresca_lista_personajes()
    clear_character_edit_fields()
    disable_character_edit_controls()
    print("DATA:", data)
    save_json(data)
    character_edit_mode = CHARACTER_NOT_BEING_EDITED
    

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

# --- definición del a interfaz de usuario ---

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
btn_choose_character_image = ttk.Button(frame_character_image, text="Examinar", command=btn_choose_character_image_pressed)
btn_choose_character_image.pack(side="left")

frame_character_edit_accept_or_cancel = ttk.Frame(frame_edit_character)
frame_character_edit_accept_or_cancel.grid(row=3, column=1)
btn_character_edit_accept = ttk.Button(frame_character_edit_accept_or_cancel, text="Accept", command=btn_character_edit_accept_pressed)
btn_character_edit_accept.pack(side="left")
btn_character_edit_cancel = ttk.Button(frame_character_edit_accept_or_cancel, text="Cancel", command=btn_character_edit_cancel_pressed)
btn_character_edit_cancel.pack(side="left")

# Pestaña Diálogos

# TODO: Implementar

# --- fin definición del a interfaz de usuario ---

refresca_lista_personajes()
disable_character_edit_controls()

# keep the window displaying
root.mainloop()
