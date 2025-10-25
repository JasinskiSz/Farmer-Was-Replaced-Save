def plant_smth(entity, entity_ground_type, water):
	if get_ground_type() != entity_ground_type:
		till()
	plant(entity)
	if water and get_water() < 0.75:
		use_item(Items.Water)

def move_and_plant(entity, ground, direction, water):
	move(direction)
	plant_smth(entity, ground, water)

# This function will work if starting position is 0,0
def move_to_the_middle():
	half_size = (get_world_size() / 2) - 1
	for i in range(half_size):
		move(North)
		move(East)

def go_to(x, y):
	"""
	Moves the drone to the specified x and y
	coordinates

	Returns True when destination is reached
	Returns False when x or y exceed the world size
	"""
	x_now = get_pos_x()
	y_now = get_pos_y()

	if x == x_now and y == y_now:
		return True

	world_size = get_world_size()
	if world_size < x or world_size < y:
		return False
	
	move_north = True
	move_east = True
	
	x_abs = x - x_now
	y_abs = y - y_now

	if x_abs < 0:
		move_east = False
		x_abs = abs(x_abs)

	if y_abs < 0:
		move_north = False
		y_abs = abs(y_abs)

	for i in range(x_abs):
		move_if(move_east, East, West)

	for i in range(y_abs):
		move_if(move_north, North, South)

def go_to_start():
	"""
	Make the drone move to pos 0;0
	"""
	x = get_pos_x()
	y = get_pos_y()

	for i in range(x):
		move(West)
	
	for i in range(y):
		move(South)

def move_if(condition, goDirection, otherwiseDirection):
	if condition:
		move(goDirection)
	else:
		move(otherwiseDirection)

def farm(x_size, y_size, entity, ground, loopCondition, shouldWater, move_north, move_east):

	world_size = get_world_size()

	if x_size > world_size:
		x_size = world_size

	if y_size > world_size:
		y_size = world_size

	max_x_size = x_size == world_size 
	max_y_size = y_size == world_size

	while loopCondition:
		# going over y axis (columns up/down)
		for y in range(y_size):
			# going over x axis (rows left/right)
			for x in range(x_size):
				if can_harvest():
					harvest()
				plant_smth(entity, ground, shouldWater)
				# on last block in row, don't move
				if x != x_size - 1:
					if move_east:
						move(East)
					else:
						move(West)
			# on last block in column, don't move
			if y != y_size - 1:
				move_if(move_north, North, South)

			# go back to the row start
			# when farm x size is max go over the edge
			if max_x_size:
				move_if(move_east, East, West)

			# when farm is smaller, go back using
			# the opposite direction
			else:
				for i in range(x_size - 1):
					move_if(move_east, West, East)
		# go back to the column start
		# when farm x size is max go over the edge
		if max_y_size:
			move_if(move_north, North, South)

		# when farm is smaller, go back using
		# the opposite direction
		else:
			for i in range(y_size - 1):
				move_if(move_north, South, North)