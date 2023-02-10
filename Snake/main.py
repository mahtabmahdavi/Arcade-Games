import math
import arcade
from snake import Snake
from apple import Apple
from pear import Pear
from poop import Poop


class Game(arcade.Window):
    def __init__(self):
        # Properties
        super().__init__(width = SCREEN_WIDTH, height = SCREEN_HEIGHT, title = "Snake Game 🍎🐍")
        arcade.set_background_color(arcade.color.BLACK)
        self.background_image = arcade.load_texture("Images/sand.jpg")
        self.snake = Snake(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.apple = Apple(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.pear = Pear(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.poop = Poop(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Methods
    def on_draw(self):
        arcade.start_render()
        if self.snake.score < 0 or  self.snake.center_x < 0 or self.snake.center_x > SCREEN_WIDTH or self.snake.center_y < 0 or self.snake.center_y > SCREEN_HEIGHT:
            arcade.draw_text("Game Over!", (SCREEN_WIDTH // 4) - 40, SCREEN_HEIGHT // 2, arcade.color.RED, width = 400, font_size = 40, align = "left")
        else:
            arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background_image)
            self.snake.draw()
            self.apple.draw()
            self.pear.draw()
            self.poop.draw()
            arcade.draw_text(f"SCORE : {self.snake.score}", 5, SCREEN_HEIGHT - 20, arcade.color.BLACK, width = 100, font_size = 14, align = "left")
        
    def on_update(self, delta_time: float):
        self.snake.move()
        if arcade.check_for_collision(self.snake, self.apple):
            self.snake.eat("apple")
            self.apple = Apple(SCREEN_WIDTH, SCREEN_HEIGHT)
        elif arcade.check_for_collision(self.snake, self.pear):
            self.snake.eat("pear")
            self.pear = Pear(SCREEN_WIDTH, SCREEN_HEIGHT)
        elif arcade.check_for_collision(self.snake, self.poop):
            self.snake.eat("poop")
            self.poop = Poop(SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif key == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0
        elif key == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif key == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

my_game = Game()
arcade.run()