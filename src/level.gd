extends Node2D

@export_file var dialog_path
var dict


# Called when the node enters the scene tree for the first time.
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

func _input(event):
	if event.is_action_pressed("click"):
#		print("Event click: ", event.position)
		$Hero.update_target_location(get_global_mouse_position())

func dialog(npc: CharacterBody2D, dialog_name: String):
	print(dict["dialogs"][dialog_name]["conversation"])
