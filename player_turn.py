from sequence import output


def look(board, character):
    pass


def make_bar(current):
    filled = ''
    empty = ''
    for index in range(1, current):
        filled += '█'
    for index in range(1, (10 - current)):
        empty += '░'

    if current >= 8:
        bar = '[\033[32m' + filled + empty + '\033[0m]'
    elif current >= 4:
        bar = '[\033[33m' + filled + empty + '\033[0m]'
    else:
        bar = '[\033[31m' + filled + empty + '\033[0m]'
    return bar

def status(character):
    output('>\n> [VEIL-9] STATUS: Process initiated.', True, 0.03)
    output('> \033[32m[bioscan complete]\033[0m', True, 0.03)
    output('> ------------------------', True, 0.03)
    output('> \033[4mIDENTITY:\033[0m', True, 0.03)
    output(f'> Name...............{character['first-name']}', True, 0.03)
    output(f'> Designation........{character['class']}\n> ', True, 0.03)

    health = make_bar(character['current-HP'])
    energy = make_bar(character['current-EP'])

    health_percent = (character['current-HP'] / 10) * 100
    energy_percent = (character['current-EP'] / 10) * 100

    output('> \033[4mVITALS:\033[0m', True, 0.03)
    output(f'> Health........{health} {health_percent}%', True, 0.03)
    output(f'> Energy........{energy} {energy_percent}%\n> ', True, 0.03)
    output('> \033[4mATTRIBUTES:\033[0m', True, 0.03)
    output(f'> Endure...........[{character['end']}]', True, 0.03)
    output(f'> Engage...........[{character['eng']}]', True, 0.03)
    output(f'> Interface........[{character['inf']}]', True, 0.03)
    output(f'> Intuit...........[{character['int']}]\n> ', True, 0.03)
    output('> \033[4mINVENTORY:\033[0m', True, 0.03)
    output(f'> Slot_1......{character['inventory'][0]}', True, 0.03)
    output(f'> Slot_2......{character['inventory'][1]}', True, 0.03)
    output(f'> Slot_3......{character['inventory'][2]}', True, 0.03)
    output(f'> Slot_4......{character['inventory'][3]}', True, 0.03)
    output('> ------------------------ ', True, 0.03)
    output('> ', True, 0.03)


def move(character):
    pass

def interact(board, character):
    pass

def hull_integrity(hull):
    pass