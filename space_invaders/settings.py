"""Toutes les constantes du jeu sont regroupees ici.

Comme ca on evite les "nombres magiques" dans le code (736, 480...)
et on peut modifier le jeu a un seul endroit.
"""
import os

# Ecran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
TITLE = "Space Invaders - Groupe 10"

# Dossier des ressources (images, sons)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = os.path.join(BASE_DIR, "assets", "images")
SOUNDS_DIR = os.path.join(BASE_DIR, "assets", "sounds")

# Joueur
PLAYER_SIZE = 64
PLAYER_SPEED = 5
PLAYER_Y = 480

# Ennemis
ENEMY_SIZE = 64
BOSS_SIZE = 96
FLEET_SPEED = 2          # vitesse horizontale de la flotte
FLEET_SPEED_BONUS = 0.5  # vitesse en plus a chaque nouvelle vague
FLEET_STEP_DOWN = 30     # de combien la flotte descend quand elle touche un bord

# Projectiles
BULLET_SIZE = 32
BULLET_SPEED = 10

# Couleurs
WHITE = (255, 255, 255)
RED = (220, 40, 40)
GREEN = (40, 200, 40)
