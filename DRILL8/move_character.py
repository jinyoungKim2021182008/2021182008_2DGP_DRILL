from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    global status
    global dir_x, dir_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                dir_x += 1
                status = 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                status = 0
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

def animation(x, y, dir_x, dir_y):
    if dir_x == 0 and dir_y == 0:
        character.clip_draw(frame * 100, 200 + status * 100, 100, 100, x, y)
    elif dir_x == 1 or (dir_y != 0 and status == 1):
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    elif dir_x == -1 or (dir_y != 0 and status == 0):
        character.clip_draw(frame * 100, 0, 100, 100, x, y)

open_canvas(TUK_WIDTH, TUK_HEIGHT)
character = load_image('animation_sheet.png')
tuk_ground = load_image('TUK_GROUND.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dir_x, dir_y = 0, 0
status = 0 # 1 = see_right, 0 = see_left

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    animation(x, y, dir_x, dir_y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    if x + dir_x * 5 <= TUK_WIDTH and x + dir_x * 5 >= 0:
        x += dir_x * 5
    if y + dir_y * 5 <= TUK_HEIGHT and y + dir_y * 5 >= 0:
        y += dir_y * 5
    delay(0.01)

close_canvas()

