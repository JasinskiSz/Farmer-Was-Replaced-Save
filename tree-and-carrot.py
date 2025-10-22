clear()

first_run = True

def get_boolean_number(isEven):
    if isEven:
        return 1
    return 0

def reverse_boolean(isEven):
    if isEven:
        return get_boolean_number(isEven)
    return get_boolean_number(isEven)

def column_movement(isEven):
    number = reverse_boolean(isEven)

    for i in range(get_world_size()):
        if can_harvest():
            harvest()
        if get_pos_y() % 2 == number:
            plant(Entities.Tree)
        else:
            till()
            plant(Entities.Carrot)

        move(North)

def column_movement_no_till(isEven):
    number = reverse_boolean(isEven)

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
        isEven = get_pos_x() % 2 == 0
        column_movement(isEven)
        move(East)
    
    first_run = False

while not first_run:
    isEven = get_pos_x() % 2 == 0
    column_movement_no_till(isEven)
    move(East)