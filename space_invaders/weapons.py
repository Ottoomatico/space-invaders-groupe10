"""Les armes du joueur.

Pour ajouter une arme il suffit de creer une classe fille de Weapon
et de redefinir create_projectiles().
"""
from space_invaders import settings
from space_invaders.entities.projectiles import Bullet


class Weapon:
    """Classe mere des armes.

    cooldown = nombre d'images a attendre entre deux tirs.
    """

    def __init__(self, name, cooldown):
        self.name = name
        self.cooldown = cooldown
        self.timer = 0

    def update(self):
        if self.timer > 0:
            self.timer -= 1

    def fire(self, x, y):
        """Tire si l'arme est prete. x est le centre du vaisseau."""
        if self.timer > 0:
            return []
        self.timer = self.cooldown
        return self.create_projectiles(x, y)

    def create_projectiles(self, x, y):
        raise NotImplementedError("chaque arme doit definir create_projectiles")


class SimpleGun(Weapon):
    """Tire une seule balle, assez rapidement."""

    def __init__(self):
        super().__init__("Tir simple", cooldown=20)

    def create_projectiles(self, x, y):
        return [Bullet(x - settings.BULLET_SIZE / 2, y)]


class DoubleGun(Weapon):
    """Tire deux balles cote a cote, mais recharge plus lentement."""

    def __init__(self):
        super().__init__("Tir double", cooldown=35)

    def create_projectiles(self, x, y):
        gap = 18
        left = Bullet(x - settings.BULLET_SIZE / 2 - gap, y)
        right = Bullet(x - settings.BULLET_SIZE / 2 + gap, y)
        return [left, right]
