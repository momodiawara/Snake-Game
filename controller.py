class SnakeGameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.running = True
        self.speed = 150  # Vitesse initiale en ms (100ms = rapide, 200ms = plus lent)

    def change_direction(self, event):
        """Change la direction du serpent en fonction de l'entrée utilisateur."""
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            self.model.direction = event.keysym.upper()

    def update(self):

        """Met à jour le jeu (boucle principale)."""
        if not self.running:
            return

        self.model.move_snake()

        # Vérifie les collisions avec les murs ou le serpent
        if self.model.check_collision():
            self.running = False
            print("Game Over")
            return

        # Vérifie si le serpent mange la nourriture
        if self.model.check_food():
            self.model.place_food()
            
            # Réduit le délai pour augmenter la vitesse du jeu
            if self.speed > 50:  # Limite minimale de vitesse
                self.speed -= 10

        # Vue : Dessiner les éléments du jeu
        self.view.draw_snake(self.model.snake)
        self.view.draw_food(self.model.food)
        self.view.draw_obstacles(self.model.obstacles)  # Dessine les obstacles
        self.view.update_score(self.model.score)

        # Planifie la prochaine mise à jour
        self.view.canvas.after(self.speed, self.update)
