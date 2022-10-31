from pico2d import *

RD, LD, RU, LU, TIMER, AD = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_a): AD
}


class IDLE:
    @staticmethod
    def enter(self, event):  # 상태에 들어갈 때 행하는 액션
        # print('ENTER IDLE')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        self.timer = 1000

    @staticmethod
    def exit(self):  # 상태를 나올 때 행하는 액션
        # print('EXIT IDLE')
        pass

    @staticmethod
    def do(self):  # 상태에 있을 때 지속적으로 행하는 행위
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            self.que.insert(0, TIMER)

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)


class RUN:
    @staticmethod
    def enter(self, event):  # 상태에 들어갈 때 행하는 액션
        # print('ENTER IDLE')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    @staticmethod
    def exit(self):  # 상태를 나올 때 행하는 액션
        # print('EXIT IDLE')
        self.face_dir = self.dir

    @staticmethod
    def do(self):  # 상태에 있을 때 지속적으로 행하는 행위
        self.frame = (self.frame + 1) % 8
        self.x += self.dir

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)


class AUTO_RUN:
    @staticmethod
    def enter(self, event):  # 상태에 들어갈 때 행하는 액션
        print('ENTER AUTO')
        self.dir = self.face_dir

    @staticmethod
    def exit(self):  # 상태를 나올 때 행하는 액션
        # print('EXIT AUTO')
        self.face_dir = self.dir
        self.dir = 0

    @staticmethod
    def do(self):  # 상태에 있을 때 지속적으로 행하는 행위
        self.frame = (self.frame + 1) % 8
        self.x += self.dir

        if self.x < 30:
            self.dir = 1
        if self.x > 770:
            self.dir = -1

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)


class SLEEP:
    @staticmethod
    def enter(self, event):  # 상태에 들어갈 때 행하는 액션
        # print('ENTER SLEEP')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    @staticmethod
    def exit(self):  # 상태를 나올 때 행하는 액션
        # print('EXIT SLEEP')
        pass

    @staticmethod
    def do(self):  # 상태에 있을 때 지속적으로 행하는 행위
        self.frame = (self.frame + 1) % 8

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                           3.14 / 2, 'h', self.x, self.y - 30, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                           -3.14 / 2, '', self.x, self.y - 30, 100, 100)


next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AD: AUTO_RUN},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, TIMER: RUN, AD: AUTO_RUN},
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AD: SLEEP},
    AUTO_RUN: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: AUTO_RUN, AD: IDLE}
}


class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.que.insert(0, key_event)

    def update(self):
        self.cur_state.do(self)

        if self.que:
            event = self.que.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
