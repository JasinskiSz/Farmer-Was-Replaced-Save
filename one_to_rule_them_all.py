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

def is_side_bigger_than_world(side_length):
	return side_length > get_world_size()

def farm(x_size, y_size, entity, ground, shouldWater, move_north, move_east):
	
	if is_side_bigger_than_world(x_size):
		x_size = get_world_size()
		
	if is_side_bigger_than_world(y_size):
		y_size = get_world_size()

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
			if move_north:
				move(North)
			else:
				move(South)

		# go back to the row start

		# when farm is max size go
		# over the edge
		if max_farm:
			if move_east:
				move(East)
			else:
				move(West)
		# when farm is smaller, go
		# back using the opposite
		# direction
		else:
			for i in range(farm_limit - 1):
				if not move_east:
					move(East)
				else:
					move(West)