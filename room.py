def look(character):
    pass

def make_board(level):
    if level == 'stasis':
        return make_stasis()
    if level == 'loading':
        return make_loading()
    if level == 'galley':
        return make_galley()
    if level == 'bridge':
        return make_bridge()
    if level == 'observation':
        return make_observation()
    if level == 'pod_1':
        return make_podbay1()
    return None

def make_stasis():
    rows = 6
    columns = 11
    board = {}
    for number1 in range(0, columns):
        for number2 in range(0, rows):
            coordinates = (number1, number2)
            board[coordinates] = ""
    board["goal"] = ((rows - 1), (columns - 1))

    board[(0, 1)] = "Locker - Peeling white paint, a red cross decal is half-scraped away."
    board[(0, 2)] = "Locker - The interior is frosted over. A single blue battery pack rests in the bottom tray."
    board[(0, 3)] = "Locker - The rusted locker door has fallen off the hinges and shattered the cryo pod adjacent."
    board[(0, 4)] = "Locker - Cold vapor spills out as you get close to it."

    board[(2, 1)] = "Cryopod-01 - The inside shows a faint outline of a body in frost."
    board[(2, 2)] = "Cryopod-02 - This cryopod is empty."
    board[(2, 3)] = "Cryopod-03 - This cryopod has been shattered by a fallen locker door. A frozen corpse slumps out"
    board[(2, 4)] = "Cryopod-04 - This cryopod is empty"

    board[(5, 1)] = "Cryopod-05 - The inside shows a faint outline of a body in frost."
    board[(5, 2)] = "Cryopod-06 - The hatch hangs open. The restraint straps are torn and stiff with frozen condensation."
    board[(5, 3)] = "Cryopod-07 - The glass is cracked inward as though something forced its way inside."
    board[(5, 4)] = "Cryopod-08 - This cryopod is empty."

    board[(8, 1)] = "Cryopod-09 - A swirling fog fills the pod interior, lit by faint emergency lights."
    board[(8, 2)] = "Cryopod-10 - The pod display flickers between two unreadable diagnostic screens."
    board[(8, 3)] = "Cryopod-11 - This cryopod is empty."
    board[(8, 4)] = "Cryopod-12 - This cryopod is empty."

    board[(10, 2)] = "Terminal - A low-power terminal displaying flickering blue text."
    board[(10, 3)] = "Terminal - This terminal stutters through corrupted log frames."

    board['Cryopod-03']
    board['Cryopod-07']
    board['Cryopod-10']
    board['Terminal']
    board['Locker-1']
    board['Locker-2']
    board['Locker-3']
    board['Locker-4']

    return

def make_loading():
    pass

def make_galley():
    pass

def make_bridge():
    pass

def make_observation():
    pass

def make_podbay1():
    pass