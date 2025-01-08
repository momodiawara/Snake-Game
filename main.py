import tkinter as tk
from model import SnakeGameModel
from view import SnakeGameView
from controller import SnakeGameController

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Snake Game")

    grid_size = 20
    model = SnakeGameModel(grid_size)
    model.place_obstacles(2)  # Ajout de 3 obstacles
    view = SnakeGameView(root, grid_size)
    controller = SnakeGameController(model, view)

    root.bind("<KeyPress>", controller.change_direction)

    controller.update()
    root.mainloop()
