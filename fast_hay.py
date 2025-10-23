# To plant hay and sunflower every so often
# Goal is to get faster

import one_to_rule_them_all

def flip_flag(bool):
	return not bool

clear()

# max x and y coords to reach
x_boundary = 6
y_boundary = 6

move_north = True
move_east = True

while True:
	# North boundary
	for i in range(y_boundary):
		# move_south = move_north
		# if i == 0:
			# move_south = not move_north
		for j in range(x_boundary):
			if move_east:
				move(East)
			else:
				move(West)
		move_east = not move_east
		if move_north:
			move(North)
		else:
			move(South)
	move_north = not move_north