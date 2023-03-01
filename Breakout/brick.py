import arcade

class Brick(arcade.Sprite):
    def __init__(self, center_x, center_y, color):
        # Properties
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.width = 40
        self.height = 15
        self.color = color

    # Methods
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)