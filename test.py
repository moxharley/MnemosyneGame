import pygame, sound, room, logic, player_turn, scene_sequence


def game():
    """
    Run the game loop.
    """
    sound.ambient_noise()
    player = {'X-coordinate': 1, 'Y-coordinate': 1, 'first-name': "Jimmy", 'last-name': "Freaks", 'current-HP': 8,
              'current-EP': 7, 'room': 'Stasis-Pods', 'class': 'Ace-pilot', 'end': -1, 'eng': 1, 'inf': 0, 'int': 0,
              'inventory': ['Side-Arm', 'Empty', 'Empty', 'Empty']}
    board = room.make_board()
    board['interacts'] = room.make_interaction()
    goal_achieved = False
    hull_integrity = 90
    while goal_achieved == False:
        scene_sequence.output("> \n>> ")
        action = logic.get_user_input()
        if action in ('n', 'N', 'e', 'E', 's', 'S', 'w', 'W'):
            if logic.validate_move(board, player, action):
                player_turn.move(player, action)
            else:
                scene_sequence.output('>\n> [\033[31mARCHANGEL\033[0m] MOVEMENT_DENIED: Obstruction at target coordinates.', True)
        elif action in ('status', 'Status'):
            player_turn.status(player)
        elif action in ('look', 'Look'):
            player_turn.look(board, player)
        elif action in ('interact', 'Interact'):
            player_turn.interact(board['interacts'], player)
        elif action in ('map', 'Map'):
            player_turn.ship_map()
    if goal_achieved == True:
        scene_sequence.escape(player)
    else:
        scene_sequence.death(player)


def main():
    """
    Drive the program.
    """
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
    pygame.mixer.init()
    pygame.mixer.set_num_channels(4)
    game()


if __name__ == "__main__":
    main()