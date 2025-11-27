import sequence, logic, time, sound, player_turn


def make_interaction():

    def data_pad(character):
        sequence.output("> You reach down to the raised platform beside your open cryopod.", True)
        sequence.output("> The data-pad is half-frozen to the metal, its screen shot through with cracks.\n> ", True)
        time.sleep(1)
        sequence.output("> Carefully, you pry it loose. A few dead pixels flake away like ash.\n> ", True)
        sequence.output("> [\033[31mARCHANGEL\033[0m] ANALYSIS: Peripheral device identified — crew-issued data-slate.", True)
        sequence.output("> [\033[31mARCHANGEL\033[0m] STATUS: Housing compromised, memory sectors unstable but potentially recoverable.\n> ", True)
        sequence.output("> Possible actions:\n> ", True)
        sequence.output(f">   [1] INTERFACE — Attempt to coax surviving memory sectors online.\n>      [STAT: Interface [{character["inf"]}] | DIFFICULTY: [moderate]]\n> ", True)
        sequence.output(f">   [2] ENGAGE — Force the casing open and salvage any intact components.\n>      [STAT: Engage [{character["eng"]}] | DIFFICULTY: [intermediate]]\n> ",    True)
        sequence.output(">> ")
        action = int(sequence.validate_command(("1", "2")))
        if action == 1:
            successful = logic.roll(character["inf"], 3)
            sequence.output("> ", True)
            if successful:
                sound.play_sound(3)
                sequence.output("> [\033[31mARCHANGEL\033[0m] ACTION: Success.\n> ", True)
                sequence.output("> You bridge two exposed contacts and apply careful pressure.", True)
                sound.play_sound(1)
                sequence.output("> The screen buzzes, then stabilizes into a dim, barely functional UI.\n> ", True)
                sequence.output("> [\033[31mARCHANGEL\033[0m] ROUTINE: Bypassing damaged bootloader… partial success.\n> ", True)
                sequence.output("> Fragmented logs materialize — survey notes, flux readings, a reference to something", True)
                sequence.output("> called the “Tethys Rift.”\n> ", True)
                sequence.log_1()
                sequence.output("> [VEIL-9] ENERGY: Energy levels decreased a small amount: ", False)
                character = logic.update("current-EP", character, (-1))
                energy_percent = (character['current-EP'] / 10) * 100
                energy = player_turn.make_bar(character['current-EP'])
                sequence.output(f'{energy} {energy_percent}%\n>', True)
            else:
                sound.play_sound(4)
                sequence.output("> [\033[31mARCHANGEL\033[0m] ACTION: Failure.\n> ", True)
                sequence.output("> You try to bridge the exposed contacts.", True)
                sequence.output("> A pulse of heat flashes across your glove — the pad pops, internally shorting out.\n> ", True)
                sequence.output("> The screen dies completely.\n>", True)
                sequence.output("> [VEIL-9] HEALTH: Health levels decreased a small amount: ")
                character = logic.update("current-HP", character, -1)
                health_percent = (character['current-HP'] / 10) * 100
                health = player_turn.make_bar(character['current-HP'])
                sequence.output(f'{health} {health_percent}%\n>', True)
                character = logic.level_up(character)
        elif action == 2:
            successful = logic.roll(character["eng"], 5)
            sequence.output("> ", True)
            if successful:
                sound.play_sound(3)
                sequence.output("> [\033[31mARCHANGEL\033[0m] ACTION: Success.\n> ", True)
                sequence.output("> You dig your fingers under the casing and twist hard.", True)
                sequence.output("> The brittle housing snaps open with a sharp crack.\n> ", True)
                sequence.output("> Inside, a micro power cell remains intact.\n>", True)
                sequence.output("> [VEIL-9] ENERGY: Energy levels increased a moderate amount: ")
                character = logic.update("current-EP", character, 2)
                energy_percent = (character['current-EP'] / 10) * 100
                energy =player_turn.make_bar(character['current-EP'])
                sequence.output(f'{energy} {energy_percent}%\n>', True)
            else:
                sound.play_sound(4)
                sequence.output("> [\033[31mARCHANGEL\033[0m] ACTION: Failure.\n> ", True)
                sequence.output("> You wrench the casing open — too forcefully. ", True)
                sequence.output("> The frozen plastic explodes in your grip, scattering useless shards.\n> ", True)
                sound.play_sound(2)
                sequence.output("> A few jagged edges bite into your fingertips.\n> ", True)
                sequence.output("> [VEIL-9] HEALTH: Health levels decreased a small amount: ", False)
                character = logic.update("current-HP", character, (-1))
                health_percent = (character['current-HP'] / 10) * 100
                health = player_turn.make_bar(character['current-HP'])
                sequence.output(f'{health} {health_percent}%', True)
                sequence.output("> [VEIL-9] ENERGY: Energy levels decreased a small amount: ", False)
                character = logic.update("current-EP", character, (-1))
                energy_percent = (character['current-EP'] / 10) * 100
                energy = player_turn.make_bar(character['current-EP'])
                sequence.output(f'{energy} {energy_percent}%\n>', True)
                character = logic.level_up(character)
        del has_interact[(1, 1)]
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
        (0, 0): ("Entrance Hatch - The sliding hatch leads out into the hallway. Frost rims its seams, and a faint green exit strip glows beneath your feet.", "Stasis-Pods"),

        (1, 0): ("Overhead Conduit - The ceiling panel above is bowed and stained by a dark, dried drip. Something dripped here recently.", "Stasis-Pods"),

        (2, 0): ("Supply Cabinet - A waist-high storage cabinet. Its magnetic \033[34mlock\033[0m flickers weakly, and the metal is dented from the inside.", "Stasis-Pods"),

        (3, 0): ("Cryopod-01 (Fractured) - The viewport glass is shattered inward as though something forced its way inside. Frost spreads in jagged veins.", "Stasis-Pods"),

        (0, 1): ("Cryopod-02 (Offline) - The pod is dark. A faint human-shaped frost imprint remains on the window, but the pod is empty.", "Stasis-Pods"),

        (1, 1): ("Cryopod-03 (Your Pod) - The hatch is hanging sideways. Cracks in the interior ice suggest you thrashed free. A broken \033[31mdata-pad\033[0m lies on the platform.", "Stasis-Pods"),

        (2, 1): ("Terminal A - A flickering stasis control terminal. Lines of corrupted diagnostics scroll by too quickly to read.", "Stasis-Pods"),

        (3, 1): ("Cryopod-04 (Scorched) - The inner surface is warped and blackened by heat. Something inside burned violently before power failed.", "Stasis-Pods"),

        (0, 2): ("Cryopod-05 (Scratched) - Deep, uneven gouges mark the inside walls. Some look metallic; others disturbingly biological.", "Stasis-Pods"),

        (1, 2): ("Cryopod-06 (Coolant Leak) - Coolant pools beneath the pod, unusually dark and viscous. It reeks of warm metal.", "Stasis-Pods"),

        (2, 2): ("Terminal B - A partially frozen backup \033[34mterminal\033[0m. Crew IDs flicker onscreen before dissolving into static.", "Stasis-Pods"),

        (3, 2): ("Drain Pit - A grated floor drain where melted ice gathers. Something metallic clatters deep beneath it when you move nearby.", "Stasis-Pods"),

        (0, 3): ("WIP - Empty description (Corridor).", "Corridor"),

        (0, 4): ("WIP - Empty description (Corridor).", "Corridor"),

        (0, 5): ("WIP - Empty description (Loading Bay)", "Loading Bay"),

        (0, 6): ("WIP - Empty description (Loading Bay)", "Loading Bay"),

        (0, 7): ("WIP - Empty description (Loading Bay)", "Loading Bay"),

        (-1, 5): ("WIP - Empty description (Loading Bay)", "Loading Bay"),

        (-1, 6): ("WIP - Empty description (Loading Bay)", "Loading Bay"),

        (-1, 7): ("WIP - Empty description (Loading Bay)", "Loading Bay"),

        (1, 5): ("WIP - Empty description (Loading Bay)", "Loading Bay"),

        (1, 6): ("WIP - Empty description (Loading Bay)", "Loading Bay"),

        (1, 7): ("WIP - Empty description (Loading Bay)", "Loading Bay")

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
    sequence.output('> ' + str(board[player_coordinate][0]), True, 0.03)