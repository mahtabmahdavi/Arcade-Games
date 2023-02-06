import math
import arcade


class Bullet(arcade.Sprite):
    def __init__(self, host):
        # Properties
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.angle = host.angle
        self.speed = 6

    # Methods
    def move(self):
        angle = math.radians(self.angle)
        self.center_x -= self.speed * math.sin(angle)
        self.center_y += self.speed * math.cos(angle)