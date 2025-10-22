clear()

first_run = True

def get_boolean_number(is_even):
    if is_even:
        return 1
    return 0

def reverse_boolean(is_even):
    if is_even:
        return get_boolean_number(is_even)
    return get_boolean_number(is_even)

def column_movement(is_even):
    number = reverse_boolean(is_even)

    for i in range(get_world_size()):
        if can_harvest():
            harvest()
        if get_pos_y() % 2 == number:
            plant(Entities.Tree)
        else:
            till()
            plant(Entities.Carrot)

        move(North)

def column_movement_no_till(is_even):
    number = reverse_boolean(is_even)

    for i in range(get_world_size()):
        if can_harvest():
            harvest()
        if get_pos_y() % 2 == number:
            plant(Entities.Tree)
        else:
            plant(Entities.Carrot)

        move(North)

while first_run:
    for i in range(get_world_size()):
        is_even = get_pos_x() % 2 == 0
        column_movement(is_even)
        move(East)
    
    first_run = False

while not first_run:
    is_even = get_pos_x() % 2 == 0
    column_movement_no_till(is_even)
    move(East)