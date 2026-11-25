import os

import pygame

from space_invaders import settings


class SoundManager:
    """Charge les sons une seule fois puis les joue quand on le demande."""

    def __init__(self):
        self.sounds = {}
        try:
            pygame.mixer.init()
            self.sounds["laser"] = pygame.mixer.Sound(os.path.join(settings.SOUNDS_DIR, "laser.wav"))
            self.sounds["explosion"] = pygame.mixer.Sound(os.path.join(settings.SOUNDS_DIR, "explosion.wav"))
            pygame.mixer.music.load(os.path.join(settings.SOUNDS_DIR, "background.wav"))
            pygame.mixer.music.play(-1)
        except pygame.error:
            # par exemple si l'ordinateur n'a pas de carte son
            print("Attention : impossible de charger les sons, le jeu sera muet.")

    def play(self, name):
        if name in self.sounds:
            self.sounds[name].play()
