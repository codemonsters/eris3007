extends Control

var d = 0

# Called when the node enters the scene tree for the first time.
func _ready():

	var new_dialog = Dialogic.start("New_Timeline")
	add_child(new_dialog)


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func random(integ):
	print(integ)
	return randi()%integ
