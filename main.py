"""Point d'entree du jeu : lance avec  python main.py"""
import os

import pygame

from space_invaders import settings
from space_invaders.game import Game
from space_invaders.view.renderer import Renderer
from space_invaders.view.sounds import SoundManager


def main():
    pygame.init()
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption(settings.TITLE)
    pygame.display.set_icon(pygame.image.load(os.path.join(settings.IMAGES_DIR, "ufo.png")))
    clock = pygame.time.Clock()

    game = Game()
    renderer = Renderer(screen)
    sounds = SoundManager()

    running = True
    while running:
        # 1) les evenements (touches appuyees une fois)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_1:
                    game.change_weapon(0)
                if event.key == pygame.K_2:
                    game.change_weapon(1)
                if event.key == pygame.K_r and game.game_over:
                    game.restart()

        # 2) les touches maintenues (deplacement et tir)
        keys = pygame.key.get_pressed()
        game.player.direction = 0
        if keys[pygame.K_LEFT]:
            game.player.direction = -1
        if keys[pygame.K_RIGHT]:
            game.player.direction = 1
        if keys[pygame.K_SPACE]:
            game.player_shoot()

        # 3) la logique du jeu
        game.update()

        # 4) les sons demandes par le jeu
        for name in game.sounds_to_play:
            sounds.play(name)
        game.sounds_to_play.clear()

        # 5) l'affichage
        renderer.draw(game)
        clock.tick(settings.FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
