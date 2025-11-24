import room, logic, sys, scene_sequence, time


def ship_map():
    scene_sequence.output('>\n> [\033[31mARCHANGEL\033[0m] DATA: Starship layout initializing.', True, 0.02)
    scene_sequence.output('> -------------------------------------', True, 0.02)
    scene_sequence.output('>    ┌───────┐  ┌──────┐  ┌───────┐', True, 0.02)
    scene_sequence.output('>    │Medical├──┼Galley┼──┤Loading│', True, 0.02)
    scene_sequence.output('>    │ Bay   │  └──┬┬──┘  │ Bay   │', True, 0.02)
    scene_sequence.output('>    └──┬┬───┘  ┌──┴┴──┐  └───┬┬──┘', True, 0.02)
    scene_sequence.output('>    ┌──┴┴────┐ │Bridge│  ┌───┴┴──┐', True, 0.02)
    scene_sequence.output('>    │Crew    │ └──┬┬──┘  │Stasis │', True, 0.02)
    scene_sequence.output('>    │Quarters│    ││     │ Pods  │', True, 0.02)
    scene_sequence.output('>    └────────┘    ││     └───────┘', True, 0.02)
    scene_sequence.output('>             ┌────┴┴─────┐', True, 0.02)
    scene_sequence.output('>             │Maintenance│', True, 0.02)
    scene_sequence.output('>             │ Access    │', True, 0.02)
    scene_sequence.output('>             └────┬┬─────┘', True, 0.02)
    scene_sequence.output('>      ┌─────┐ ┌───┴┴───┐ ┌───────┐', True, 0.02)
    scene_sequence.output('>      │Relay├─┤Reactors├─┤Utility│', True, 0.02)
    scene_sequence.output('>      └─────┘ └───┬┬───┘ └───────┘', True, 0.02)
    scene_sequence.output('>             ┌────┴┴─────┐', True, 0.02)
    scene_sequence.output('>             │Fabrication│', True, 0.02)
    scene_sequence.output('>             │ Bay       │', True, 0.02)
    scene_sequence.output('>             └────┬┬─────┘', True, 0.02)
    scene_sequence.output('>              ┌───┴┴────┐', True, 0.02)
    scene_sequence.output('>              │Emergency│', True, 0.02)
    scene_sequence.output('>              │Pod Bay  │', True, 0.02)
    scene_sequence.output('>              └─────────┘', True, 0.02)
    scene_sequence.output('> -------------------------------------', True, 0.02)
    scene_sequence.output('> ', True, 0.02)


def look(board, character):
    scene_sequence.output('>\n> [\033[31mARCHANGEL\033[0m] ENVIRONMENT: Telemetry scan initialized.', True, 0.03)
    scene_sequence.output('> \033[32m[telemetry synced]\033[0m', True, 0.03)
    scene_sequence.output('> ------------------------ ', True, 0.03)
    scene_sequence.output('> \033[4mCOORDINATES:\033[0m', True, 0.03)
    scene_sequence.output(f'> Position..........({character['X-coordinate']}, {character['Y-coordinate']})', True, 0.03)
    scene_sequence.output(f'> Room..............{character['room']}\n> ', True, 0.03)
    scene_sequence.output('> \033[4mSURROUNDINGS:\033[0m', True, 0.03)
    room.describe_current_location(board, character)
    scene_sequence.output('> ', True, 0.03)

    can_north = logic.validate_move(board, character, 'n')
    can_east = logic.validate_move(board, character, 'e')
    can_south = logic.validate_move(board, character, 's')
    can_west = logic.validate_move(board, character, 'w')

    scene_sequence.output('> \033[4mACCESS:\033[0m', True, 0.03)
    scene_sequence.output('> Available Routes...', False, 0.03)
    if can_north:
        scene_sequence.output('north, ')
    if can_east:
        scene_sequence.output('east, ')
    if can_south:
        scene_sequence.output('south, ')
    if can_west:
        scene_sequence.output('west, ')
    sys.stdout.write('\b\b\n')
    scene_sequence.output('> ------------------------ ', True, 0.03)


