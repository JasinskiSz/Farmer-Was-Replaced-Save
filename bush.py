clear()

while True:
	for i in range(get_world_size()):
		harvest()
		plant(Entities.Bush)
		move(North)
	move(East)