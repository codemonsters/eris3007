extends Node2D


# Called when the node enters the scene tree for the first time.
func _ready():
	$BackgroundColor/Button.grab_focus()

func _on_button_pressed():
	get_parent().start_game()
