import pygame, sound, room, logic, player_turn, scene_sequence


def game():
    """
    Run the game loop.
    """
    sound.ambient_noise()
    player = {'X-coordinate': 1, 'Y-coordinate': 1, 'first-name': "Jimmy", 'last-name': "Freaks", 'current-HP': 8,
              'current-EP': 7, 'room': 'Stasis-Pods', 'class': 'Ace-pilot', 'end': -1, 'eng': 1, 'inf': 0, 'int': 0,
              'exp': 2, 'inventory': ['Side-Arm', 'Empty', 'Empty', 'Empty']}
    board = room.make_board()
    board['interacts'] = room.make_interaction()
    player_turn.interact(board['interacts'], player)


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