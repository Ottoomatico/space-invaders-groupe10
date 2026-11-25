# Space Invaders – Groupe 10

Projet de programmation orientée objet : une version de **Space Invaders** en Python avec Pygame.

On est partis du code de [attreyabhatt/Space-Invaders-Pygame](https://github.com/attreyabhatt/Space-Invaders-Pygame), qu'on a réorganisé en classes, modules et packages.

## Installation

Il faut **Python 3.8 ou plus récent**.

1. Récupérer le projet :
   ```bash
   git clone https://github.com/Ottoomatico/space-invaders-groupe10.git
   cd space-invaders-groupe10
   ```

2. (Conseillé) Créer un environnement virtuel :
   ```bash
   python -m venv venv
   ```
   Puis l'activer :
   - Windows : `venv\Scripts\activate`
   - macOS / Linux : `source venv/bin/activate`

3. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Lancer le jeu

Depuis le dossier du projet :
```bash
python main.py
```
(sur macOS / Linux, ce sera peut-être `python3 main.py`)

## Commandes

| Touche | Action |
|---|---|
| ← / → | Se déplacer |
| Espace | Tirer (on peut rester appuyé) |
| 1 | Arme : tir simple |
| 2 | Arme : tir double |
| R | Rejouer après un game over |
| Échap | Quitter |

## Règles

- Détruire tous les ennemis fait apparaître une nouvelle vague, un peu plus rapide.
- La partie est perdue quand les ennemis arrivent au niveau du vaisseau.
- Ennemi normal : 1 point de vie, 10 points.
- Boss : plus gros, 3 points de vie (barre verte au-dessus), 50 points.
- Tir simple : 1 balle, recharge rapide.
- Tir double : 2 balles, recharge plus lente.

## Organisation du code

```
space-invaders-groupe10/
├── main.py                  # point d'entrée : boucle du jeu + clavier
├── requirements.txt
├── assets/
│   ├── images/              # images du jeu
│   └── sounds/              # sons et musique
└── space_invaders/
    ├── settings.py          # toutes les constantes (taille écran, vitesses...)
    ├── game.py              # Game : état de la partie, collisions, score
    ├── fleet.py             # Fleet : la flotte d'ennemis et son déplacement
    ├── weapons.py           # Weapon, SimpleGun, DoubleGun
    ├── entities/            # les objets du jeu (sans pygame)
    │   ├── entity.py        # Entity : classe mère (position, taille, collision)
    │   ├── player.py        # Player
    │   ├── enemies.py       # Enemy, BasicEnemy, BossEnemy
    │   └── projectiles.py   # Projectile, Bullet
    └── view/                # tout ce qui utilise pygame
        ├── renderer.py      # Renderer : dessine le jeu
        └── sounds.py        # SoundManager : joue les sons
```

L'idée principale : **la logique du jeu ne dépend pas de pygame**. Les classes de `entities/`, `game.py`, `fleet.py` et `weapons.py` ne font que des calculs (positions, points de vie, score). Seul le dossier `view/` (et `main.py`) utilise pygame pour l'affichage, le son et le clavier.

## Ajouter du contenu

### Un nouvel ennemi
Dans `space_invaders/entities/enemies.py`, créer une classe fille de `Enemy` :
```python
class TankEnemy(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, settings.ENEMY_SIZE, hp=2, points=20, image_name="enemy")
```
Ensuite l'ajouter dans `Fleet.create_enemies()` (`fleet.py`). Si on veut une nouvelle image, il faut aussi l'ajouter dans le dictionnaire `images` de `view/renderer.py`.

### Une nouvelle arme
Dans `space_invaders/weapons.py`, créer une classe fille de `Weapon` et écrire `create_projectiles()` :
```python
class TripleGun(Weapon):
    def __init__(self):
        super().__init__("Tir triple", cooldown=45)

    def create_projectiles(self, x, y):
        return [Bullet(x - 46, y), Bullet(x - 16, y), Bullet(x + 14, y)]
```
Puis l'ajouter dans la liste `self.weapons` de `Game` (`game.py`) et ajouter une touche dans `main.py`.

### Un nouveau projectile
Créer une classe fille de `Projectile` dans `entities/projectiles.py` (par exemple avec plus de dégâts ou une autre vitesse) et l'utiliser dans une arme.

## Crédits

Images et sons repris du projet d'origine [attreyabhatt/Space-Invaders-Pygame](https://github.com/attreyabhatt/Space-Invaders-Pygame).
