import pygame, sound, room, logic, player_turn, sequence


def game():
    """
    Run the game loop.
    """
    sound.ambient_noise()
    player = sequence.boot()
    board = room.make_board()
    board['interacts'] = room.make_interaction()
    sequence.tutorial(board, player)
    goal_achieved = False
    hull_integrity = 90
    encounters_passed = [False, False]
    while True:
        sequence.output("> \n>> ")
        action = logic.get_user_input()
        if action in ('n', 'N', 'e', 'E', 's', 'S', 'w', 'W'):
            if logic.validate_move(board, player, action):
                player_turn.move(player, action)
            else:
                sequence.output('>\n> [\033[31mARCHANGEL\033[0m] MOVEMENT_DENIED: Obstruction at target coordinates.', True, 0.03)
        elif action in ('status', 'Status'):
            player_turn.status(player)
            logic.energy_drain(player)
        elif action in ('look', 'Look'):
            player_turn.look(board, player)
            logic.energy_drain(player)
        elif action in ('interact', 'Interact'):
            player_turn.interact(board['interacts'], player)
        elif action in ('map', 'Map'):
            player_turn.ship_map()
            logic.energy_drain(player)
        hull_integrity = logic.hull_damage(hull_integrity)
        room.encounter_chance(player, encounters_passed)
        if not logic.check_alive(player, hull_integrity):
            break
        if logic.check_win(board, player):
            goal_achieved = True
            break
    if goal_achieved:
        sequence.end_game()
    else:
        sequence.death()


def main():
    """
    Drive the program.
    """
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=4, buffer=512)
    pygame.mixer.init()
    pygame.mixer.set_num_channels(4)
    print(
    """
-----------------------------------------------------------------------
    Hello! Welcome to my Term Project!

    This is a demo for a game called \033[1mMnemosyne\033[0m, 
    a text-based sci-fi horror/thriller experience.

    The game is fully functional and should have no bugs or crashes.
    I believe I have sufficiently met all the criteria, though since 
    I chose a bit of a radical direction for my genre, if I am missing 
    anything, I hope that this still demonstrates my proficiency in the 
    subject material of your class.
    
    My original scope for the game was perhaps a little too ambitious,
    and though I have met almost every one of the project requirements, any text or output
    highlighted in \033[34mblue\033[0m is something that was planned but unfinished.
    I figured it was more important to ensure I met all the project requirements
    than to dwell on the things that aren't incredibly central to the game loop.

    I really enjoyed your lectures, and I am glad to see that I have 
    another class with you next term!

    All the best, and enjoy your winter break!
    
    Also turn your sound on!!! I spent too much time on the sound!!!

       — Harlan
-----------------------------------------------------------------------
    """
    )
    while True:
        player_start = input('Please type \033[4mstart\033[0m to start the game:\n')
        if player_start != "start":
            print('Invalid Input')
        else:
            print('Starting game...')
            sequence.output('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n', delay=0.03)
            game()
            break


if __name__ == "__main__":
    main()