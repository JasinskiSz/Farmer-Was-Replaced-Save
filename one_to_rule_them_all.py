def plant_smth(entity, entity_ground_type, water):
	if get_ground_type() != entity_ground_type:
		till()
	plant(entity)
	if water and get_water() < 0.75:
		use_item(Items.Water)

def move_and_plant(entity, ground, direction, water):
	move(direction)
	plant_smth(entity, ground, water)