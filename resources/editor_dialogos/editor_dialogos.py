# Editor de diálogos del juego
# 
# En Linux, requiere tener instalado TK (ej: "$ yay -S tk")

import tkinter as tk
from tkinter import ttk


def btn_new_character_pressed():
    pass


def btn_delete_character_pressed():
    pass


root = tk.Tk()
root.title("Editor de Diálogos")
root.geometry("800x600") 

tab_control = ttk.Notebook(root)

tab_characters = ttk.Frame(tab_control)
tab_dialogs = ttk.Frame(tab_control)

tab_control.add(tab_characters, text ='Personajes')
tab_control.add(tab_dialogs, text ='Diálogos')
tab_control.pack(expand = 1, fill ="both")

btn_new_character = ttk.Button(tab_characters, text="Nuevo personaje", command=btn_new_character_pressed)
btn_new_character.pack(side="left", anchor="nw")

btn_delete_character = ttk.Button(tab_characters, text="Eliminar personaje", command=btn_delete_character_pressed)
btn_delete_character.pack(side="left", anchor="nw")







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

# keep the window displaying
root.mainloop()