def make_bar(current):
    filled = ''
    empty = ''
    for index in range(0, current):
        filled += '█'
    for index in range(0, (10 - current)):
        empty += '░'

    if current >= 8:
        bar = '[\033[32m' + filled + empty + '\033[0m]'
    elif current >= 4:
        bar = '[\033[33m' + filled + empty + '\033[0m]'
    else:
        bar = '[\033[31m' + filled + empty + '\033[0m]'
    return bar


def status(character):
    scene_sequence.output('>\n> [VEIL-9] STATUS: Process initiated.', True, 0.03)
    scene_sequence.output('> \033[32m[bioscan complete]\033[0m', True, 0.03)
    scene_sequence.output('> ------------------------', True, 0.03)
    scene_sequence.output('> \033[4mIDENTITY:\033[0m', True, 0.03)
    scene_sequence.output(f'> Name...............{character['first-name']}', True, 0.03)
    scene_sequence.output(f'> Designation........{character['class']}\n> ', True, 0.03)

    health = make_bar(character['current-HP'])
    energy = make_bar(character['current-EP'])

    health_percent = (character['current-HP'] / 10) * 100
    energy_percent = (character['current-EP'] / 10) * 100

    scene_sequence.output('> \033[4mVITALS:\033[0m', True, 0.03)
    scene_sequence.output(f'> Health..........{health} {health_percent}%', True, 0.03)
    scene_sequence.output(f'> Energy..........{energy} {energy_percent}%\n> ', True, 0.03)
    scene_sequence.output('> \033[4mATTRIBUTES:\033[0m', True, 0.03)
    scene_sequence.output(f'> Endure...........[{character['end']}]', True, 0.03)
    scene_sequence.output(f'> Engage...........[{character['eng']}]', True, 0.03)
    scene_sequence.output(f'> Interface........[{character['inf']}]', True, 0.03)
    scene_sequence.output(f'> Intuit...........[{character['int']}]\n> ', True, 0.03)
    scene_sequence.output('> \033[4mINVENTORY:\033[0m', True, 0.03)
    scene_sequence.output(f'> Slot_1.........{character['inventory'][0]}', True, 0.03)
    scene_sequence.output(f'> Slot_2.........{character['inventory'][1]}', True, 0.03)
    scene_sequence.output(f'> Slot_3.........{character['inventory'][2]}', True, 0.03)
    scene_sequence.output(f'> Slot_4.........{character['inventory'][3]}', True, 0.03)
    scene_sequence.output('> ------------------------ ', True, 0.03)


def move(character, direction):
    """
    Move character coordinates.

    Adjusts character x and y coordinates based off of movement direction.

    :param character: a dictionary.
    :param direction: a single character string.
    :precondition: direction must be 'n', 'N', 'e', 'E', 's', 'S', 'w' or 'W'
    :precondition: character must be a dictionary with a "Y-coordinate" and "X-coordinate" key.
    :precondition: character["Y-coordinate"] and character["X-coordinate"] must be integers.
    :postcondition: adjusts character dictionary using movement direction.
    :return: updated character dictionary.
    """
    north = ('n', 'N')
    east = ('e', 'E')
    south = ('s', 'S')
    west = ('w', 'W')
    if direction in north:
        character["Y-coordinate"] += 1
        scene_sequence.output('>\n> [\033[31mARCHANGEL\033[0m] MOVEMENT: north-ward movement confirmed.',True)
    elif direction in east:
        character["X-coordinate"] += 1
        scene_sequence.output('>\n> [\033[31mARCHANGEL\033[0m] MOVEMENT: east-ward movement confirmed.', True)
    elif direction in south:
        character["Y-coordinate"] -= 1
        scene_sequence.output('>\n> [\033[31mARCHANGEL\033[0m] MOVEMENT: south-ward movement confirmed.', True)
    elif direction in west:
        character["X-coordinate"] -= 1
        scene_sequence.output('>\n> [\033[31mARCHANGEL\033[0m] MOVEMENT: west-ward movement confirmed.', True)
    return character


def interact(interacts, character):
    scene_sequence.output("> ", True)
    character_coordinates = (character["X-coordinate"], character["Y-coordinate"])
    if character_coordinates in interacts:
        character = interacts[character_coordinates](character)
    else:
        scene_sequence.output('> INVALID INPUT: There is nothing to interact with')
        time.sleep(1)
        sys.stdout.write('\r')
        scene_sequence.output('>> ')
    return character