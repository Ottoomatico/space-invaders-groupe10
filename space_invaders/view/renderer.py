import os

import pygame

from space_invaders import settings


class Renderer:
    """Dessine la partie a l'ecran avec pygame."""

    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 80)

        self.background = self.load_image("background.png")
        enemy_image = self.load_image("enemy.png")

        # chaque objet du jeu a un image_name qui correspond a une cle ici
        self.images = {
            "player": self.load_image("player.png"),
            "enemy": enemy_image,
            "boss": pygame.transform.scale(enemy_image, (settings.BOSS_SIZE, settings.BOSS_SIZE)),
            "bullet": self.load_image("bullet.png"),
        }

    def load_image(self, filename):
        return pygame.image.load(os.path.join(settings.IMAGES_DIR, filename)).convert_alpha()

    def draw(self, game):
        self.screen.blit(self.background, (0, 0))

        self.screen.blit(self.images["player"], (game.player.x, game.player.y))

        for enemy in game.fleet.enemies:
            self.screen.blit(self.images[enemy.image_name], (enemy.x, enemy.y))
            if enemy.max_hp > 1:
                self.draw_health_bar(enemy)

        for projectile in game.projectiles:
            self.screen.blit(self.images[projectile.image_name], (projectile.x, projectile.y))

        self.draw_text("Score : " + str(game.score), 10, 10)
        self.draw_text("Vague : " + str(game.wave), 10, 45)
        self.draw_text("Arme : " + game.player.weapon.name, 560, 10)

        if game.game_over:
            self.draw_game_over()

        pygame.display.update()

    def draw_health_bar(self, enemy):
        """Petite barre de vie au dessus des ennemis qui ont plusieurs PV (boss)."""
        width = enemy.width * enemy.hp / enemy.max_hp
        pygame.draw.rect(self.screen, settings.RED, (enemy.x, enemy.y - 10, enemy.width, 6))
        pygame.draw.rect(self.screen, settings.GREEN, (enemy.x, enemy.y - 10, width, 6))

    def draw_text(self, text, x, y):
        image = self.font.render(text, True, settings.WHITE)
        self.screen.blit(image, (x, y))

    def draw_game_over(self):
        # fond noir transparent pour que le texte soit lisible
        overlay = pygame.Surface((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        overlay.set_alpha(160)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))

        text = self.big_font.render("GAME OVER", True, settings.WHITE)
        x = settings.SCREEN_WIDTH / 2 - text.get_width() / 2
        self.screen.blit(text, (x, 230))

        info = self.font.render("Appuie sur R pour rejouer", True, settings.WHITE)
        x = settings.SCREEN_WIDTH / 2 - info.get_width() / 2
        self.screen.blit(info, (x, 310))
