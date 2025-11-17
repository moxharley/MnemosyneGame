import pygame, sound, room, logic, player_turn, scene_sequence


def game():
    """
    Run the game loop.
    """
    sound.ambient_noise()
    player = scene_sequence.boot()
    board = room.make_board()
    scene_sequence.tutorial(board, player)
    goal_achieved = False
    hull_integrity = 90
    while goal_achieved == False:
        action = logic.get_user_input()
        if action in ('n', 'N', 'e', 'E', 's', 'S', 'w', 'W'):
            player = player_turn.move(player)
        elif action in ('status', 'Status'):
            player = player_turn.status(player)
        elif action in ('look', 'Look'):
            player = player_turn.look(board, player)
        elif action in ('interact', 'Interact'):
            player = player_turn.interact(board, player)
        elif action in ('map', 'Map'):
            player_turn.map()
        hull_integrity = player_turn.hull_damage(hull_integrity)
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