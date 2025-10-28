import one_to_rule_them_all

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

quick_print("pumpkin size = " + str(pumpkin_width))

counter = 0

pumpkin_results = []

while loop_condition:
	
	# prepare for calculations

	pumpkins = num_items(Items.Pumpkin)
	time_start = get_time()
	
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
				# one_to_rule_them_all.plant_smth(entity, ground, use_water)
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

	# Calculate output section

	# quick_print("pumpkins was: " + str(pumpkins))
	time_end = get_time()
	time_passed = time_end - time_start

	counter += 1

	quick_print("----------------------------")
	quick_print("Run #" + str(counter))
	quick_print("Took " + str(time_passed) + " seconds")

	pumpkins = num_items(Items.Pumpkin) - pumpkins
	quick_print("pumpkins earned: " + str(pumpkins))

	pumpkins_per_second = pumpkins / time_passed
	pumpkin_results.append(pumpkins_per_second)

	quick_print("pumpkins per second: " + str(pumpkins_per_second))
	quick_print("----------------------------")

	if counter >= 10:
		loop_condition = False

total = 0
for i in pumpkin_results:
	total += i

# TODO First run is biased. It has to till the soil and it takes time.
average_harvest = total / counter

quick_print("Average result: " + str(average_harvest))