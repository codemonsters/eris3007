@tool
extends VBoxContainer


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass



func _on_button_personajes_pressed():
	print(get_parent().get_parent())


func _on_button_dialogos_pressed():
	pass # Replace with function body.