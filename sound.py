import pygame


def play_track(track):
    """
    Play track.
    """
    if track == 1:
        track = pygame.mixer.Sound('sounds/track_1.ogg')
        track.set_volume(0.2)
        track.play(loops=1, fade_ms=1500)
    elif track == 2:
        track = pygame.mixer.Sound('sounds/track_2.ogg')
        track.set_volume(0.13)
        track.play(loops=0, fade_ms=1500)
    elif track == 3:
        track = pygame.mixer.Sound('sounds/track_3.ogg')
        track.set_volume(0.2)
        track.play(loops=1, fade_ms=1500)
    elif track == 4:
        track = pygame.mixer.Sound('sounds/track_4.ogg')
        track.set_volume(0.2)
        track.play(loops=1, fade_ms=1500)


def play_sound(sound):
    """
    Play sound.
    """
    if sound == 1:
        sound = pygame.mixer.Sound('sounds/interface.ogg')
        sound.set_volume(1)
        sound.play(loops=0, fade_ms=1500)
    elif sound == 2:
        sound = pygame.mixer.Sound('sounds/damage.ogg')
        sound.set_volume(1)
        sound.play(loops=0, fade_ms=1500)
    elif sound == 3:
        sound = pygame.mixer.Sound('sounds/success.ogg')
        sound.set_volume(1)
        sound.play(loops=0, fade_ms=1500)
    elif sound == 4:
        sound = pygame.mixer.Sound('sounds/failure.ogg')
        sound.set_volume(1)
        sound.play(loops=0, fade_ms=1500)
    elif sound == 5:
        sound = pygame.mixer.Sound('sounds/hull_1.ogg')
        sound.set_volume(1.8)
        sound.play(loops=0, fade_ms=1500)
    elif sound == 6:
        sound = pygame.mixer.Sound('sounds/hull_2.ogg')
        sound.set_volume(2)
        sound.play(loops=0, fade_ms=1500)
    elif sound == 7:
        sound = pygame.mixer.Sound('sounds/hull_3.ogg')
        sound.set_volume(0.3)
        sound.play(loops=0, fade_ms=1500)
    elif sound == 8:
        sound = pygame.mixer.Sound('sounds/death.ogg')
        sound.set_volume(1)
        sound.play(loops=0, fade_ms=1500)


def ambient_noise():
    """
    Play ambient sound.
    """
    ambient = pygame.mixer.Sound('sounds/ambient.ogg')
    ambient.set_volume(1.9)
    ambient.play(loops=-1, fade_ms=1500)