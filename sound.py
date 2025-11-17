import pygame


def play_track(track):
    """
    Play track.

    :param track: an integer variable
    :precondition: track must be an integer variable greater than 0 or less than 5.
    :postcondition: plays track audio.
    """
    if track == 1:
        track = pygame.mixer.Sound('sounds/track_1.ogg')
        track.set_volume(0.2)
        track.play(loops=1, fade_ms=1500)
    elif track == 2:
        track = pygame.mixer.Sound('sounds/track_2.ogg')
        track.set_volume(0.2)
        track.play(loops=1, fade_ms=1500)
    elif track == 3:
        track = pygame.mixer.Sound('sounds/track_3.ogg')
        track.set_volume(0.2)
        track.play(loops=1, fade_ms=1500)
    elif track == 4:
        track = pygame.mixer.Sound('sounds/track_4.ogg')
        track.set_volume(0.2)
        track.play(loops=1, fade_ms=1500)


def ambient_noise():
    """
    Play ambient sound.
    """
    ambient = pygame.mixer.Sound('sounds/ambient.ogg')
    ambient.set_volume(1.5)
    ambient.play(loops=-1, fade_ms=1500)