extends CharacterBody2D
class_name NPC 

@export var dialog_name: String


func _ready():
	self.add_to_group("NPC")


func speak():
	#dialog_signal.emit(dialog_name)
	get_parent().emit_signal("show_dialog", dialog_name)
