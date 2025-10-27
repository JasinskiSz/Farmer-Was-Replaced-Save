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

while loop_condition:
	for y in range(pumpkin_width):
		for x in range(pumpkin_width):
			if x < pumpkin_width - 1:
				one_to_rule_them_all.plant_and_move_if(entity, ground, move_east, East, West, use_water)
			else:
				one_to_rule_them_all.plant_smth(entity, ground, use_water)
				move_east = not move_east
		if y < pumpkin_width - 1:
			one_to_rule_them_all.move_if(move_north, North, South)
		else:
			move_north = not move_north