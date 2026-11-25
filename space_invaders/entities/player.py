from space_invaders import settings
from space_invaders.entities.entity import Entity


class Player(Entity):
    """Le vaisseau du joueur.

    Le joueur possede une arme (composition) : c'est l'arme qui
    decide comment on tire. On peut donc changer d'arme sans
    modifier cette classe.
    """

    def __init__(self, weapon):
        x = settings.SCREEN_WIDTH / 2 - settings.PLAYER_SIZE / 2
        super().__init__(x, settings.PLAYER_Y, settings.PLAYER_SIZE, settings.PLAYER_SIZE)
        self.speed = settings.PLAYER_SPEED
        self.direction = 0  # -1 = gauche, 0 = immobile, 1 = droite
        self.weapon = weapon

    def update(self):
        self.x += self.direction * self.speed

        # on empeche le vaisseau de sortir de l'ecran
        if self.x < 0:
            self.x = 0
        if self.x > settings.SCREEN_WIDTH - self.width:
            self.x = settings.SCREEN_WIDTH - self.width

        self.weapon.update()

    def shoot(self):
        """Tire avec l'arme actuelle. Renvoie une liste de projectiles."""
        return self.weapon.fire(self.center_x(), self.y)

    def set_weapon(self, weapon):
        self.weapon = weapon
