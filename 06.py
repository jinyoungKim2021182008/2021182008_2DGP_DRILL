from pico2d import *
import math
import os

motion = 0 # 0 = rect, 1 = cir
x = 400
y = 90
r = 210
angle = 0
cir_x = 400
cir_y = 300

open_canvas()
os.chdir('d:\kimcode\d06\image')
grass = load_image('grass.png')
character = load_image('character.png')

while (True):
    if(motion == 0):
        while (x < 770):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x += 5
            delay(0.01)
        while (y < 550):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y += 5
            delay(0.01)
        while (x > 30):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x -= 5
            delay(0.01)
        while (y > 90):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y -= 5
            delay(0.01)
        while (x < 400):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x += 5
            delay(0.01)
            
    elif(motion == 1):
        while (angle < 2 * math.pi):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(cir_x - r * math.sin(angle), cir_y - r * math.cos(angle))
            angle += 0.03
            delay(0.01)
        angle = 0
        
    motion = 1 - motion


close_canvas()
