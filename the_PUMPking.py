# prepare the dictionary with (x,y) as key
# go over y
# go over x
# on every tile:
# - till the ground if not soil already
# - plant a pumpkin
#		save the position (x,y)
# 		save the time of planting
# 			every pumpkin takes 0.2-3.8 seconds to grow
# when all rows and columns are done, go back and check if can harvest
# go over y (backwards)
# go over x (backwards)
# on every tile:
# - save can_harvest() to dictionary
# - actually, just save can_harvest() where it is equal to False
# when all rows and columns are checked, turn on replanting mode
# go to (x,y) where can_harvest() == False
# check can_harvest() again and save the value
# if False, replant the pumpkin (should also check the time if able to harvest with given time constraints)
# if True, skip
# go over every item in dict like this

import one_to_rule_them_all

clear()

# width of the pumpkin square
pumpkin_width = 6

use_water = True
entity = Entities.Pumpkin
ground = Grounds.Soil

if pumpkin_width > get_world_size():
	pumpkin_width = get_world_size()

loop_condition = True
move_east = True
move_north = True

tiles = []

x_start = get_pos_x()
y_start = get_pos_y()

while loop_condition:
	
	# planting section

	for y in range(pumpkin_width):
		for x in range(pumpkin_width):
			one_to_rule_them_all.plant_smth(entity, ground, use_water)
			if x < pumpkin_width - 1:
				one_to_rule_them_all.move_if(move_east, East, West)
			else:
				move_east = not move_east
		if y < pumpkin_width - 1:
			one_to_rule_them_all.move_if(move_north, North, South)
		else:
			move_north = not move_north

	# checking section

	one_to_rule_them_all.go_to(x_start, y_start)

	# clear the states
	move_east = True
	move_north = True

	for y in range(pumpkin_width):
		for x in range(pumpkin_width):
			if not can_harvest():
				x_pos = get_pos_x()
				y_pos = get_pos_y()
				tiles.append((x_pos, y_pos))
			if x < pumpkin_width - 1:
				one_to_rule_them_all.move_if(move_east, East, West)
			else:
				move_east = not move_east
		if y < pumpkin_width - 1:
			one_to_rule_them_all.move_if(move_north, North, South)
		else:
			move_north = not move_north

	# clear the states
	move_east = True
	move_north = True

	# replanting section

	# TODO sort the tiles list, by adding x and y together
	# to get amount of movements needed from starting position.
	# It actually might be useless, when drone is moving around
	# and going from its current position. It doesn' go back to
	# starting position between the replanting tiles.

	while tiles.len() != 0:
		for pos in tiles:
			x_cord, y_cord = pos
			one_to_rule_them_all.go_to(x_cord, y_cord)
			if not can_harvest():
				one_to_rule_them_all.plant_smth(entity, ground, use_water)
			else:
				tiles.remove(pos)
	
	# harvesting section

	one_to_rule_them_all.go_to(x_start, y_start)
	harvest()