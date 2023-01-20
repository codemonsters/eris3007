extends CharacterBody2D

@export var nav_optimize_path : bool = false
@onready var nav_agent: NavigationAgent2D = $NavigationAgent2D

var speed = 250
var speed_test = 300
var path = []

func _ready():
	nav_agent.path_desired_distance = 4.0
	nav_agent.target_desired_distance = 4.0


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
#	if Input.is_action_just_pressed('click'):
#		update_target_location(Vector2(44, 184))
		
#		path = NavigationServer2D.map_get_path(get_parent(), self.position, get_local_mouse_position())
	velocity = velocity.normalized() * speed


func _physics_process(delta):
	if nav_agent.is_target_reached():
		return
	var current_agent_position : Vector2 = global_transform.origin
	var next_path_position : Vector2 = nav_agent.get_next_location()
	
	var new_vel = (next_path_position - current_agent_position).normalized() * speed_test

	
	
	set_velocity(new_vel)

#	get_input()
	move_and_slide()
	
func update_target_location(target_location: Vector2):
	nav_agent.set_target_location(target_location)

