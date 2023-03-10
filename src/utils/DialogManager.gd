extends Node

var dialog_path: String = "res://assets/dialog-sample.json"
var dict: Dictionary

# Called when the node enters the scene tree for the first time.
# Loads the JSON with the dialogs
func _ready():
	var file = FileAccess.open(dialog_path, FileAccess.READ)
	var text = file.get_as_text()
	
	var json = JSON.new()
	var result = json.parse(text)
	assert(result == OK, "El fichero está dañado!") 
	
	dict = json.get_data()
	file = null


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass


func start_dialog(dialog_name):
	print(dict["dialogs"][dialog_name]["conversation"])
	get_parent().get_node("Game").start_dialog()
