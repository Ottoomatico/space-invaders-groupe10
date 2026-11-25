from space_invaders import settings
from space_invaders.entities.entity import Entity


class Enemy(Entity):
    """Classe mere des ennemis.

    Chaque ennemi a des points de vie, rapporte des points quand il
    est detruit et a un nom d'image (utilise par l'affichage).
    Le deplacement est gere par la flotte (voir fleet.py).
    """

    def __init__(self, x, y, size, hp, points, image_name):
        super().__init__(x, y, size, size)
        self.max_hp = hp
        self.hp = hp
        self.points = points
        self.image_name = image_name

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.alive = False


class BasicEnemy(Enemy):
    """Ennemi de base : 1 point de vie."""

    def __init__(self, x, y):
        super().__init__(x, y, settings.ENEMY_SIZE, hp=1, points=10, image_name="enemy")


class BossEnemy(Enemy):
    """Boss : plus gros, 3 points de vie et rapporte plus de points."""

    def __init__(self, x, y):
        super().__init__(x, y, settings.BOSS_SIZE, hp=3, points=50, image_name="boss")
