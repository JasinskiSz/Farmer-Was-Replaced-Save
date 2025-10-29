import one_to_rule_them_all

clear()

x_size = 6
y_size = 6
entity = Entities.Carrot
ground = Grounds.Soil
loop = True
use_water = True
move_north = True
move_east = True

one_to_rule_them_all.farm(x_size, y_size, entity, ground, loop, use_water, move_north, move_east)