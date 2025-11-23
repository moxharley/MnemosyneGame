import random, scene_sequence, time, sys


def get_user_input():
    """
    Get user input.

    Prompts user input for character action.

    :postcondition: prompts movement input and ensures it is well-formed.
    :return: a valid string input.
    """
    while True:
        action = str(input())
        accepted_inputs = ('n', 'N', 'e', 'E', 's', 'S', 'w', 'W', 'look', 'status', 'lore', 'interact', 'Status', 'Interact')
        if action not in accepted_inputs:
            scene_sequence.output('> INVALID INPUT: Type a valid input')
            time.sleep(1)
            sys.stdout.write('\r')
            scene_sequence.output('>> ')
        else:
            break
    return action


def move_character(character, direction):
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

    >>> move_character({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}, 's')
    {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
    >>> move_character({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}, 'e')
    {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
    """
    north = ('n', 'N')
    east = ('e', 'E')
    south = ('s', 'S')
    west = ('w', 'W')
    if direction in north:
        character["Y-coordinate"] += 1
    elif direction in east:
        character["X-coordinate"] -= 1
    elif direction in south:
        character["Y-coordinate"] -= 1
    elif direction in west:
        character["X-coordinate"] += 1
    return character


def validate_move(board, character, direction):
    """
    Validate move coordinates.

    Ensures movement stays within game-board confines.

    :param board: a dictionary.
    :param character: a dictionary.
    :param direction: a single character string.
    :precondition: direction must be 'n', 'N', 'e', 'E', 's', 'S', 'w' or 'W'
    :precondition: board must be a dictionary in the proper format (i.e. {(0, 0): Room,... 'Goal': (X, X)}.
    :precondition: character must be a dictionary with an "X-coordinate" and "Y-coordinate" key.
    :precondition: character["X-coordinate"] and character["Y-coordinate] must be integers.
    :postcondition: ensures movement is legal and stays within board confines.
    :return: a boolean value of whether the move is valid.

    >>> validate_move({(0, 0): 'Empty Room', (1, 0): 'Empty Room', 'goal': (1, 0)}, {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}, 's')
    True
    >>> validate_move({(0, 0): 'Empty Room', (1, 0): 'Empty Room', 'goal': (1, 0)}, {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}, 'n')
    False
    """
    north = ('n', 'N')
    east = ('e', 'E')
    south = ('s', 'S')
    west = ('w', 'W')
    character_coordinates = [character["X-coordinate"], character["Y-coordinate"]]
    if direction in north:
        character_coordinates[0] -= 1
    elif direction in east:
        character_coordinates[1] += 1
    elif direction in south:
        character_coordinates[0] += 1
    elif direction in west:
        character_coordinates[1] -= 1
    return tuple(character_coordinates) in board


def roll(stat, difficulty_class):
    """
    Roll a die.

    Roll a die to beat a difficulty class.

    :param stat: an integer variable
    :param difficulty_class: an integer variable
    :precondition: stat must be at least -1 and no greater than 2.
    :precondition: difficulty_class must be at least 1 and no greater than 8.
    :postcondition: determines whether you pass a difficulty class roll.
    :return: a boolean variable.
    """
    dice = random.randint(1, 6)
    dice += stat
    return dice >= difficulty_class


def experience(character):
    pass


def level_up(character):
    pass


def update(key, character, amount):
    """
    Update health or energy.

    :param key: a string variable.
    :param character: a well-formed character dictionary.
    :param amount: an integer variable.
    :precondition: character must be a dictionary with a "current-HP" and "current-EP" key.
    :precondition: character["current-HP"] and character["current-EP"] must be integers.
    :postcondition: deals damage or drains energy of player.
    :return: updated character dictionary.
    """
    character[key] += amount
    if character[key] < 0:
        character[key] = 0
    return character