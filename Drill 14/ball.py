from pico2d import *
import random
import server
import game_world

class Ball:

    def __init__(self):
        self.x, self.y = random.randint(50, 1750), random.randint(50, 1000)
        self.image = load_image('ball21x21.png')

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x - server.background.window_left, self.y - server.background.window_bottom)

    def handle_collision(self, other, group):
        if group == 'BB':
            game_world.remove_object(self)
