from pico2d import *

import game_framework
import play_mode

image = None

def init():
    # 로고 이미지를 로드
    global image, logo_start_time

    image = load_image('title.png')
    pass

def update():
    pass

def draw():
    # 로고 이미지를 그려준다
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    pass

def finish():
    global image
    del image
    pass

def handle_events():
    event_list = get_events() #현재 까지 들어온 이벤트들을 받아온다

    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(play_mode)


def pause():
    pass
def resume():
    pass