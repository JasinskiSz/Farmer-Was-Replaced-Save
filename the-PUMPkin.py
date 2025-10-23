import one_to_rule_them_all

clear()

# width of the pumpkin square
pumpkin_width = 1

should_water_plants = True
entity = Entities.Pumpkin
ground = Grounds.Soil

desired_pumpkin_size = 6

if desired_pumpkin_size > get_world_size():
	desired_pumpkin_size = get_world_size()

while True:
	one_to_rule_them_all.plant_smth(entity, ground, should_water_plants)

	for i in range(pumpkin_width-1):
		one_to_rule_them_all.move_and_plant(entity, ground, North, should_water_plants)
	for i in range(pumpkin_width-1):
		one_to_rule_them_all.move_and_plant(entity, ground, West, should_water_plants)
	for i in range(pumpkin_width-1):
		move(South)

	# if last world block is reached,
	# harvest and reset the loop
	if pumpkin_width == desired_pumpkin_size:
		harvest()
		pumpkin_width = 0

	# goes to next starting position
	for i in range(pumpkin_width):
		move(East)

	pumpkin_width += 1