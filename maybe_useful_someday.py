def run_in_square_and_back(x_boundary, y_boundary, move_north, move_east):
	# max x and y coords to reach
	# x_boundary = 6
	# y_boundary = 6

	# move_north = True
	# move_east = True

	while True:
		for i in range(y_boundary):
			for j in range(x_boundary):
				if move_east:
					move(East)
				else:
					move(West)
			# flip flag when reached
			# end of the row
			move_east = not move_east
			if move_north:
				move(North)
			else:
				move(South)
		# flip flag when reached
		# end of the column 
		move_north = not move_north