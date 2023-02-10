extends CharacterBody2D

@export var dialog_name: String

func speak():
	get_parent().dialog(self,dialog_name)
