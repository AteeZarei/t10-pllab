import random
import arcade

class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.color = arcade.color.DARK_GREEN
        self.width = 16
        self.height = 16
        self.center_x = 225
        self.center_y = 250

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

    def move(self):
        pass
    def eat(self):
        pass

class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.color = arcade.color.RED
        self.radiaus = 8
        self.center_x = random.randint(0, 450) 
        self.center_y = random.randint(0, 500)

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radiaus, self.color)

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width= 450, height=500, title="Snake Game")
        self.background_color = arcade.color.KHAKI
        self.food = Apple()
        self.player = Snake()

    def on_draw(self):
        arcade.start_render()
        self.food.draw()
        self.player.draw()


g = Game()
arcade.run()


