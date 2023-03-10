extends CharacterBody2D
class_name NPC 

@export var dialog_name: String

var dialog_signal

func _ready():
	self.add_to_group("NPC")


func speak():
	DialogManager.start_dialog(dialog_name)
