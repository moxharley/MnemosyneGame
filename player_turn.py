import room, logic, sys, sequence, time, pygame


def ship_map():
    """
    Output star-ship map layout.
    """
    sequence.output('>\n> [\033[31mARCHANGEL\033[0m] DATA: Starship layout initializing.', True, 0.02)
    sequence.output('> -------------------------------------', True, 0.01)
    sequence.output('>    ┌───────┐  ┌──────┐  ┌───────┐', True, 0.01)
    sequence.output('>    │Medical├──┼Galley┼──┤Loading│', True, 0.01)
    sequence.output('>    │ Bay   │  └──┬┬──┘  │ Bay   │', True, 0.01)
    sequence.output('>    └──┬┬───┘  ┌──┴┴──┐  └───┬┬──┘', True, 0.01)
    sequence.output('>    ┌──┴┴────┐ │Bridge│  ┌───┴┴──┐', True, 0.01)
    sequence.output('>    │Crew    │ └──┬┬──┘  │Stasis │', True, 0.01)
    sequence.output('>    │Quarters│    ││     │ Pods  │', True, 0.01)
    sequence.output('>    └────────┘    ││     └───────┘', True, 0.01)
    sequence.output('>             ┌────┴┴─────┐', True, 0.01)
    sequence.output('>             │Maintenance│', True, 0.01)
    sequence.output('>             │ Access    │', True, 0.01)
    sequence.output('>             └────┬┬─────┘', True, 0.01)
    sequence.output('>      ┌─────┐ ┌───┴┴───┐ ┌───────┐', True, 0.01)
    sequence.output('>      │Relay├─┤Reactors├─┤Utility│', True, 0.01)
    sequence.output('>      └─────┘ └───┬┬───┘ └───────┘', True, 0.01)
    sequence.output('>             ┌────┴┴─────┐', True, 0.01)
    sequence.output('>             │Fabrication│', True, 0.01)
    sequence.output('>             │ Bay       │', True, 0.01)
    sequence.output('>             └────┬┬─────┘', True, 0.01)
    sequence.output('>              ┌───┴┴────┐', True, 0.01)
    sequence.output('>              │Emergency│', True, 0.01)
    sequence.output('>              │Pod Bay  │', True, 0.01)
    sequence.output('>              └─────────┘', True, 0.01)
    sequence.output('> -------------------------------------', True, 0.01)


def look(board, character):
    """
    Player looks.

    Prints details about player's current location.

    :param board: a dictionary.
    :param character: a dictionary.
    :precondition: board must be a well-formed board dictionary.
    :precondition: character must be a well-formed character dictionary.
    :postcondition: checks the player's current tile and displays environmental details.

    >>> pygame.mixer.pre_init(frequency=44100, size=-16, channels=4, buffer=512)
    >>> pygame.mixer.init()
    >>> pygame.mixer.set_num_channels(4)
    >>> example_board = {(0, 0): ["Test Description", "Room"], (1, 0): ["Test Description", "Other Room"]}
    >>> example_character = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> look(example_board, example_character)
    >
    > [[31mARCHANGEL[0m] ENVIRONMENT: Telemetry scan initialized.
    > [32m[telemetry synced][0m
    > ------------------------
    > [4mCOORDINATES:[0m
    > Position..........(0, 0)
    > Room..............Room
    >
    > [4mSURROUNDINGS:[0m
    > Test Description
    >
    > [4mACCESS:[0m
    > Available Routes...east, 
    > ------------------------
    >>> pygame.mixer.pre_init(frequency=44100, size=-16, channels=4, buffer=512)
    >>> pygame.mixer.init()
    >>> pygame.mixer.set_num_channels(4)
    >>> example_board = {(0, 0): ["Test Description", "Room"], (1, 0): ["Test Description", "Other Room"]}
    >>> example_character = {'X-coordinate': 1, 'Y-coordinate': 0}
    >>> look(example_board, example_character)
    >
    > [[31mARCHANGEL[0m] ENVIRONMENT: Telemetry scan initialized.
    > [32m[telemetry synced][0m
    > ------------------------
    > [4mCOORDINATES:[0m
    > Position..........(1, 0)
    > Room..............Other Room
    >
    > [4mSURROUNDINGS:[0m
    > Test Description
    >
    > [4mACCESS:[0m
    > Available Routes...west, 
    > ------------------------
    """
    sequence.output('>\n> [\033[31mARCHANGEL\033[0m] ENVIRONMENT: Telemetry scan initialized.', True, 0.01)
    sequence.output('> \033[32m[telemetry synced]\033[0m', True, 0.01)
    sequence.output('> ------------------------', True, 0.01)
    sequence.output('> \033[4mCOORDINATES:\033[0m', True, 0.01)
    character_coordinates = (character["X-coordinate"], character["Y-coordinate"])
    sequence.output(f'> Position..........{character_coordinates}', True, 0.01)
    sequence.output(f'> Room..............{board[character_coordinates][1]}\n>', True, 0.01)
    sequence.output('> \033[4mSURROUNDINGS:\033[0m', True, 0.01)
    room.describe_current_location(board, character)
    sequence.output('>', True, 0.01)

    can_north = logic.validate_move(board, character, 'n')
    can_east = logic.validate_move(board, character, 'e')
    can_south = logic.validate_move(board, character, 's')
    can_west = logic.validate_move(board, character, 'w')

    sequence.output('> \033[4mACCESS:\033[0m', True, 0.01)
    sequence.output('> Available Routes...', False, 0.01)
    if can_north:
        sequence.output('north, ', False, 0.01)
    if can_east:
        sequence.output('east, ', False, 0.01)
    if can_south:
        sequence.output('south, ', False, 0.01)
    if can_west:
        sequence.output('west, ', False, 0.01)
    sys.stdout.write('\b\b\n')
    sequence.output('> ------------------------', True, 0.01)


