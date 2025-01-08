import random

class SnakeGameModel:
    def __init__(self, grid_size=20):
        self.grid_size = grid_size
        self.snake = [(5, 5), (4, 5), (3, 5)]  # Position initiale du snake
        self.food = (10, 10)                   # Position initiale de la nourriture
        self.direction = "RIGHT"               # Direction initiale
        self.score = 0                         # Score initial
        self.obstacles = []                    # Liste des obstacles


    def place_obstacles(self, num_obstacles=2):
        """Place un certain nombre d'obstacles sur la grille."""      
        for _ in range(num_obstacles):
            while True:
                obstacle = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
                if obstacle not in self.snake and obstacle != self.food and obstacle not in self.obstacles:
                    self.obstacles.append(obstacle)
                    break
                
    def move_snake(self):
        """Met à jour la position du serpent en fonction de la direction."""
        head_x, head_y = self.snake[0]

        if self.direction == "UP":
            new_head = (head_x, head_y - 1)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + 1)
        elif self.direction == "LEFT":
            new_head = (head_x - 1, head_y)
        elif self.direction == "RIGHT":
            new_head = (head_x + 1, head_y)

        self.snake = [new_head] + self.snake[:-1]

    def check_collision(self):
        """Vérifie si le serpent entre en collision avec un mur, lui-même ou un obstacle."""
        head = self.snake[0]

        # Collision avec les murs
        if head[0] < 0 or head[0] >= self.grid_size or head[1] < 0 or head[1] >= self.grid_size:
            return True

        # Collision avec le corps
        if head in self.snake[1:] or head in self.obstacles:
            return True

        return False

    def check_food(self):
        """Vérifie si le serpent a mangé la nourriture."""
        if self.snake[0] == self.food:
            self.snake.append(self.snake[-1])  # Allonge le serpent
            self.score += 10                   # Augmente le score
            return True
        return False

    def place_food(self):
        """Place la nourriture à un nouvel emplacement."""
        import random
        while True:
            new_food = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
            if new_food not in self.snake:
                self.food = new_food
                break
