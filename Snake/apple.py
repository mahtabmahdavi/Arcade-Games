import random
from fruit import Fruit
from snake import Snake 


class Apple(Fruit):
    def __init__(self, width, height):
        # Properties
        super().__init__("Images/apple.png")
        self.snake = Snake(width, height)
        temp_x = random.randint(0, width // 2) * 2
        temp_y = random.randint(0, height // 2) * 2
        if not any ([temp_x, temp_y] for part in self.snake.body):
            self.center_x = temp_x
            self.center_y = temp_y

    # Methods
    def draw(self):
        super().draw()