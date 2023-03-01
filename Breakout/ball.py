import random
import arcade


class Ball(arcade.Sprite):
    def __init__(self, game):
        # Properties
        super().__init__()
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.change_x = random.choice([-1, 1])
        self.change_y = -1
        self.radius = 8
        self.width = self.radius * 2
        self.height = self.radius * 2
        self.color = arcade.color.WHITE
        self.speed = 4

    # Methods
    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)