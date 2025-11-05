import one_to_rule_them_all

clear()

# entities = [
# 	(Entities.Bush, Grounds.Soil),
# 	(Entities.Carrot, Grounds.Soil),
# 	(Entities.Grass, Grounds.Soil),
# 	(Entities.Pumpkin, Grounds.Soil),
# 	(Entities.Sunflower, Grounds.Soil),
# 	(Entities.Tree, Grounds.Soil)
# ]

entities = [
	Entities.Bush,
	Entities.Carrot,
	Entities.Grass,
	Entities.Tree
]

positions = []

use_water = True

# Randomize entity for the first plant
index = random() * len(entities) // 1
entity = entities[index]
ground = Grounds.Soil
previous_position = None

while True:
	position = (get_pos_x(), get_pos_y())
	# plant the entity
	if previous_position != position:
		one_to_rule_them_all.plant_smth(entity, ground, use_water)
		previous_position = position
		positions.append(position)

	# get the companion to plant next
	companion = get_companion()

	# TODO: probably not needed check
	# There is no way to get None here (I think)
	# if companion == None:
	# 	while not can_harvest():
	# 		do_a_flip()
	# 	harvest()
	# else:
	entity, (comapnion_x, companion_y) = companion
	if (comapnion_x, companion_y) == previous_position:
		while not can_harvest():
			do_a_flip()
		harvest()
		x, y = previous_position
		previous_position = positions.remove(previous_position)
	else:
		x, y = (comapnion_x, companion_y)

	one_to_rule_them_all.go_to(x, y)