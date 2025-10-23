import one_to_rule_them_all

# moving in a square script

clear()

# width of the square
n = 1

should_water_plants = True
entity = Entities.Pumpkin
ground = Grounds.Soil

desired_pumpkin_size = 6

if desired_pumpkin_size > get_world_size():
	desired_pumpkin_size = get_world_size()

while True:
	one_to_rule_them_all.plant_smth(entity, ground, should_water_plants)

	for i in range(n-1):
		one_to_rule_them_all.move_and_plant(entity, ground, North, should_water_plants)
	for i in range(n-1):
		one_to_rule_them_all.move_and_plant(entity, ground, West, should_water_plants)
	for i in range(n-1):
		move(South)

	if n >= 2:
		is_big_pumpkin = False
		while not is_big_pumpkin:
			is_grown = []
			if not can_harvest():
				one_to_rule_them_all.plant_smth(entity, ground, should_water_plants)
				is_grown.append(False)
			else:
				is_grown.append(True)

			for i in range(n-1):
				move(East)
				if not can_harvest():
					one_to_rule_them_all.plant_smth(entity, ground, should_water_plants)
					is_grown.append(False)
				else:
					is_grown.append(True)


			for i in range(n-1):
				move(North)
				if not can_harvest():
					one_to_rule_them_all.plant_smth(entity, ground, should_water_plants)
					is_grown.append(False)
				else:
					is_grown.append(True)
				
			for i in range(n-1):
				move(West)
				if not can_harvest():
					one_to_rule_them_all.plant_smth(entity, ground, should_water_plants)
					is_grown.append(False)
				else:
					is_grown.append(True)
			
			for i in range(n-1):
				move(South)
			
			for is_completed in is_grown:
				if not is_completed:
					is_big_pumpkin = False
					break
				else:
					is_big_pumpkin = True

	# if last world block is reached,
	# harvest and reset the loop
	if n == desired_pumpkin_size:
		harvest()
		n = 0

	# goes to next starting position
	for i in range(n):
		move(East)

	n += 1