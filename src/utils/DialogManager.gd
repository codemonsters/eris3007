extends Node


var dialog_path: String = "res://assets/dialog-sample.json"
var dict: Dictionary

# Called when the node enters the scene tree for the first time.
# Loads the JSON with the dialogs
func _ready():
	#$../../npc.connect("show_dialog", _on_show_dialog)
	#get_parent().get_parent().get_node("npc").connect("show_dialog", _on_show_dialog)
	#get_node("../../npc").connect("show_dialog", _on_show_dialog)
	#TODO conectar la señal show_dialog del nodo npc a la funcion _on_show_dialog de este script
	var file = FileAccess.open(dialog_path, FileAccess.READ)
	var text = file.get_as_text()
	
	var json = JSON.new()
	var result = json.parse(text)
	assert(result == OK, "El fichero está dañado!") 
	
	dict = json.get_data()
	file = null


# Called every frame. 'deltadict["dialogs"][dialog_name]["conversation"])' is the elapsed time since the previous frame.
func _process(delta):
	pass


func _on_show_dialog(dialog_name):
	print(dict["dialogs"][dialog_name]["conversation"])
	self.visible=true
#	get_parent().get_node("Game").start_dialog()
