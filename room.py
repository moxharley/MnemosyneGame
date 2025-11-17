import game


def look(character):
    pass


def make_board():
    """
    Make board.

    Makes the playable map of the starship.

    :return: a well-formed board dictionary
    """
    board = {
    (0, 0): "Entrance Hatch - The sliding hatch leads out into the hallway. Frost rims its seams, and a faint green exit strip glows beneath your feet.",

    (1, 0): "Overhead Conduit - The ceiling panel above is bowed and stained by a dark, dried drip. Something dripped here recently.",

    (2, 0): "Supply Cabinet - A waist-high storage cabinet. Its magnetic lock flickers weakly, and the metal is dented from the inside.",

    (3, 0): "Cryopod-01 (Fractured) - The viewport glass is shattered inward as though something forced its way inside. Frost spreads in jagged veins.",

    (0, 1): "Cryopod-02 (Offline) - The pod is dark. A faint human-shaped frost imprint remains on the window, but the pod is empty.",

    (1, 1): "Cryopod-03 (Your Pod) - The hatch is hanging sideways. Cracks in the interior ice suggest you thrashed free. A broken datapad lies on the platform.",

    (2, 1): "Terminal A - A flickering stasis control terminal. Lines of corrupted diagnostics scroll by too quickly to read.",

    (3, 1): "Cryopod-04 (Scorched) - The inner surface is warped and blackened by heat. Something inside burned violently before power failed.",

    (0, 2): "Cryopod-05 (Scratched) - Deep, uneven gouges mark the inside walls. Some look metallic; others disturbingly biological.",

    (1, 2): "Cryopod-06 (Coolant Leak) - Coolant pools beneath the pod, unusually dark and viscous. It reeks of warm metal.",

    (2, 2): "Terminal B - A partially frozen backup terminal. Crew IDs flicker onscreen before dissolving into static.",

    (3, 2): "Drain Pit - A grated floor drain where melted ice gathers. Something metallic clatters deep beneath it when you move nearby."
    }
    return board


def describe_current_location(board, character):
    """
    Describe current location.

    Prints the associated description of the current character location.

    :param board: a dictionary.
    :param character: a dictionary.
    :precondition: board must be a dictionary in the proper format (i.e. {(0, 0): Room,... 'Goal': (1, 1)}.
    :precondition: character must be a dictionary with a "Y-coordinate" and "X-coordinate" key.
    :precondition: character["Y-coordinate"] and character["X-coordinate] must be integers.
    :postcondition: finds the associated description of the character's current location on the board.
    :return: None
    """
    player_coordinate = (character["X-coordinate"], character["Y-coordinate"])
    game.output("> Description: ")
    game.archangel_output(str(board[player_coordinate]))