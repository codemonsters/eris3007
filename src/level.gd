extends Node2D

signal show_dialog(dialog_name)

# Called when the node enters the scene tree for the first time.
func _ready():
	pass


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func _input(event):
	if event.is_action_pressed("click"):
#		print("Event click: ", event.position)
		$Hero.update_target_location(get_global_mouse_position())
		

func dialog(npc: CharacterBody2D, dialog_name: String):
	pass
