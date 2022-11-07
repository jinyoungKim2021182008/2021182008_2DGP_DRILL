from pico2d import *
import game_world
import game_framework
import random

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Bird:
    image = None
    image_w, image_h = 0, 0

    def __init__(self):
        self.x, self.y = random.randint(100, 1000), random.randint(200, 450)
        self.frame = random.randint(0, 14)
        self.dir = 1
        if Bird.image is None:
            Bird.image = load_image('bird_animation.png')
            Bird.image_w = self.image.w // 5
            Bird.image_h = self.image.h // 3

    def update(self):
        self.frame = self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time

        if self.dir == 1 and self.x >= 1550:
            self.dir = -1
        if self.dir == -1 and self.x <= 50:
            self.dir = 1

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw((int(self.frame) % 5) * self.image_w,
                                           self.image_h * 2 - (int(self.frame) // 5) * self.image_h,
                                           self.image_w, self.image_h, 0, '', self.x, self.y, 100, 100)
        else:
            self.image.clip_composite_draw((int(self.frame) % 5) * self.image_w,
                                           self.image_h * 2 - (int(self.frame) // 5) * self.image_h,
                                           self.image_w, self.image_h, 0, 'h', self.x, self.y, 100, 100)
