clear()

def get_boolean_number(is_even):
    if is_even:
        return 1
    return 0

def column_movement(is_even, should_till):
    number = get_boolean_number(is_even)

    for i in range(get_world_size()):
        if can_harvest():
            harvest()
        if get_pos_y() % 2 == number:
            plant(Entities.Tree)
        else:
            if should_till:
                till()
            plant(Entities.Carrot)

        move(North)

first_run = True
counter = 0

while True:
    is_column_even = get_pos_x() % 2 == 0

    column_movement(is_column_even, first_run)
    move(East)

    if first_run:
        counter += 1
        if get_world_size() == counter:
            first_run = False
