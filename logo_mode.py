from pico2d import *

import game_framework
import title_mode

image = None
logo_start_time = 0

def init():
    # 로고 이미지를 로드
    global image, logo_start_time

    image = load_image('tuk_credit.png')
    logo_start_time = get_time()
    pass

def update():
    # 시간 체크를 해주고
    if get_time() - logo_start_time > 2.0:
        game_framework.change_mode(title_mode)

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
    #그리고 아무 처리도 하지 않는다

def pause():
    pass
def resume():
    pass
