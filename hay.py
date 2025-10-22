clear()

while True:
	for i in range(get_world_size()):
		while not can_harvest():
			do_a_flip()
		harvest()
		move(North)
		
	move(East)