import arcade
from racket import Racket
from ball import Ball
from brick import Brick


class Game(arcade.Window):
    def __init__(self):
        # Properties
        super().__init__(width = 500, height = 500, title = "⚾ Breakout 🧱")
        arcade.set_background_color(arcade.color.BLACK)
        self.background_image = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")

        self.player = Racket(self)
        self.ball = Ball(self)
        self.brick_list = []
        self.create_bricks()

    # Methods
    def on_draw(self):
        arcade.start_render()
        if self.player.life <= 0 or self.player.score < 0:
            arcade.draw_text("GAME OVER!", self.width // 2 - 200, self.height // 2, arcade.color.RED, width = 400, font_size = 36, align = "center")
        else:
            arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background_image)
            self.player.draw()
            self.ball.draw()
            for brick in self.brick_list:
                brick.draw()
            space = 0
            for i in range(self.player.life):
                arcade.draw_texture_rectangle(self.width - (20 + space), self.height - 20, 20, 20, self.player.life_image)
                space += 25
            arcade.draw_text(f"score : {self.player.score}", 10, self.height - 20, arcade.color.FLORAL_WHITE, width = 100, font_size = 12, align = "left")

    def create_bricks(self):
        temp_center_y = self.height - 100
        for i in range(5):
            temp_center_x = 25
            for j in range(self.width // 50):
                if i == 0:
                    self.brick_list.append(Brick(temp_center_x, temp_center_y, arcade.color.GRAY))
                elif i == 1:
                    self.brick_list.append(Brick(temp_center_x, temp_center_y, arcade.color.RED))
                elif i == 2:
                    self.brick_list.append(Brick(temp_center_x, temp_center_y, arcade.color.ORANGE))
                elif i == 3:
                    if j > 0.25 * (self.width // 50) and j < 0.65 * (self.width // 50):
                        self.brick_list.append(Brick(temp_center_x, temp_center_y, arcade.color.GREEN))
                    else:
                        self.brick_list.append(Brick(temp_center_x, temp_center_y, arcade.color.YELLOW))
                temp_center_x += 50
            temp_center_y -= 20

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if (self.player.width // 2) + 5 < x < self.width - (self.player.width // 2) - 5:
            self.player.center_x = x

    def on_key_press(self, symbol: int, modifiers: int):
        if self.player.width // 2 < self.player.center_x < self.width - (self.player.width // 2):
            if symbol == arcade.key.RIGHT:
                self.player.move(self, "RIGHT")
            elif symbol == arcade.key.LEFT:
                self.player.move(self, "LEFT")
    
    def on_update(self, delta_time: float):
        self.ball.move()
        if self.ball.center_x < self.ball.radius or self.ball.center_x > self.width - self.ball.radius:
            self.ball.change_x *= -1
        if self.ball.center_y < 0:
            self.player.score -= 1
            self.player.life -= 1
            del self.ball
            self.ball = Ball(self)
        if self.ball.center_y > self.height:
            self.ball.change_y *= -1
        if arcade.check_for_collision(self.player, self.ball):
            self.ball.change_y *= -1
        for brick in self.brick_list:
            if arcade.check_for_collision(brick, self.ball):
                self.brick_list.remove(brick)
                self.ball.change_y *= -1
                self.player.score += 1
        

game = Game()
arcade.run() 