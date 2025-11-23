import scene_sequence, logic, time, sound, player_turn


def make_interaction():

    def data_pad(character):
        scene_sequence.output("> You reach down to the raised platform beside your open cryopod.", True)
        scene_sequence.output("> The data-pad is half-frozen to the metal, its screen shot through with cracks.\n> ", True)
        time.sleep(1)
        scene_sequence.output("> Carefully, you pry it loose. A few dead pixels flake away like ash.\n> ", True)
        scene_sequence.output("> [\033[31mARCHANGEL\033[0m] ANALYSIS: Peripheral device identified — crew-issued data-slate.", True)
        scene_sequence.output("> [\033[31mARCHANGEL\033[0m] STATUS: Housing compromised, memory sectors unstable but potentially recoverable.\n> ", True)
        scene_sequence.output("> Possible actions:\n> ", True)
        scene_sequence.output(f">   [1] INTERFACE — Attempt to coax surviving memory sectors online.\n>      [STAT: Interface [{character["inf"]}] | DIFFICULTY: [moderate]]\n> ", True)
        scene_sequence.output(f">   [2] ENGAGE — Force the casing open and salvage any intact components.\n>      [STAT: Engage [{character["eng"]}] | DIFFICULTY: [intermediate]]\n> ",    True)
        scene_sequence.output(">> ")
        action = int(scene_sequence.validate_command(("1", "2")))
        if action == 1:
            successful = logic.roll(character["inf"], 3)
            scene_sequence.output("> ", True)
            if successful:
                scene_sequence.output("> [\033[31mARCHANGEL\033[0m] ACTION: Success.\n> ", True)
                scene_sequence.output("> You bridge two exposed contacts and apply careful pressure.", True)
                sound.play_sound(1)
                scene_sequence.output("> The screen buzzes, then stabilizes into a dim, barely functional UI.\n> ", True)
                scene_sequence.output("> [\033[31mARCHANGEL\033[0m] ROUTINE: Bypassing damaged bootloader… partial success.\n> ", True)
                scene_sequence.output("> Fragmented logs materialize — survey notes, flux readings, a reference to something", True)
                scene_sequence.output("> called the “Tethys Rift.”\n> ", True)
                scene_sequence.log_1()
                scene_sequence.output("> [VEIL-9] ENERGY: Energy levels decreased a small amount: ", False)
                character = logic.update("current-EP", character, (-1))
                energy_percent = (character['current-EP'] / 10) * 100
                energy = player_turn.make_bar(character['current-EP'])
                scene_sequence.output(f'{energy} {energy_percent}%', True)
                return character
            else:
                scene_sequence.output("> [\033[31mARCHANGEL\033[0m] ACTION: Failure.\n> ", True)
                scene_sequence.output("> You try to bridge the exposed contacts.", True)
                scene_sequence.output("> A pulse of heat flashes across your glove — the pad pops, internally shorting out.\n> ", True)
                scene_sequence.output("> The screen dies completely.", True)
                scene_sequence.output("> [VEIL-9] HEALTH: Health levels decreased a small amount: ", True)
                character = logic.update("current-HP", character, -1)
                health_percent = (character['current-HP'] / 10) * 100
                health = player_turn.make_bar(character['current-HP'])
                scene_sequence.output(f'{health} {health_percent}%', True)
                return character
        elif action == 2:
            successful = logic.roll(character["eng"], 5)
            scene_sequence.output("> ", True)
            if successful:
                scene_sequence.output("> [\033[31mARCHANGEL\033[0m] ACTION: Success.\n> ", True)
                scene_sequence.output("> You dig your fingers under the casing and twist hard.", True)
                scene_sequence.output("> The brittle housing snaps open with a sharp crack.\n> ", True)
                scene_sequence.output("> Inside, a micro power cell remains intact.", True)
                scene_sequence.output("> [VEIL-9] ENERGY: Energy levels increased a moderate amount: ", True)
                character = logic.update("current-EP", character, 2)
                energy_percent = (character['current-EP'] / 10) * 100
                energy =player_turn.make_bar(character['current-EP'])
                scene_sequence.output(f'{energy} {energy_percent}%', True)
                return character
            else:
                scene_sequence.output("> [\033[31mARCHANGEL\033[0m] ACTION: Failure.\n> ", True)
                scene_sequence.output("> You wrench the casing open — too forcefully. ", True)
                scene_sequence.output("> The frozen plastic explodes in your grip, scattering useless shards.\n> ", True)
                sound.play_sound(2)
                scene_sequence.output("> A few jagged edges bite into your fingertips.\n> ", True)
                scene_sequence.output("> [VEIL-9] HEALTH: Health levels decreased a small amount: ", False)
                character = logic.update("current-HP", character, (-1))
                health_percent = (character['current-HP'] / 10) * 100
                health = player_turn.make_bar(character['current-HP'])
                scene_sequence.output(f'{health} {health_percent}%', True)
                scene_sequence.output("> [VEIL-9] ENERGY: Energy levels decreased a small amount: ", False)
                character = logic.update("current-EP", character, (-1))
                energy_percent = (character['current-EP'] / 10) * 100
                energy =player_turn.make_bar(character['current-EP'])
                scene_sequence.output(f'{energy} {energy_percent}%', True)
                return character
        return character

    has_interact = {
        (1, 1): data_pad
    }
    return has_interact


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

    (1, 1): "Cryopod-03 (Your Pod) - The hatch is hanging sideways. Cracks in the interior ice suggest you thrashed free. A broken \033[31mdata-pad\033[0m lies on the platform.",

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
    scene_sequence.output('> ' + str(board[player_coordinate]), True, 0.03)


def set_room(character):
    pass