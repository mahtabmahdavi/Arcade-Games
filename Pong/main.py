import random
import arcade


class Ball(arcade.Sprite):
    def __init__(self, game):
        # Properties
        super().__init__()
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.color = arcade.color.YELLOW_ORANGE
        self.radius = 15
        self.change_x = random.choice([-1, 1])
        self.change_y = random.choice([-1, 1])
        self.width = self.radius * 2
        self.height = self.radius * 2
        self.speed = 5

    # Methods
    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)


class Rocket(arcade.Sprite):
    def __init__(self, center_x, center_y, color, name):
        # Properties
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.color = color
        self.name = name 
        self.change_x = 0
        self.change_y = 0
        self.width = 10
        self.height = 60
        self.speed = 4
        self.score = 0

    # Methods
    def move(self, game, ball):
        if ball.center_x > (game.width // 2):
            if self.center_y > ball.center_y:
                self.change_y = -1

            if self.center_y < ball.center_y:
                self.change_y = 1

            self.center_y += self.change_y * self.speed

            if self.center_y < self.height:
                self.center_y = self.height

            if self.center_y < game.height - self.height:
                self.center_y = game.height - self.height

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)


class Game(arcade.Window):
    def __init__(self):
        # Properties
        super().__init__(width = 800, height = 500, title = "Pong 🏓")
        arcade.set_background_color(arcade.color.DARK_GREEN)
        self.player_1 = Rocket(40, self.height // 2, arcade.color.PINK_SHERBET, "Mahtab")
        self.player_2 = Rocket(self.width - 40, self.height // 2, arcade.color.BABY_BLUE, "Artificial Intelligence")
        self.ball = Ball(self)

    # Methods
    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_outline(self.width // 2, self.height // 2, self.width - 30, self.height - 30, arcade.color.WHITE, border_width = 10)
        arcade.draw_line(self.width // 2, 30, self.width // 2, self.height - 30, arcade.color.WHITE, line_width = 10)
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