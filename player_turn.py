from sequence import output

def look(board, character):
    pass


def make_bar(current):
    filled = ''
    empty = ''

    for index in range(1, current):
        filled += '▓'

    for index in range(1, (10-current)):
        empty += '░'

    bar = '|' + filled + empty + '|'
    return bar

def status(character):
    output('>\n> COMMAND: status\n>', True, 0.01)
    output('> --------------------------------------------------', True, 0.01)
    output('> IDENTITY', True, 0.01)
    output(f'> Name...............{character['first-name']}', True, 0.01)
    output(f'> Designation........{character['class']}', True, 0.01)

    health = make_bar(character['current-HP'])
    energy = make_bar(character['current-EP'])

    output('> VITALS', True, 0.01)
    output(f'> Health........{health}', True, 0.01)
    output(f'> Energy........{energy}', True, 0.01)
    output('> ATTRIBUTES', True, 0.01)
    output(f'> Endure...........|{character['end']}|', True, 0.01)
    output(f'> Engage...........|{character['eng']}|', True, 0.01)
    output(f'> Interface........|{character['inf']}|', True, 0.01)
    output(f'> Intuit...........|{character['int']}|', True, 0.01)
    output('> --------------------------------------------------', True, 0.01)
    output('> [VEIL-9] NOTICE: Values outside safe range may result in cognitive drift, structural failure, or death.\n>\n>>', False, 0.01)

def move(character):
    pass

def interact(board, character):
    pass

def hull_integrity(hull):
    pass