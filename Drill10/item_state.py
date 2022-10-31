from pico2d import *
import game_framework
import play_state

image = None

def enter():
    global image
    image = load_image('add_delete_boy.png')
    pass

def exit():
    global image
    del image
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_EQUALS:
                    play_state.boys.append(play_state.Boy())
                case pico2d.SDLK_MINUS:
                    if len(play_state.boys) > 1:
                        play_state.boys.pop()


def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400,300)
    update_canvas()

def update():
    pass

def pause():

    pass

def resume():

    pass