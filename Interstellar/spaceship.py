import arcade
from bullet import Bullet


class SpaceShip(arcade.Sprite):
    def __init__(self, width):
        # Properties
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")
        self.width = 48
        self.height = 48
        self.center_x = width // 2
        self.center_y = 32
        self.angle = 0
        self.change_angle = 0
        self.speed = 4
        self.score = 0
        self.life = 3
        self.life_image = arcade.load_texture("Images/heart.png")
        self.bullet_list = []

    # Methods
    def rotate(self):
        self.angle += self.speed * self.change_angle

    def fire(self):
        self.bullet_list.append(Bullet(self))

    def sound_fire(self):
        arcade.play_sound(arcade.sound.Sound(":resources:sounds/laser1.mp3"))