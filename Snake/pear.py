import random
from fruit import Fruit
from apple import Apple


class Pear(Fruit):
    def __init__(self, width, height):
        # Properties
        super().__init__("Images/pear.png")
        self.apple = Apple(width, height)
        temp_x = random.randint(0, width // 2) * 2
        temp_y = random.randint(0, height // 2) * 2
        if temp_x != self.apple.center_x or temp_y != self.apple.center_y:
            self.center_x = temp_x
            self.center_y = temp_y

    # Methods
    def draw(self):
        super().draw()