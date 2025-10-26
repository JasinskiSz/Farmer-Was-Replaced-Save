import one_to_rule_them_all

def check():
	x, y = get_pos_x(), get_pos_y()
	return {(x,y):can_harvest()}

def repair_pumpkin(dict, entity, ground, use_water):
	ready = True
	for key in dict:
		if not dict[key]:
			x, y = key
			one_to_rule_them_all.go_to(x, y)
			one_to_rule_them_all.plant_smth(entity, ground, use_water)
			ready = False
	one_to_rule_them_all.go_to_start()
	return ready

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

now_plant = True
now_check = False
now_harvest = False

check_dict = {}

counter = 0
pumpkin_squared = pumpkin_width * pumpkin_width

while loop_condition:
	for y in range(pumpkin_width):
		for x in range(pumpkin_width):
			if now_plant and x < pumpkin_width - 1:
				one_to_rule_them_all.plant_and_move_if(entity, ground, move_east, East, West, use_water)
			elif now_plant:
				one_to_rule_them_all.plant_smth(entity, ground, use_water)
				move_east = not move_east
			elif now_check:
				if counter == pumpkin_squared:
					if repair_pumpkin(check_dict, entity, ground, use_water):
						now_check = False
						now_harvest = True
					counter = 0
				else:
					counter += 1
					quick_print("Should add to dict")
					check_dict = {(x,y):can_harvest()}
			elif now_harvest:
				do_a_flip()
		if y < pumpkin_width - 1:
			one_to_rule_them_all.move_if(move_north, North, South)
		else:
			move_north = not move_north

	if now_plant:
		now_plant = False
		now_check = True