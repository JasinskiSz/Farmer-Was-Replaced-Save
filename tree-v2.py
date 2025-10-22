clear()

def harvest_column_grass():
	for j in range(get_world_size()):
		if get_entity_type() == Entities.Grass:
			harvest()
		move(North)
	return

def get_modulo_number(isEven):
	number = 0 
	if not isEven:
		number = 1
	return number

def plant_column(isEven):
	number = get_modulo_number(isEven)
	
	for j in range(get_world_size()):
		if get_pos_y() % 2 == number:
			plant(Entities.Tree)
		move(North)
		
def harvest_column(isEven):
	number = get_modulo_number(isEven)
	
	for j in range(get_world_size()):
		if get_pos_y() % 2 == number:
			harvested = False
			while not harvested:
				if can_harvest():
					harvest()
					harvested = True
				else:
					harvest_column_grass()
		move(North)

first_run = True
cols_completed = 0
world_size = get_world_size()

while True:
	while first_run:
		isEven = get_pos_x() % 2 == 0
		plant_column(isEven)
		move(East)
		cols_completed += 1
		if world_size == cols_completed:
			first_run = False
			cols_completed = 0
	
	while not first_run:
		isEven = get_pos_x() % 2 == 0
		harvest_column(isEven)
		move(East)
		cols_completed += 1
		if world_size == cols_completed:
			first_run = True
			cols_completed = 0