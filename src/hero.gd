extends CharacterBody2D

@export var nav_optimize_path : bool = false

var speed = 250
var path = []

# final navigation destination position/point
var nav_destination : Vector2 
# The normal path to the destination
var character_nav_path : Array = []


func get_input():
	# Detect up/down/left/right keystate and only move when pressed.
	velocity = Vector2()
	if Input.is_action_pressed('ui_right'):
		velocity.x += 1
	if Input.is_action_pressed('ui_left'):
		velocity.x -= 1
	if Input.is_action_pressed('ui_down'):
		velocity.y += 1
	if Input.is_action_pressed('ui_up'):
		velocity.y -= 1
	if Input.is_action_just_pressed('click'):
		pass
#		path = NavigationServer2D.map_get_path(get_parent(), self.position, get_local_mouse_position())
	velocity = velocity.normalized() * speed


func _physics_process(delta):
	get_input()
	move_and_collide(velocity * delta)


func set_navigation_position(nav_position_to_set : Vector2) -> void:
	nav_destination = nav_position_to_set
	
	# set the new character target location
	$NavigationAgent2D.set_target_location(nav_destination)
	
	# calculate a new map path with the server using character nav agent map and new nav destination
	character_nav_path = NavigationServer2D.map_get_path($NavigationAgent2D.get_navigation_map(), global_position, nav_destination, nav_optimize_path)
	print(character_nav_path)
