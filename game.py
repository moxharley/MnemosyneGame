import pygame, sound, room, logic, player_turn, sequence, sys, os


def game():
    """
    Run the game loop.
    """
    sound.ambient_noise()
    print('\n\n\n\n\n\n')
    player = sequence.boot()
    board = room.make_board()
    board['interacts'] = room.make_interaction()
    sequence.tutorial(board, player)
    goal_achieved = False
    hull_integrity = 90
    while True:
        sequence.output("> \n>> ")
        action = logic.get_user_input()
        if action in ('n', 'N', 'e', 'E', 's', 'S', 'w', 'W'):
            if logic.validate_move(board, player, action):
                player_turn.move(player, action)
            else:
                sequence.output('>\n> [\033[31mARCHANGEL\033[0m] MOVEMENT_DENIED: Obstruction at target coordinates.', True)
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
        if not logic.check_alive(player, hull_integrity):
            break
        if logic.check_win(board, player):
            goal_achieved = True
            break
    if goal_achieved == True:
        sequence.escape()
    else:
        sequence.death()


def main():
    """
    Drive the program.
    """
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=4, buffer=512)
    pygame.mixer.init()
    pygame.mixer.set_num_channels(4)
    print('\n------------------------------------\nHello! Welcome to my game Mnemosyne.\n')
    while True:
        player_start = input('Please type \033[4mstart\033[0m to start the game:\n')
        if player_start != "start":
            print('Invalid Input')
        else:
            print('Starting game...\n------------------------------------')
            game()
            break


if __name__ == "__main__":
    main()