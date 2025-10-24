clear()

first_run = True
cols_completed = 0
world_size = get_world_size()

while first_run:
	for j in range(get_world_size()):
		harvest()
		till()
		plant(Entities.Carrot)
		move(North)
	move(East)
	cols_completed += 1
	if world_size == cols_completed:
		break
	
first_run = False

while not first_run:
	for i in range(get_world_size()):
		while not can_harvest():
			do_a_flip()	
		harvest()
		plant(Entities.Carrot)
		move(North)
	move(East)