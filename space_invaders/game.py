from space_invaders import settings
from space_invaders.entities.player import Player
from space_invaders.fleet import Fleet
from space_invaders.weapons import SimpleGun, DoubleGun


class Game:
    """Contient l'etat de la partie et les regles du jeu.

    Cette classe n'utilise pas pygame : elle ne dessine rien et ne
    joue aucun son. Elle remplit juste la liste sounds_to_play, et
    c'est main.py qui joue les sons.
    """

    def __init__(self):
        self.weapons = [SimpleGun(), DoubleGun()]
        self.restart()

    def restart(self):
        self.player = Player(self.weapons[0])
        self.wave = 1
        self.fleet = Fleet(self.wave)
        self.projectiles = []
        self.score = 0
        self.game_over = False
        self.sounds_to_play = []

    def player_shoot(self):
        if self.game_over:
            return
        new_projectiles = self.player.shoot()
        if len(new_projectiles) > 0:
            self.projectiles.extend(new_projectiles)
            self.sounds_to_play.append("laser")

    def change_weapon(self, index):
        """index commence a 0 (touche 1 = arme 0)."""
        if 0 <= index < len(self.weapons):
            self.player.set_weapon(self.weapons[index])

    def update(self):
        if self.game_over:
            return

        self.player.update()
        for projectile in self.projectiles:
            projectile.update()
        self.fleet.update()

        self.check_collisions()

        # on enleve les objets morts
        self.projectiles = [p for p in self.projectiles if p.alive]
        self.fleet.remove_dead()

        # nouvelle vague quand tous les ennemis sont detruits
        if self.fleet.is_empty():
            self.wave += 1
            self.fleet = Fleet(self.wave)

        # perdu si les ennemis arrivent au niveau du joueur
        if self.fleet.lowest_y() >= settings.PLAYER_Y:
            self.game_over = True

    def check_collisions(self):
        for projectile in self.projectiles:
            for enemy in self.fleet.enemies:
                if projectile.alive and enemy.alive and projectile.collides_with(enemy):
                    projectile.alive = False
                    enemy.take_damage(projectile.damage)
                    if not enemy.alive:
                        self.score += enemy.points
                        self.sounds_to_play.append("explosion")
