import math
import time
import random
import threading
import arcade
from spaceship import SpaceShip
from enemy import Enemy


class Game(arcade.Window):
    def __init__(self):
        # Properties
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Interstellar Game 🌍🚀")
        arcade.set_background_color(arcade.color.BLACK)
        self.background_image = arcade.load_texture(":resources:images/backgrounds/stars.png")

        self.me = SpaceShip(SCREEN_WIDTH)
        self.enemy_list = []
        self.my_thread = threading.Thread(target = self.add_enemy)
        self.my_thread.start()
        self.end_thread = False

    # Methods
    def add_enemy(self):
        while True:
            self.enemy_list.append(Enemy(SCREEN_WIDTH, SCREEN_HEIGHT))
            time.sleep(3)
            if self.end_thread == True:
                break

    def on_update(self, delta_time: float):
        self.me.rotate()
        factor = 1
        for enemy in self.enemy_list:
            enemy.move(factor)
            factor += 0.5
        for bullet in self.me.bullet_list:
            bullet.move()
        for enemy in self.enemy_list:
            if any (arcade.check_for_collision(enemy, bullet) for bullet in self.me.bullet_list):
                enemy.explosion_sound()
                self.enemy_list.remove(enemy)
                self.me.bullet_list.remove(bullet)
                self.me.score += 1
        if any (enemy.center_y <= 0 for enemy in self.enemy_list):
            self.enemy_list.remove(enemy)
            self.me.life -= 1
        if any (bullet.center_y >= SCREEN_HEIGHT or bullet.center_y <= 0 or bullet.center_x >= SCREEN_WIDTH or bullet.center_x <= 0 for bullet in self.me.bullet_list):
            self.me.bullet_list.remove(bullet)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.me.fire()
            self.me.sound_fire()
        elif symbol == arcade.key.RIGHT:
            self.me.change_angle = -1
        elif symbol == arcade.key.LEFT:
            self.me.change_angle = 1

    def on_key_release(self, symbol: int, modifiers: int):
        self.me.change_angle = 0

    def on_draw(self):
        arcade.start_render()
        if self.me.life <= 0:
            arcade.draw_text("GAME OVER!", (SCREEN_WIDTH // 4), SCREEN_HEIGHT // 2, arcade.color.ORANGE, width = 400, font_size = 40, align = "center")
            self.end_thread = True
        else:
            arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background_image)
            self.me.draw()
            for enemy in self.enemy_list:
                enemy.draw()
            for bullet in self.me.bullet_list:
                bullet.draw()
            arcade.draw_text(f"score : {self.me.score}", SCREEN_WIDTH - 110, 20, arcade.color.RED, width = 100, font_size = 15, align = "center")
            space = 0
            for life in range(self.me.life):
                arcade.draw_texture_rectangle(25 + space, 25, 20, 20, self.me.life_image)
                space += 25


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

game = Game()
game.run()