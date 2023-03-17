extends CharacterBody2D
class_name NPC 

@export var dialog_name: String

signal show_dialog(dialog_name)

func _ready():
	self.add_to_group("NPC")


func speak():
	#dialog_signal.emit(dialog_name)
	emit_signal("show_dialog", dialog_name)
