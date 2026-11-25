class Entity:
    """Classe mere de tous les objets du jeu.

    Une entite est un rectangle (x, y, largeur, hauteur) qui peut etre
    vivant ou non. Quand alive vaut False, l'objet est supprime du jeu.
    """

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.alive = True

    def update(self):
        """Met a jour l'entite a chaque image. Redefinie dans les classes filles."""
        pass

    def center_x(self):
        return self.x + self.width / 2

    def collides_with(self, other):
        """Renvoie True si les deux rectangles se touchent."""
        return (self.x < other.x + other.width
                and self.x + self.width > other.x
                and self.y < other.y + other.height
                and self.y + self.height > other.y)
