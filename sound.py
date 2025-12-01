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
    channel = None
    if sound == 1:
        sound = pygame.mixer.Sound('sounds/interface.ogg')
        sound.set_volume(0.7)
        channel = sound.play(loops=0, fade_ms=500)
    elif sound == 2:
        sound = pygame.mixer.Sound('sounds/damage.ogg')
        sound.set_volume(0.5)
        channel = sound.play(loops=0, fade_ms=500)
    elif sound == 3:
        sound = pygame.mixer.Sound('sounds/success.ogg')
        sound.set_volume(0.5)
        channel = sound.play(loops=0, fade_ms=500)
    elif sound == 4:
        sound = pygame.mixer.Sound('sounds/failure.ogg')
        sound.set_volume(1.2)
        channel = sound.play(loops=0, fade_ms=500)
    elif sound == 5:
        sound = pygame.mixer.Sound('sounds/hull_1.ogg')
        sound.set_volume(2.5)
        channel = sound.play(loops=0, fade_ms=1500)
    elif sound == 6:
        sound = pygame.mixer.Sound('sounds/hull_2.ogg')
        sound.set_volume(2.5)
        channel = sound.play(loops=0, fade_ms=1500)
    elif sound == 7:
        sound = pygame.mixer.Sound('sounds/hull_3.ogg')
        sound.set_volume(0.3)
        channel = sound.play(loops=0, fade_ms=1500)
    elif sound == 8:
        sound = pygame.mixer.Sound('sounds/death.ogg')
        sound.set_volume(0.9)
        channel = sound.play(loops=0, fade_ms=1500)
    elif sound == 9:
        sound = pygame.mixer.Sound('sounds/drone.ogg')
        sound.set_volume(0.9)
        channel = sound.play(loops=-1, fade_ms=8000)
    elif sound == 10:
        sound = pygame.mixer.Sound('sounds/danger.ogg')
        sound.set_volume(0.5)
        channel = sound.play(loops=0, fade_ms=9000)
    elif sound == 11:
        sound = pygame.mixer.Sound('sounds/alert.ogg')
        sound.set_volume(0.6)
        channel = sound.play(loops=0, fade_ms=1500)
    elif sound == 12:
        sound = pygame.mixer.Sound('sounds/growl.ogg')
        sound.set_volume(0.3)
        channel = sound.play(loops=0, fade_ms=6000)
    elif sound == 13:
        sound = pygame.mixer.Sound('sounds/growl.ogg')
        sound.set_volume(0.6)
        channel = sound.play(loops=0, fade_ms=6000)
    elif sound == 14:
        sound = pygame.mixer.Sound('sounds/calling.ogg')
        sound.set_volume(0.6)
        channel = sound.play(loops=0, fade_ms=20000)
    elif sound == 15:
        sound = pygame.mixer.Sound('sounds/gaunt.ogg')
        sound.set_volume(0.7)
        channel = sound.play(loops=0, fade_ms=6000)
    elif sound == 16:
        sound = pygame.mixer.Sound('sounds/voices.ogg')
        sound.set_volume(0.7)
        channel = sound.play(loops=0, fade_ms=6000)
    elif sound == 17:
        sound = pygame.mixer.Sound('sounds/pressure.ogg')
        sound.set_volume(0.7)
        channel = sound.play(loops=-1, fade_ms=6000)
    elif sound == 18:
        sound = pygame.mixer.Sound('sounds/gore.ogg')
        sound2 = pygame.mixer.Sound('sounds/damage.ogg')
        sound.set_volume(1.2)
        sound2.set_volume(1.6)
        sound2.play(loops=0, fade_ms=1500)
        channel = sound.play(loops=0, fade_ms=1500)
    return channel


def ambient_noise():
    """
    Play ambient sound.
    """
    ambient = pygame.mixer.Sound('sounds/ambient.ogg')
    ambient.set_volume(1.9)
    ambient.play(loops=-1, fade_ms=1500)