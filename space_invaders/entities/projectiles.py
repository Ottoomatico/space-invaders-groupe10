from space_invaders import settings
from space_invaders.entities.entity import Entity


class Projectile(Entity):
    """Classe mere des projectiles : ils montent tout droit."""

    def __init__(self, x, y, width, height, speed, damage, image_name):
        super().__init__(x, y, width, height)
        self.speed = speed
        self.damage = damage
        self.image_name = image_name

    def update(self):
        self.y -= self.speed
        # si le projectile sort de l'ecran on le supprime
        if self.y + self.height < 0:
            self.alive = False


class Bullet(Projectile):
    """Balle classique : 1 degat."""

    def __init__(self, x, y):
        super().__init__(x, y, settings.BULLET_SIZE, settings.BULLET_SIZE,
                         speed=settings.BULLET_SPEED, damage=1, image_name="bullet")
