import one_to_rule_them_all

one_to_rule_them_all.go_to_start()

entity = Entities.Carrot
ground = Grounds.Soil
shouldWater = True

move_north = True
move_east = True

farm_limit = 6
should_plant_sunflowers = False

max_farm = False
world_size = get_world_size()

if farm_limit > world_size:
	farm_limit = world_size

if farm_limit == world_size:
	max_farm = True

minimum_farm_size = 30
if should_plant_sunflowers == True and farm_limit * farm_limit >= minimum_farm_size:
	should_plant_sunflowers = True
	print("Farm size is not big enough for sunflowers")
else:
	should_plant_sunflowers = False

sunflower_count = 0
max_sunflower = 10

while True:
	# moving over Y axis
	for i in range(farm_limit):
		# moving over X axis
		for j in range(farm_limit):
			entityType = get_entity_type()
			# TODO this will harvest everything
			if can_harvest():
				harvest()
				if entityType == Entities.Sunflower:
					sunflower_count -= 1
			if sunflower_count < max_sunflower:
				one_to_rule_them_all.plant_smth(Entities.Sunflower, Grounds.Soil, shouldWater)
				sunflower_count += 1
			else:
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