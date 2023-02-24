import arcade
from racket import Racket
from ball import Ball


class Game(arcade.Window):
    def __init__(self):
        # Properties
        super().__init__(width = 800, height = 500, title = "Pong 🏓")
        arcade.set_background_color(arcade.color.DARK_GREEN)
        self.player_1 = Racket(40, self.height // 2, arcade.color.PINK_SHERBET, "You")
        self.player_2 = Racket(self.width - 40, self.height // 2, arcade.color.BABY_BLUE, "AI")
        self.ball = Ball(self)

    # Methods
    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_outline(self.width // 2, self.height // 2, self.width - 30, self.height - 30, arcade.color.WHITE, border_width = 10)
        arcade.draw_line(self.width // 2, 30, self.width // 2, self.height - 30, arcade.color.WHITE, line_width = 10)
        arcade.draw_text(f"{self.player_1.name} : {self.player_1.score}", 30, self.height - 45, arcade.color.FLORAL_WHITE, width = 100, font_size = 14, align = "left")
        arcade.draw_text(f"{self.player_2.name} : {self.player_2.score}", self.width - 130, self.height - 45, arcade.color.FLORAL_WHITE, width = 100, font_size = 14, align = "right")
        self.player_1.draw()
        self.player_2.draw()
        self.ball.draw()
        arcade.finish_render()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.player_1.height < y < self.height - self.player_1.height:
            self.player_1.center_y = y

    def on_update(self, delta_time: float):
        self.ball.move()
        self.player_2.move(self, self.ball)

        if self.ball.center_y < 30 or self.ball.center_y > self.height - 30:
            self.ball.change_y *= -1
        if arcade.check_for_collision(self.player_1, self.ball) or arcade.check_for_collision(self.player_2, self.ball):
            self.ball.change_x *= -1
            
        if self.ball.center_x < 0:
            self.player_2.score += 1
            del self.ball
            self.ball = Ball(self)
        if self.ball.center_x > self.width:
            self.player_1.score += 1
            del self.ball
            self.ball = Ball(self)
            

game = Game()
arcade.run()  