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
        self.auto_find()
        if arcade.check_for_collision(self.snake, self.apple):
            self.snake.eat("apple")
            self.apple = Apple(SCREEN_WIDTH, SCREEN_HEIGHT)
        elif arcade.check_for_collision(self.snake, self.pear):
            self.snake.eat("pear")
            self.pear = Pear(SCREEN_WIDTH, SCREEN_HEIGHT)
        elif arcade.check_for_collision(self.snake, self.poop):
            self.snake.eat("poop")
            self.poop = Poop(SCREEN_WIDTH, SCREEN_HEIGHT)

    def auto_find(self):
        distance_apple = math.sqrt((self.snake.center_x - self.apple.center_x) ** 2 + (self.snake.center_y - self.apple.center_y) ** 2)
        distance_pear = math.sqrt((self.snake.center_x - self.pear.center_x) ** 2 + (self.snake.center_y - self.pear.center_y) ** 2)
        goal_x = 0
        goal_y = 0
        if distance_apple < distance_pear:
            goal_x = self.apple.center_x
            goal_y = self.apple.center_y
        else:
            goal_x = self.pear.center_x
            goal_y = self.pear.center_y
            
        go_right = True
        go_left = True
        go_up = True
        go_down = True
        if self.snake.center_x < self.poop.center_x and self.snake.center_y == self.poop.center_y:
            go_right = False
        if self.snake.center_x > self.poop.center_x and self.snake.center_y == self.poop.center_y:
            go_left = False
        if self.snake.center_x == self.poop.center_x and self.snake.center_y < self.poop.center_y:
            go_up = False
        if self.snake.center_x == self.poop.center_x and self.snake.center_y > self.poop.center_y:
            go_down = False
        if go_right and self.snake.center_x < goal_x:
            self.snake.change_x = 1
            self.snake.change_y = 0
            self.snake.move()
        elif go_left and self.snake.center_x > goal_x:
            self.snake.change_x = -1
            self.snake.change_y = 0
            self.snake.move()
        elif go_up and self.snake.center_y < goal_y:
            self.snake.change_x = 0
            self.snake.change_y = 1
            self.snake.move()
        elif go_down and self.snake.center_y > goal_y:
            self.snake.change_x = 0
            self.snake.change_y = -1
            self.snake.move()
    

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

my_game = Game()
arcade.run()