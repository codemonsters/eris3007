extends Node2D

@onready var level = preload("res://level.tscn")
@onready var dialog_scene = preload("res://DialogScene.tscn")


func start_game():
	change_screen(level)


func change_screen(target_screen_resource):
	get_child(0).queue_free()
	add_child(target_screen_resource.instantiate())

func start_dialog():
	add_child(dialog_scene.instantiate())
