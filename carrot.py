import one_to_rule_them_all

clear()

entity = Entities.Carrot
ground = Grounds.Soil
shouldWater = False

move_north = True
move_east = True

farm_limit = 6
max_farm = False
world_size = get_world_size()

if farm_limit > world_size:
	farm_limit = world_size

if farm_limit == world_size:
	max_farm = True

while True:
	# moving over Y axis
	for i in range(farm_limit):
		# moving over X axis
		for j in range(farm_limit):
			if can_harvest():
				harvest()
			one_to_rule_them_all.plant_smth(entity, ground, shouldWater)

			if j != farm_limit - 1:
				if move_east:
					move(East)
				else:
					move(West)
		if i != farm_limit - 1:
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

	if max_farm:
		if move_north:
			move(North)
		else:
			move(South)
	else:
		for i in range(farm_limit - 1):
			if not move_north:
				move(North)
			else:
				move(South)