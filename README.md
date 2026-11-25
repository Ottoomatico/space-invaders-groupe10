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
