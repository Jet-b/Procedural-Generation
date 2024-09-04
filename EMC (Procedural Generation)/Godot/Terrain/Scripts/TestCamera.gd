extends Camera2D

@export var speed: int = 400
@export var zoom_factor = 0.1

func _ready():
	pass

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	
	var direction = Vector2.ZERO

	if Input.is_action_pressed("move_up"):
		direction.y -= 1
	if Input.is_action_pressed("move_down"):
		direction.y += 1
	if Input.is_action_pressed("move_left"):
		direction.x -= 1
	if Input.is_action_pressed("move_right"):
		direction.x += 1

	if direction != Vector2.ZERO:
		direction = direction.normalized()
	direction.x /= zoom.x
	direction.y /= zoom.y

	# position is the camera's real time position
	position += direction * speed * delta

	# Zoom in and out with the mouse wheel
	if Input.is_action_pressed("zoom_in"):
		zoom /= Vector2(zoom_factor, zoom_factor)
	if Input.is_action_pressed("zoom_out"):
		zoom *= Vector2(zoom_factor, zoom_factor)
