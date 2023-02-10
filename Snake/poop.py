import random
from fruit import Fruit
from pear import Pear


class Poop(Fruit):
    def __init__(self, width, height):
        # Properties
        # Properties
        super().__init__("Images/poop.png")
        self.pear = Pear(width, height)
        temp_x = random.randint(0, width // 2) * 2
        temp_y = random.randint(0, height // 2) * 2
        if temp_x != self.pear.center_x or temp_y != self.pear.center_y:
            self.center_x = temp_x
            self.center_y = temp_y
        
    # Methods
    def draw(self):
        super().draw()