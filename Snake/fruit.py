import arcade


class Fruit(arcade.Sprite):
    def __init__(self, image_path):
        # Properties
        super().__init__()
        self.width = 16
        self.height = 16
        self.image = arcade.load_texture(image_path)

    # Methods
    def draw(self):
        arcade.draw_texture_rectangle(self.center_x, self.center_y, 30, 30, self.image)