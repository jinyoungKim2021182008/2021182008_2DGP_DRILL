from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('cave_man.png')
character_w = character.w // 6
character_h = character.h // 7

def character_animation(ani_len, start_frame ,frame_len, sheet_h, startpos_x, startpos_y , addpos_x, addpos_y):
    x, y = startpos_x, startpos_y
    frame = start_frame
    for i in range(0, ani_len):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * (character_w), sheet_h * (character_h), (character_w), (character_h), startpos_x, startpos_y)
        update_canvas()
        frame = start_frame + (frame + 1) % frame_len
        startpos_x += addpos_x
        startpos_y += addpos_y
        delay(0.1)
        get_events()
    pass

def character_idle():
    character_animation(12, 0, 6, 6, 400, 70, 0, 0)

def character_walk():
    character_animation(18, 0, 6, 5, 300, 70, 10, 0)

def character_jump():
    character_animation(3, 0, 3, 4, 400, 70, 20, 20) #up
    character_animation(4, 3, 3, 4, 460, 130, 20, -20) #down

def character_rolling():
    character_animation(6, 0, 6, 3, 300, 70, 20, 0) #start rolling
    character_animation(6, 3, 3, 3, 420, 70, 20, 0) #keep rolling

def character_attack():
    character_animation(6, 0, 5, 2, 400, 70, 0, 0)

def character_gothit():
    character_animation(6, 0, 6, 1, 400, 70, -15, 0) #got hit
    character_animation(6, 5, 1, 1, 310, 70, 0, 0) #keep down

def character_ladder_climb():
    character_animation(8, 0, 4, 0, 400, 70, 0, 10)

while True:
    character_idle()
    character_walk()
    character_jump()
    character_rolling()
    character_attack()
    character_gothit()
    character_ladder_climb()
close_canvas()
