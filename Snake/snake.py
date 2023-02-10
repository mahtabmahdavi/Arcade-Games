import arcade


class Snake(arcade.Sprite):
    def __init__(self, width, height):
        # Properties
        super().__init__()
        self.width = 16
        self.height = 16
        self.color_1 = arcade.color.YELLOW_GREEN
        self.color_2 = arcade.color.UFO_GREEN
        self.change_x = 0
        self.change_y = 0
        self.center_x = width // 2
        self.center_y = height // 2
        self.score = 0
        self.speed = 2
        self.body = []

    # Methods
    def move(self):
        self.body.append([self.center_x, self.center_y])
        if len(self.body) > self.score:
            self.body.pop(0)

        if self.change_x > 0:
            self.center_x += self.speed
        elif self.change_x < 0:
            self.center_x -= self.speed

        if self.change_y > 0:
            self.center_y += self.speed
        elif self.change_y < 0:
            self.center_y -= self.speed

    def eat(self, food):
        if food == "apple":
            self.score += 1
        elif food == "pear":
            self.score += 2
        elif food == "poop":
            self.score -= 1

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color_1, 45)
        for i in range(len(self.body)):
            if len(self.body) % 2:
                if i % 2 == 0 :
                    arcade.draw_rectangle_filled(self.body[i][0], self.body[i][1], self.width, self.height, self.color_1)
                else:
                    arcade.draw_rectangle_filled(self.body[i][0], self.body[i][1], self.width, self.height, self.color_2)
            else:
                if i % 2 == 0 :
                    arcade.draw_rectangle_filled(self.body[i][0], self.body[i][1], self.width, self.height, self.color_2)
                else:
                    arcade.draw_rectangle_filled(self.body[i][0], self.body[i][1], self.width, self.height, self.color_1)