import tkinter as tk

class SnakeGameView:
    def __init__(self, root, grid_size):
        self.grid_size = grid_size
        self.cell_size = 20  # Taille de chaque cellule
        self.canvas = tk.Canvas(root, width=self.grid_size * self.cell_size, height=self.grid_size * self.cell_size, bg="black")
        self.canvas.pack()

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

    def draw_obstacles(self, obstacles):
        """Dessine les obstacles sur le canvas."""
        self.canvas.delete("obstacles")
        for obstacle in obstacles:
            x, y = obstacle
            self.canvas.create_rectangle(
                x * self.cell_size,
                y * self.cell_size,
                (x + 1) * self.cell_size,
                (y + 1) * self.cell_size,
                fill="gray",
                tags="obstacles"
            )

    def draw_food(self, food):
        """Dessine la nourriture sur le canvas."""
        self.canvas.delete("food")
        x, y = food
        self.canvas.create_oval(
            x * self.cell_size,
            y * self.cell_size,
            (x + 1) * self.cell_size,
            (y + 1) * self.cell_size,
            fill="red",
            tags="food"
        )

    def update_score(self, score):
        """Affiche le score dans la fenêtre."""
        self.canvas.delete("score")
        self.canvas.create_text(
            10, 10, anchor="nw", fill="white", text=f"Score: {score}", font=("Arial", 14), tags="score"
        )
