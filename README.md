# Snake-Game
Un jeu Snake classique développé en Python avec une interface graphique utilisant `tkinter`. Ce projet met en œuvre une architecture MVC (Modèle-Vue-Contrôleur) pour une meilleure organisation et maintenabilité.

## Fonctionnalités

- Contrôles directionnels pour guider le serpent (`↑`, `↓`, `←`, `→`).
- Augmentation progressive de la vitesse lorsque le serpent mange de la nourriture.
- Gestion des collisions avec les murs, le corps du serpent, et des obstacles.
- Affichage du score en temps réel.
- Génération aléatoire d'obstacles pour augmenter la difficulté.

## Prérequis

- Python 3.7 ou supérieur.
- Aucune bibliothèque supplémentaire n'est requise (utilise uniquement `tkinter`, inclus par défaut avec Python).

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/snake-game.git
   cd snake-game

    Exécutez le jeu :

    python main.py

Contrôles du jeu

    Flèches directionnelles : Contrôlez la direction du serpent (Haut, Bas, Gauche, Droite).
    Échap : Quittez le jeu (peut être ajouté dans les améliorations futures).

Structure du projet

├── controller.py     # Contrôleur gérant les interactions utilisateur et la boucle principale.
├── model.py          # Modèle contenant la logique de jeu (mouvement, collisions, obstacles, etc.).
├── view.py           # Vue pour dessiner le serpent, la nourriture, les obstacles et afficher le score.
├── main.py           # Point d'entrée du jeu, reliant le modèle, la vue et le contrôleur.
└── README.md         # Documentation du projet.

Aperçu du Code
Exemple de la logique des collisions (model.py) :

def check_collision(self):
    """Vérifie si le serpent entre en collision avec un mur, lui-même ou un obstacle."""
    head = self.snake[0]

    # Collision avec les murs
    if head[0] < 0 or head[0] >= self.grid_size or head[1] < 0 or head[1] >= self.grid_size:
        return True

    # Collision avec le corps ou un obstacle
    if head in self.snake[1:] or head in self.obstacles:
        return True

    return False

Exemple d'affichage des éléments graphiques (view.py) :

def draw_snake(self, snake):
    """Dessine le serpent sur le canvas."""
    self.canvas.delete("snake")
    for segment in snake:
        x, y = segment
        self.canvas.create_rectangle(
            x * self.cell_size,
            y * self.cell_size,
            (x + 1) * self.cell_size,
            (y + 1) * self.cell_size,
            fill="green",
            tags="snake"
        )
Idées d'améliorations

    Ajouter des niveaux avec des vitesses initiales différentes ou des obstacles dynamiques.
    Ajouter un mode multijoueur.
    Enregistrer les meilleurs scores dans un fichier ou une base de données.
    Ajouter une option pour personnaliser la taille de la grille ou les couleurs.

Contributions

Les contributions sont les bienvenues ! Veuillez soumettre vos propositions via une pull request après avoir consulté les issues ouvertes.

Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, de le modifier et de le distribuer avec attribution.

Auteur

    Mohamed DIAWARA
    Passionné par le développement Python et l'architecture logicielle.
