from space_invaders import settings
from space_invaders.entities.enemies import BasicEnemy, BossEnemy


class Fleet:
    """La flotte d'ennemis.

    Tous les ennemis se deplacent ensemble : quand un ennemi touche
    un bord, toute la flotte descend et change de sens.
    """

    def __init__(self, wave):
        self.enemies = []
        self.direction = 1
        self.speed = settings.FLEET_SPEED + (wave - 1) * settings.FLEET_SPEED_BONUS
        self.create_enemies()

    def create_enemies(self):
        # un boss en haut au milieu
        boss_x = settings.SCREEN_WIDTH / 2 - settings.BOSS_SIZE / 2
        self.enemies.append(BossEnemy(boss_x, 40))

        # deux lignes de 6 ennemis normaux
        for row in range(2):
            for col in range(6):
                x = 50 + col * 90
                y = 150 + row * 70
                self.enemies.append(BasicEnemy(x, y))

    def update(self):
        # deplacement horizontal
        for enemy in self.enemies:
            enemy.move(self.direction * self.speed, 0)

        # on regarde si un ennemi touche un bord
        touch_edge = False
        for enemy in self.enemies:
            if enemy.x <= 0 or enemy.x + enemy.width >= settings.SCREEN_WIDTH:
                touch_edge = True

        if touch_edge:
            self.direction = -self.direction
            for enemy in self.enemies:
                enemy.move(self.direction * self.speed, settings.FLEET_STEP_DOWN)

    def remove_dead(self):
        self.enemies = [e for e in self.enemies if e.alive]

    def is_empty(self):
        return len(self.enemies) == 0

    def lowest_y(self):
        """Renvoie le bas de l'ennemi le plus bas."""
        lowest = 0
        for enemy in self.enemies:
            if enemy.y + enemy.height > lowest:
                lowest = enemy.y + enemy.height
        return lowest
