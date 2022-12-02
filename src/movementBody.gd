extends CharacterBody2D

const accel = 1
const friction = 0.2

var xSpeed = 0
var ySpeed = 0

var xAxis
var yAxis

var signFactor

func _process(delta):
	velocity.x += xSpeed * delta
	velocity.y += ySpeed * delta
	
	inputSpeed()
	
	
	move_and_slide()

func inputSpeed():
	
	xAxis = Input.get_axis("ui_left", "ui_right")
	yAxis = Input.get_axis("ui_down", "ui_up")
	
	if xAxis:
		xSpeed += (accel * xAxis)
	
	if yAxis:
		ySpeed += (accel * yAxis)
	
	# FRICCIÓN
	
	if xSpeed:
		if xSpeed > 0:
			signFactor = 1
		else:
			signFactor = -1
		
		
