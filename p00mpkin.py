# moving in a square script

clear()

# width of the square
n = 1

def plant_pumpkin(water):
	if get_ground_type() == Grounds.Grassland:
		till()
	plant(Entities.Pumpkin)
	if water and get_water() < 0.75:
		use_item(Items.Water)

def move_and_plant(direction, water):
	move(direction)
	plant_pumpkin(water)

while True:

	plant_pumpkin(True)

	for i in range(n-1):
		move_and_plant(North, True)
	for i in range(n-1):
		move_and_plant(West, True)
	for i in range(n-1):
		move(South)

	if n >= 2:
		is_big_pumpkin = False
		while not is_big_pumpkin:
			is_grown = []
			if not can_harvest():
				plant_pumpkin(True)
				is_grown.append(False)
			else:
				is_grown.append(True)

			for i in range(n-1):
				move(East)
				if not can_harvest():
					plant_pumpkin(True)
					is_grown.append(False)
				else:
					is_grown.append(True)


			for i in range(n-1):
				move(North)
				if not can_harvest():
					plant_pumpkin(True)
					is_grown.append(False)
				else:
					is_grown.append(True)
				
			for i in range(n-1):
				move(West)
				if not can_harvest():
					plant_pumpkin(True)
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
	if n == get_world_size():
		harvest()
		n = 0

	# goes to next starting position
	for i in range(n):
		move(East)

	n += 1