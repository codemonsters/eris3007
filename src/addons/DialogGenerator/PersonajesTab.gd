@tool
extends GridContainer

var elemento = preload("res://addons/DialogGenerator/utils/Element.tscn")

func _enter_tree():
	print("LKJBJA")
	for i in range(19):
		$HSplitContainer/ScrollContainer/VBoxContainer.add_child(elemento.instantiate())


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
