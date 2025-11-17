import pygame, sound, room, logic, player_turn, sequence


def game():
    sound.ambient_noise()
    player = sequence.boot()
    board = room.make_board()
    sequence.tutorial(player)
    goal_achieved = False
    hull_integrity = 90
    while goal_achieved == False:
        room.describe_current_location(board, player)
        action = logic.get_user_input()
        if action in ('n', 'N', 'e', 'E', 's', 'S', 'w', 'W'):
            player = player_turn.move(player)
        elif action in ('status', 'Status'):
            player = player_turn.status(player)
        elif action in ('look', 'Look'):
            player = player_turn.look(board, player)
        elif action in ('interact', 'Interact'):
            player = player_turn.interact(board, player)
        hull_integrity = player_turn.hull_damage(hull_integrity)
    if goal_achieved == True:
        sequence.escape(player)
    else:
        sequence.death(player)



def main():
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
    pygame.mixer.init()
    pygame.mixer.set_num_channels(4)
    game()


    # ┌───────┐  ┌──────┐  ┌───────┐
    # │Medical├──┼Galley┼──┤Loading│
    # │ Bay   │  └──┬┬──┘  │ Bay   │
    # └──┬┬───┘  ┌──┴┴──┐  └───┬┬──┘
    # ┌──┴┴────┐ │Bridge│  ┌───┴┴──┐
    # │Crew    │ └──┬┬──┘  │Stasis │
    # │Quarters│    ││     │ Pods  │
    # └────────┘    ││     └───────┘
    #          ┌────┴┴─────┐
    #          │Maintenance│
    #          │ Access    │
    #          └────┬┬─────┘
    #   ┌─────┐ ┌───┴┴───┐ ┌───────┐
    #   │Relay├─┤Reactors├─┤Utility│
    #   └─────┘ └───┬┬───┘ └───────┘
    #          ┌────┴┴─────┐
    #          │Fabrication│
    #          │ Bay       │
    #          └────┬┬─────┘
    #           ┌───┴┴────┐
    #           │Emergency│
    #           │Pod Bay 2│
    #           └─────────┘


if __name__ == "__main__":
    main()