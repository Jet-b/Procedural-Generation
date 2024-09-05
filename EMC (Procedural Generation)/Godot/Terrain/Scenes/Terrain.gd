extends TileMap

# The ID of the tile you want to fill the TileMap with
@export var tile_id: int = 0

# The size of the TileMap in tiles
@export var map_size: Vector2i = Vector2i(10, 10)

# debugging
var cell_size: int = 16

func _ready():
	fill_tilemap()

func _draw():
	for x in range(map_size.x):
		for y in range(map_size.y):
			draw_rect(Rect2(Vector2(x, y) * cell_size, Vector2(cell_size, cell_size)), Color.RED)
	fill_tilemap()

func _process(delta):
	fill_tilemap()

func fill_tilemap():
	for x in range(map_size.x):
		for y in range(map_size.y):
			set_cell(0, Vector2i(x, y), tile_id)
			print("Placing tile at " + str(Vector2i(x, y)))
