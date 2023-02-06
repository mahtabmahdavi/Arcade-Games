import random
import arcade


class Enemy(arcade.Sprite):
    def __init__(self, width, height):
        # Properties
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.width = 48
        self.height = 48
        self.center_x = random.randint(self.width, width - self.width)
        self.center_y = height + self.height // 2
        self.speed = 4

    # Methods   
    def move(self, factor):
        self.center_y -= self.speed * factor

    def explosion_sound(self):
        arcade.play_sound(arcade.sound.Sound(":resources:sounds/explosion1.wav"))