import arcade


class Racket(arcade.Sprite):
    def __init__(self, game):
        # Properties
        super().__init__()
        self.center_x = game.width // 2
        self.center_y = 20
        self.change_x = 2
        self.width = 80
        self.height = 20
        self.color = arcade.color.PINK_SHERBET
        self.speed = 100
        self.score = 0
        self.life = 3
        self.life_image = arcade.load_texture("Images/heart.png")

    # Methods
    def move(self, game, mode):
        if mode == "RIGHT":
            if self.center_x + self.speed < game.width - 5:
                self.center_x += self.change_x * self.speed
        elif mode == "LEFT":
            if self.center_x - self.speed > 5:
                self.center_x -= self.change_x * self.speed

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)