import room, logic, sys, scene_sequence

def ship_map(character):
    pass


def look(board, character):
    scene_sequence.output('>\n> [\033[31mARCHANGEL\033[0m] ENVIRONMENT: Telemetry scan initialized.', True)
    scene_sequence.output('> \033[32m[scan complete]\033[0m', True)
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
    scene_sequence.output('> Available Routes... ', False, 0.03)
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
    scene_sequence.output('> ', True, 0.03)

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
    scene_sequence.output('> ', True, 0.03)


def move(character):
    pass

def interact(board, character):
    pass

def hull_integrity(hull):
    pass