def make_bar(current):
    """
    Make health or energy bar.

    Displays health or energy in a progress-bar form.

    :param current: an integer variable.
    :precondition: current must be between (or including) 0 and 10
    :postcondition: renders a progress bar of your current HP or EP
    :return: a string variable.
    """
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
    """
    Player status.

    Displays player status information.

    :param character: a dictionary
    :precondition: character must be a well-formed character dictionary.
    :postcondition: outputs character details.

    >>> example_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'first-name': 'First', 'last-name': 'Last', 'current-HP': 5, 'current-EP': 5, 'room': 'Stasis-Pods', 'exp': 0, 'class': 'Technomancer', 'end': 0, 'int': 0, 'inf': 0, 'eng': 0, 'inventory': ['Empty', 'Empty', 'Empty', 'Empty']}
    >>> status(example_character)
    >
    > [VEIL-9] STATUS: Process initiated.
    > \033[32m[bioscan complete]\033[0m
    > ------------------------
    > \033[4mIDENTITY:\033[0m
    > Name...............First
    > Designation........Technomancer
    >
    > \033[4mVITALS:\033[0m
    > Health..........[\033[33m█████░░░░░\033[0m] 50.0%
    > Energy..........[\033[33m█████░░░░░\033[0m] 50.0%
    >
    > \033[4mATTRIBUTES:\033[0m
    > Endure...........[0]
    > Engage...........[0]
    > Interface........[0]
    > Intuit...........[0]
    >
    > \033[4mINVENTORY:\033[0m
    > Slot_1.........Empty
    > Slot_2.........Empty
    > Slot_3.........Empty
    > Slot_4.........Empty
    > ------------------------
    >>> example_character = {'X-coordinate': -1, 'Y-coordinate': -1, 'first-name': 'First', 'last-name': 'Last', 'current-HP': 4, 'current-EP': 6, 'room': 'Corridor', 'exp': 0, 'class': 'Freighter', 'end': 1, 'int': -1, 'inf': 0, 'eng': 0, 'inventory': ['Heavy-Wrench', 'Empty', 'Empty', 'Empty']}
    >>> status(example_character)
    >
    > [VEIL-9] STATUS: Process initiated.
    > \033[32m[bioscan complete]\033[0m
    > ------------------------
    > \033[4mIDENTITY:\033[0m
    > Name...............First
    > Designation........Freighter
    >
    > \033[4mVITALS:\033[0m
    > Health..........[\033[33m████░░░░░░\033[0m] 40.0%
    > Energy..........[\033[33m██████░░░░\033[0m] 60.0%
    >
    > \033[4mATTRIBUTES:\033[0m
    > Endure...........[1]
    > Engage...........[0]
    > Interface........[0]
    > Intuit...........[-1]
    >
    > \033[4mINVENTORY:\033[0m
    > Slot_1.........Heavy-Wrench
    > Slot_2.........Empty
    > Slot_3.........Empty
    > Slot_4.........Empty
    > ------------------------
    """
    sequence.output('>\n> [VEIL-9] STATUS: Process initiated.', True, 0.01)
    sequence.output('> \033[32m[bioscan complete]\033[0m', True, 0.01)
    sequence.output('> ------------------------', True, 0.01)
    sequence.output('> \033[4mIDENTITY:\033[0m', True, 0.01)
    sequence.output(f'> Name...............{character['first-name']}', True, 0.01)
    sequence.output(f'> Designation........{character['class']}\n>', True, 0.01)

    health = make_bar(character['current-HP'])
    energy = make_bar(character['current-EP'])

    health_percent = (character['current-HP'] / 10) * 100
    energy_percent = (character['current-EP'] / 10) * 100

    sequence.output('> \033[4mVITALS:\033[0m', True, 0.01)
    sequence.output(f'> Health..........{health} {health_percent}%', True, 0.01)
    sequence.output(f'> Energy..........{energy} {energy_percent}%\n>', True, 0.01)
    sequence.output('> \033[4mATTRIBUTES:\033[0m', True, 0.01)
    sequence.output(f'> Endure...........[{character['end']}]', True, 0.01)
    sequence.output(f'> Engage...........[{character['eng']}]', True, 0.01)
    sequence.output(f'> Interface........[{character['inf']}]', True, 0.01)
    sequence.output(f'> Intuit...........[{character['int']}]\n>', True, 0.01)
    sequence.output('> \033[4mINVENTORY:\033[0m', True, 0.01)
    sequence.output(f'> Slot_1.........{character['inventory'][0]}', True, 0.01)
    sequence.output(f'> Slot_2.........{character['inventory'][1]}', True, 0.01)
    sequence.output(f'> Slot_3.........{character['inventory'][2]}', True, 0.01)
    sequence.output(f'> Slot_4.........{character['inventory'][3]}', True, 0.01)
    sequence.output('> ------------------------', True, 0.01)


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

    >>> pygame.mixer.pre_init(frequency=44100, size=-16, channels=4, buffer=512)
    >>> pygame.mixer.init()
    >>> pygame.mixer.set_num_channels(4)
    >>> move({'X-coordinate': 0, 'Y-coordinate': 0}, 'n')
    >
    > [\033[31mARCHANGEL\033[0m] MOVEMENT: north-ward movement confirmed.
    {'X-coordinate': 0, 'Y-coordinate': 1}
    >>> pygame.mixer.pre_init(frequency=44100, size=-16, channels=4, buffer=512)
    >>> pygame.mixer.init()
    >>> pygame.mixer.set_num_channels(4)
    >>> move({'X-coordinate': 0, 'Y-coordinate': 0}, 'e')
    >
    > [\033[31mARCHANGEL\033[0m] MOVEMENT: east-ward movement confirmed.
    {'X-coordinate': 1, 'Y-coordinate': 0}
    """
    north = ('n', 'N')
    east = ('e', 'E')
    south = ('s', 'S')
    west = ('w', 'W')
    if direction in north:
        character["Y-coordinate"] += 1
        sequence.output('>\n> [\033[31mARCHANGEL\033[0m] MOVEMENT: north-ward movement confirmed.',True, 0.03)
    elif direction in east:
        character["X-coordinate"] += 1
        sequence.output('>\n> [\033[31mARCHANGEL\033[0m] MOVEMENT: east-ward movement confirmed.', True, 0.03)
    elif direction in south:
        character["Y-coordinate"] -= 1
        sequence.output('>\n> [\033[31mARCHANGEL\033[0m] MOVEMENT: south-ward movement confirmed.', True, 0.03)
    elif direction in west:
        character["X-coordinate"] -= 1
        sequence.output('>\n> [\033[31mARCHANGEL\033[0m] MOVEMENT: west-ward movement confirmed.', True, 0.03)
    return character


def interact(interacts, character):
    """
    Player interacts.

    Checks for interactable and executes interactable if it exists.

    :param interacts: a dictionary.
    :param character: a dictionary.
    :precondition: interacts must be a well-formed interacts dictionary.
    :precondition: character must be a well-formed character dictionary.
    :postcondition: checks if there is an interactable, then calls the interactable function and removes it.
    :return: a dictionary.
    """
    sequence.output("> ", True)
    character_coordinates = (character["X-coordinate"], character["Y-coordinate"])
    if character_coordinates in interacts:
        interacts[character_coordinates](character)
        del interacts[character_coordinates]
    else:
        sequence.output('> INVALID INPUT: There is nothing to interact with')
        time.sleep(1)
        sys.stdout.write('\r')
        sequence.output('>> ')
    return character