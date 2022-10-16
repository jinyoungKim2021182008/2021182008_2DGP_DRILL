from pico2d import *
import game_framework
import item_state
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(10, 300), 90
        self.frame = 0
        self.dir = 1 # 오른쪽
        self.image = load_image('animation_sheet.png')
        self.item = None

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 2
        if self.x > 800:
            self.x = 800
            self.dir = -1 #왼쪽
        elif self.x < 0:
            self.x = 0
            self.dir = 1

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        if self.item == 'BigBall':
            self.big_ball_image.draw(self.x + 10, self.y + 50)
        elif self.item == 'Ball':
            self.ball_image.draw(self.x + 10, self.y + 50)



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_b:
                game_framework.push_state(item_state)
    delay(0.01)

boys = []
grass = None
running = True

# 초기화
def enter():
    global boys, grass, running
    boys.append(Boy())
    grass = Grass()
    running = True

# finalization code
def exit():
    global boys, grass
    del boys
    del grass

def update():
    for boy in boys:
        boy.update()

def draw_world():
    grass.draw()
    for boy in boys:
        boy.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def test_self():
    import sys
    pico2d.open_canvas()
    game_framework.run(sys.modules['__main__'])
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()

def pause():

    pass

def resume():

    pass

