# get pos x and y
# plant
# get companion type and position
# go to companion position
# plant companion
# get companion2 type and position
# go back to original plant
# harvest
# go to companion2 position
# plant companion2
# get companion3 type and position
# ...

import one_to_rule_them_all

clear()

entities = [
	Entities.Bush,
	Entities.Carrot,
	Entities.Grass,
	Entities.Tree
]

use_water = True

# Randomize entity for the first plant
index = random() * len(entities) // 1
entity = entities[index]
ground = Grounds.Soil

# get pos x and y
original_x = get_pos_x()
original_y = get_pos_y()

while True:
	# plant
	one_to_rule_them_all.plant_smth(entity, ground, use_water)
	
	# get companion type and position
	companion = get_companion()
	quick_print(companion)
	entity, (companion_x, companion_y) = companion

	# go to companion position
	one_to_rule_them_all.go_to(companion_x, companion_y)
	
	# plant companion
	one_to_rule_them_all.plant_smth(entity, ground, use_water)
	
	# get companion2 type and position
	companion = get_companion()
	quick_print(companion)
	entity, (second_comp_x, second_comp_y) = companion

	# go back to original plant
	one_to_rule_them_all.go_to(original_x, original_y)

	# harvest
	while not can_harvest():
		do_a_flip()

	harvest()

	original_x = companion_x
	original_y = companion_y

	# go to companion2 position
	one_to_rule_them_all.go_to(second_comp_x, second_comp_y)