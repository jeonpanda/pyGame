##########################################
# 던전 들어가면 플레이어는 좌우로만 움직임
# 보스가 위에서 무언가(돌, 불 등등)를 던지며 아래로 공격을 함
# 캐릭터는 스페이스를 누르면 일자로 나가는 무기를 위로 날림
#(화살표위 키를 누를수록 파워가 강해짐(max = 25 #단, 공격력이 끝까지 찬 후 공격시 +5대미지 추가))
# 플레이어는 공격을 피하면서 보스의 를 공격해야함
# 보스의 피는 조금씩 깎이며 플레이어는 목숨 4개를 가지고 있음
# 4개를 다 쓰면 게임오버가 되며 던전에서 나와짐
# 4개의 던전을 모두 클리어하면 게임이 끝남
# 보스를 잡을때마다 하트가 초기화됨
# 보스를 잡을때마다 코인, 점수 줌
# 얻은 코인으로 상점에서 능력치 구매 가능
# (캐릭터 속도 x 2 / 체력 + 2 / 파워 x 1.5 / 대쉬)
##########################################



import pygame
import os
import random

# 현재 위치 정의
current_path = os.path.dirname(__file__)

# 이미지 폴더 위치 정의
image_path = os.path.join(current_path, "image")

#화면크기
screen_width = 480
screen_height = 640
screen=pygame.display.set_mode((screen_width, screen_height))
# FPS
clock = pygame.time.Clock()

#타이틀
pygame.display.set_caption("jeonyunseong")
#배경이미지
background = pygame.image.load(os.path.join(image_path, "background.png"))
background_text = pygame.image.load(os.path.join(image_path, "background_text.png"))
boss_ui = pygame.image.load(os.path.join(image_path, "boss_ui.png"))
#던전배경이미지
boss1_b = pygame.image.load(os.path.join(image_path, "boss1_b.png"))
boss2_b = pygame.image.load(os.path.join(image_path, "boss2_b.png"))
boss3_b = pygame.image.load(os.path.join(image_path, "boss3_b.png"))

#상점 이미지
shop = pygame.image.load(os.path.join(image_path, "shop.png"))
shop1 = pygame.image.load(os.path.join(image_path, "shop_ui1.png"))
shop2 = pygame.image.load(os.path.join(image_path, "shop_ui2.png"))
shop3 = pygame.image.load(os.path.join(image_path, "shop_ui3.png"))
shop4 = pygame.image.load(os.path.join(image_path, "shop_ui4.png"))
shop5 = pygame.image.load(os.path.join(image_path, "shop_ui5.png"))
shop_b = pygame.image.load(os.path.join(image_path, "shop_ui_b.png"))
shop_speed = pygame.image.load(os.path.join(image_path, "shop_speed.png"))
shop_heart = pygame.image.load(os.path.join(image_path, "shop_heart.png"))
shop_power = pygame.image.load(os.path.join(image_path, "shop_power.png"))
shop_heal = pygame.image.load(os.path.join(image_path, "shop_heal.png"))
shop_weapon = pygame.image.load(os.path.join(image_path, "shop_weapon.png"))
shop_speed_f = pygame.image.load(os.path.join(image_path, "shop_speed_f.png"))
shop_heart_f = pygame.image.load(os.path.join(image_path, "shop_heart_f.png"))
shop_power_f = pygame.image.load(os.path.join(image_path, "shop_power_f.png"))
shop_heal_f = pygame.image.load(os.path.join(image_path, "shop_heal_f.png"))
shop_weapon_f = pygame.image.load(os.path.join(image_path, "shop_weapon_f.png"))
shop_buy1_img = pygame.image.load(os.path.join(image_path, "shop_buy.png"))
shop_buy2_img = pygame.image.load(os.path.join(image_path, "shop_buy.png"))
shop_buy3_img = pygame.image.load(os.path.join(image_path, "shop_buy.png"))
shop_buy4_img = pygame.image.load(os.path.join(image_path, "shop_buy.png"))
shop_buy5_img = pygame.image.load(os.path.join(image_path, "shop_buy.png"))



#캐릭터이미지
character = pygame.image.load(os.path.join(image_path, "character.png"))
down = pygame.image.load(os.path.join(image_path, "down.png"))
up = pygame.image.load(os.path.join(image_path, "up.png"))
left = pygame.image.load(os.path.join(image_path, "left.png"))
right = pygame.image.load(os.path.join(image_path, "right.png"))
stop = pygame.image.load(os.path.join(image_path, "stop.png"))
character_stop_hit = pygame.image.load(os.path.join(image_path, "stop_hit.png"))

#보스이미지
boss1 = pygame.image.load(os.path.join(image_path, "boss1.png"))
boss2 = pygame.image.load(os.path.join(image_path, "boss2.png"))
boss3 = pygame.image.load(os.path.join(image_path, "boss3.png"))
#보스맞은 이미지
boss1_hit = pygame.image.load(os.path.join(image_path, "boss1_hit.png"))
boss2_hit = pygame.image.load(os.path.join(image_path, "boss2_hit.png"))
boss3_hit = pygame.image.load(os.path.join(image_path, "boss3_hit.png"))

#무기이미지
weapon = pygame.image.load(os.path.join(image_path, "character_w.png"))
boss1_w = pygame.image.load(os.path.join(image_path, "boss1_w.png"))
boss2_w = pygame.image.load(os.path.join(image_path, "boss2_w.png"))
boss3_w = pygame.image.load(os.path.join(image_path, "boss3_w.png"))

#게이지이미지
gauge = pygame.image.load(os.path.join(image_path, "gauge.png"))
gauge1 = pygame.image.load(os.path.join(image_path, "gauge1.png"))
gauge2 = pygame.image.load(os.path.join(image_path, "gauge2.png"))
gauge3 = pygame.image.load(os.path.join(image_path, "gauge3.png"))
gauge4 = pygame.image.load(os.path.join(image_path, "gauge4.png"))
gauge5 = pygame.image.load(os.path.join(image_path, "gauge5.png"))
gauge6 = pygame.image.load(os.path.join(image_path, "gauge6.png"))
gaugemax = pygame.image.load(os.path.join(image_path, "gauge_max.png"))

#HP바 이미지
boss_hp_bar = pygame.image.load(os.path.join(image_path, "boss_hp_bar.png"))
hp_bar_b = pygame.image.load(os.path.join(image_path, "hp_bar_b.png"))
hp_bar_b.set_alpha(0)

#캐릭터hp
character_hp0 = pygame.image.load(os.path.join(image_path, "hp0.png"))
character_hp1 = pygame.image.load(os.path.join(image_path, "hp1.png"))
character_hp2 = pygame.image.load(os.path.join(image_path, "hp2.png"))
character_hp3 = pygame.image.load(os.path.join(image_path, "hp3.png"))
character_hp4 = pygame.image.load(os.path.join(image_path, "hp4.png"))
plus_hp2 = pygame.image.load(os.path.join(image_path, "plus_hp2.png"))
plus_hp1 = pygame.image.load(os.path.join(image_path, "plus_hp1.png"))
plus_hp0 = pygame.image.load(os.path.join(image_path, "plus_hp0.png"))
hp_heal = 0

#우승/패배
win_image = pygame.image.load(os.path.join(image_path, "win_image.png"))
lose_image = pygame.image.load(os.path.join(image_path, "lose_image.png"))
win_image_time = 0
lose_image_time = 0
win_image.set_alpha(0)
lose_image.set_alpha(0)
win1 = False
win2 = False
win3 = False
lose = False

#게이지/hp바 투명
boss_hp_bar.set_alpha(0)
gauge.set_alpha(0)
gauge1.set_alpha(0)
gauge2.set_alpha(0)
gauge3.set_alpha(0)
gauge4.set_alpha(0)
gauge5.set_alpha(0)
gauge6.set_alpha(0)
gaugemax.set_alpha(0)

#hp바 크기
hp_bar_size = boss_hp_bar.get_rect().size #hp바 이미지 사이즈
hp_bar_width = hp_bar_size[0] #hp바 가로크기
hp_bar_height = hp_bar_size[1] #hp바 세로크기
hp_bar_x_pos = (screen_width / 2) - (hp_bar_width / 2) #hp바 x좌표 설정 (화면 가운데)
hp_bar_y_pos = screen_height - hp_bar_height - 20 #hp바 y좌표 설정


#캐릭터위치
character_size = character.get_rect().size #캐릭터 이미지 사이즈
character_width = character_size[0] #캐릭터 가로크기
character_height = character_size[1] #캐릭터 가로크기
character_x_pos = (screen_width / 2) - (character_width / 2) #캐릭터 x좌표 설정 (화면 가운데)
character_y_pos = screen_height - character_height #캐릭터 y좌표 설정

#보스1
boss1_size = boss1.get_rect().size #보스1 이미지 사이즈
boss1_width = boss1_size[0] #보스1 가로크기
boss1_height = boss1_size[1] #보스1 세로크기
boss1_x_pos = (screen_width / 2) - (boss1_width / 2) #보스1 x좌표 설정 (화면 가운데) / 좌우로 움직이는 변수
boss1_y_pos = screen_height - 640 #보스1 y좌표 설정 / 상하로 움직이는 변수
a = 0 #보스의 좌우 랜덤 움직임을 위해 0또는 1이 들어갈 자리
boss1_hp = 100 #보스1 체력
boss1_time = 0 #걸린 시간
#보스1 무기
boss1_w_size = boss1_w.get_rect().size #보스1무기 이미지 사이즈
boss1_w_width = boss1_w_size[0] #보스1무기 가로크기
boss1_w_height = boss1_w_size[1] #보스1무기 세로크기
boss1_ws=[] #보스1무기 리스트
boss1_w_x_pos = boss1_x_pos #보스1무기 x좌표 설정 / 좌우로 움직이는 변수
boss1_w_y_pos = boss1_y_pos #보스1무기 y좌표 설정 / 상하로 움직이는 변수
boss1_attack = False #보스 공격 0으로 설정
boss1_attack_time = 0 #보스 공격 쿨타임 0으로 설정
boss1_attack_random = random.randrange(120,240) #보스공격 쿨 60~180틱(2~4초) 사이로 설정
boss1_w_speed = -10 #보스무기 속도 10으로 설정
b1_hit = 0 #보스 맞음
boss1_hit.set_alpha(0) #보스맞은 이미지 가리기
boss1_w_remove = -1 #보스무기 지우기

#보스2
boss2_size = boss2.get_rect().size
boss2_width = boss2_size[0]
boss2_height = boss2_size[1]
boss2_x_pos = (screen_width / 2) - (boss2_width / 2)
boss2_y_pos = screen_height - 640
a = 0
boss2_hp = 300
boss2_time = 0
#보스2 무기
boss2_w_size = boss2_w.get_rect().size
boss2_w_width = boss2_w_size[0]
boss2_w_height = boss2_w_size[1]
boss2_ws=[]
boss2_w_x_pos = boss2_x_pos
boss2_w_y_pos = boss2_y_pos
boss2_attack = False
boss2_attack_time = 0 
boss2_attack_random = random.randrange(60,100) 
boss2_w_speed = -10
b2_hit = 0
boss2_hit.set_alpha(0)
boss2_w_remove = -1


#보스3
boss3_size = boss3.get_rect().size
boss3_width = boss3_size[0]
boss3_height = boss3_size[1]
boss3_x_pos = (screen_width / 2) - (boss3_width / 2)
boss3_y_pos = screen_height - 640
a = 0
boss3_hp = 300
boss3_time = 0
#보스3 무기
boss3_w_size = boss3_w.get_rect().size
boss3_w_width = boss3_w_size[0]
boss3_w_height = boss3_w_size[1]
boss3_ws=[]
boss3_w_x_pos = boss3_x_pos
boss3_w_y_pos = boss3_y_pos
boss3_attack = False
boss3_attack_time = 0 
boss3_attack_random = random.randrange(60,120) 
boss3_w_speed = -15
b3_hit = 0
boss3_hit.set_alpha(0)
boss3_w_remove = -1
boss3_attack1 = False
boss3_attack2 = False

#캐릭터무기
weapon_size = weapon.get_rect().size #캐릭터무기 이미지 사이즈
weapon_width = weapon_size[0] #캐릭터무기 가로크기
weapon_height = weapon_size[1] #캐릭터무기 세로크기
weapon_speed = 40 #캐릭터무기 속도 20으로 설정
press_time = 0 #스페이스 누른 시간
key_press = False #스페이스를 눌렀나?
power = 0 #캐릭터무기 파워
weapon.set_alpha(0) #캐릭터무기 가리기
weapon_x_pos = character_x_pos #무기 x좌표 설정
weapon_y_pos = character_y_pos + weapon_height #무기 y좌표 설정
weapon_next = False #다음공격 가능
plus_power = 0 #추가 공격력

#캐릭터 hp
plus_hp = 0
character_hp = 4
character_hp4.set_alpha(0)
character_hp3.set_alpha(0)
character_hp2.set_alpha(0)
character_hp1.set_alpha(0)
character_hp0.set_alpha(0)
#캐릭터 맞음
character_hit = 0

#텍스트 표시 시간
clear_text_time = 0

#이동할좌표
to_x = 0
to_y = 0
boss1_to_x = 0
boss1_w_to_y = 0
boss2_to_x = 0
boss2_w_to_y = 0
boss3_to_x = 0
boss3_w_to_y = 0

#던전 활성화/비활성화
Dungeon = False
Dungeon1 = False
Dungeon2 = False
Dungeon3 = False

#던전 클리어 / 던전 끝
Dungeon1_clear = False
Dungeon2_clear = False
Dungeon3_clear = False
Dungeon_End = False
#던전클리어 카운트
Dungeon_clear = 0

#캐릭터, 보스 스피드
plus_speed = 0
character_speed = 0.3
boss1_speed = 0.02
boss2_speed = 0.025
boss3_speed = 0.02

#캐릭터 투명
right.set_alpha(0)
left.set_alpha(0)
down.set_alpha(0)
up.set_alpha(0)
character.set_alpha(0)

#게이지투명
gauge.set_alpha(0)
gauge1.set_alpha(0)
gauge2.set_alpha(0)
gauge3.set_alpha(0)
gauge4.set_alpha(0)
gauge5.set_alpha(0)
gauge6.set_alpha(0)

#걸린시간
time = 0
#점수
score = 0
Dungeon_score = 0
#코인
coin = 0
Dungeon_coin = 0

#상점 세팅
shop_size = shop.get_rect().size
shop_width = shop_size[0]
shop_height = shop_size[1]
shop_ = 0
shop_key = True
shop_rect = shop.get_rect()
shop_rect.left = 10
shop_rect.top = 510
shop1_buy = False
shop2_buy = False
shop3_buy = False
shop4_buy = False
shop5_buy = False
shop6_buy = False
buy_error = 0

#마법진 세팅
magic_circle1 = pygame.image.load(os.path.join(image_path, "magic_circle1.png"))
magic_circle1_f = pygame.image.load(os.path.join(image_path, "magic_circle_f1.png"))
magic_circle1_f.set_alpha(0)
magic_circle1_size = magic_circle1.get_rect().size
magic_circle1_width = magic_circle1_size[0]
magic_circle1_height = magic_circle1_size[1]
magic_circle1_rect = magic_circle1.get_rect()
magic_circle1_rect.left = 73
magic_circle1_rect.top = 213

magic_circle2 = pygame.image.load(os.path.join(image_path, "magic_circle2.png"))
magic_circle2_f = pygame.image.load(os.path.join(image_path, "magic_circle_f2.png")) 
magic_circle2_f.set_alpha(1000)
magic_circle2.set_alpha(0)
magic_circle2_size = magic_circle2.get_rect().size 
magic_circle2_width = magic_circle2_size[0] 
magic_circle2_height = magic_circle2_size[1] 
magic_circle2_rect = magic_circle2.get_rect()
magic_circle2_rect.left = 333
magic_circle2_rect.top = 133

magic_circle3 = pygame.image.load(os.path.join(image_path, "magic_circle3.png"))
magic_circle3_f = pygame.image.load(os.path.join(image_path, "magic_circle_f3.png")) 
magic_circle3_f.set_alpha(1000)
magic_circle3.set_alpha(0)
magic_circle3_size = magic_circle3.get_rect().size
magic_circle3_width = magic_circle3_size[0]
magic_circle3_height = magic_circle3_size[1]
magic_circle3_rect = magic_circle3.get_rect()
magic_circle3_rect.left = 193
magic_circle3_rect.top = 83

#폰트
pygame.init()
game_font = pygame.font.SysFont(None, 25)
game_font2 = pygame.font.SysFont(None, 15, False, True)
game_font3 = pygame.font.SysFont('한국기계연구원light', 12)
score_text_font = pygame.font.SysFont('한국기계연구원bold', 30)
main_font = pygame.font.SysFont('한국기계연구원bold', 20)
#반복문
running = True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        ##던전 밖 움직임##
        if Dungeon == False and win_image_time == 0 and lose_image_time == 0 and shop_ == 0:
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT: #왼쪽방향키 누르면
                    to_x -= character_speed + plus_speed #왼쪽으로 이동
                    character.set_alpha(0) #캐릭터 가리기
                    left.set_alpha(1000) #캐릭터(왼쪽) 보이기
                    down.set_alpha(0) #캐릭터(아래쪽) 가리기
                    up.set_alpha(0) #캐릭터(위쪽) 가리기
                    right.set_alpha(0) #캐릭터(오른쪽) 가리기
                elif event.key == pygame.K_RIGHT: #오른쪽방향키 누르면
                    to_x += character_speed + plus_speed
                    character.set_alpha(0)
                    right.set_alpha(1000)
                    left.set_alpha(0)
                    down.set_alpha(0)
                    up.set_alpha(0)
                elif event.key == pygame.K_UP: #위방향키 누르면
                    to_y -= character_speed + plus_speed
                    character.set_alpha(0)
                    up.set_alpha(1000)
                    left.set_alpha(0)
                    down.set_alpha(0)
                    right.set_alpha(0)
                elif event.key == pygame.K_DOWN: #아래방향키 누르면
                    to_y += character_speed + plus_speed
                    character.set_alpha(0)
                    down.set_alpha(1000)
                    left.set_alpha(0)
                    up.set_alpha(0)
                    right.set_alpha(0)
                elif event.key == pygame.K_b and shop_ == 0:
                    shop_ = 1

        elif Dungeon == False and win_image_time >= 1 or lose_image_time >= 1:
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE: #esc누르면
                            win_image_time = 600 #우승 메뉴 끔
                            lose_image_time = 600 #패배 메뉴 끔

        ##상점##
        elif Dungeon == False and shop_ >= 1:
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_b:
                    shop_ = 0
                    shop_key = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #좌, 우 키 때면
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN: #위, 아래 키 때면
                to_y = 0        

        ##던전 안 조작##
        if Dungeon == True:
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE: #스페이스바 누르면
                    if weapon_next == True:
                        key_press = True #스페이스 눌렀나? true(1)로 설정
                elif event.key == pygame.K_LEFT: #왼쪽방향키 누르면
                    to_x -= character_speed + plus_speed
                    if character_hit == 0: #캐릭터가 맞은 상태가 아니면
                        left.set_alpha(1000)
                    character.set_alpha(0)
                    down.set_alpha(0)
                    up.set_alpha(0)
                    right.set_alpha(0)
                elif event.key == pygame.K_RIGHT: #오른쪽방향키 누르면
                    to_x += character_speed + plus_speed
                    if character_hit == 0:
                        right.set_alpha(1000)
                    left.set_alpha(0)
                    down.set_alpha(0)
                    up.set_alpha(0)  
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #좌, 우 키 때면
                    to_x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN: #위, 아래 키 때면
                    to_y = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE: #스페이스 때면
                    if  power >= 1: #파워가 1보다 크면
                        weapon.set_alpha(1000) #무기 보이기
                        key_press = False #스페이스 눌렀나? 0으로 초기화
                        press_time = 0 #스페이스 누른시간 0으로 초기화
                        weapon_next = False
                    #파워가 0이면 공격X
                    if power < 1:
                        key_press = False #스페이스 눌렀나? 0으로 초기화
                        press_time = 0 #스페이스 누른시간 0으로 초기화
                        weapon_y_pos = -100

    if Dungeon == True:
        ##캐릭터무기 공격력 설정##
        if key_press == True: #스페이스를 눌렀나? true(1)면
            weapon_y_pos = character_y_pos + 40 #무기 y좌표 설정
            weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2) #무기 x좌표 설정
            if power < 25: #파워가 25보다 작나?
                press_time = press_time + 1 #스페이스 누른시간 +1틱
                power = press_time/10 #파워 = 스페이스 누른시간 / 10
            elif power >= 25: #파워가 25이상인가?
                power = 30 #파워를 30으로 설정(30이 MAX)

    if weapon_y_pos <= 0: #캐릭터 무기가 위 경계에 닿으면
        weapon_next = True
        power = 0 #파워 0으로 초기화
    #무기를 위로 움직이게
    weapon_y_pos = weapon_y_pos - weapon_speed

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #캐릭터 화면 밖으로 못나가게
    if character_x_pos < 0: #캐릭터 왼쪽 경계에 닿으면
        character_x_pos = 0 #캐릭터 x좌표를 0으로 설정
    elif character_x_pos > screen_width - character_width: #캐릭터가 오른쪽 경계에 닿으면
        character_x_pos = screen_width - character_width #캐릭터 x좌표를 (스크린 - 캐릭터가로길이) 로 설정
    if character_y_pos > 540: #캐릭터가 아래 경계에 닿으면
        character_y_pos = 540 #캐릭터 y좌표를 540으로 설정
    elif character_y_pos < 70: #캐릭터가 위 경계에 닿으면
        character_y_pos = 70 #캐릭터 y좌표를 70으로 설정

    ##충돌감지위한 rect설정##
    #캐릭터 rect
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    #무기 rect
    weapon_rect = weapon.get_rect()
    weapon_rect.left = weapon_x_pos
    weapon_rect.top = weapon_y_pos

    ##던전에 충돌(닿았을때)##
    if character_rect.colliderect(magic_circle1_rect) and Dungeon == False and Dungeon1_clear == False: #캐릭터가 던전1에 닿았을때 던전안에 있나?Flase 던전1을 클리어하지 않았을때
        if Dungeon1 == False: #던전1에 들어왔나? 가 0이면
            Dungeon1 = True #던전1에 들어왔나? 1로 설정
            Dungeon = True #던전에 들어왔나? 1로 설정
    elif character_rect.colliderect(magic_circle1_rect) and Dungeon == False: #아니고 만약 캐릭터가 던전1에 닿았을때 던전안에 있다 == False 이면? 
        character_x_pos = (screen_width / 2) - (character_width / 2) #캐릭터 x좌표 설정
        character_y_pos = screen_height - character_height #캐릭터 y좌표 설정
        clear_text_time = 1 #비활성화된 던전 텍스트

    elif character_rect.colliderect(magic_circle2_rect) and Dungeon == False and Dungeon2_clear == False and Dungeon1_clear == True:
        if Dungeon2 == False:
            Dungeon2 = True
            Dungeon = True
    elif character_rect.colliderect(magic_circle2_rect) and Dungeon == False:
        character_x_pos = (screen_width / 2) - (character_width / 2) #캐릭터 x좌표 설정
        character_y_pos = screen_height - character_height #캐릭터 y좌표 설정
        clear_text_time = 1

    elif character_rect.colliderect(magic_circle3_rect) and Dungeon == False and Dungeon3_clear == False and Dungeon2_clear == True:
        if Dungeon3 == False:
            Dungeon3 = True
            Dungeon = True
    elif character_rect.colliderect(magic_circle3_rect) and Dungeon == False:
        character_x_pos = (screen_width / 2) - (character_width / 2) #캐릭터 x좌표 설정
        character_y_pos = screen_height - character_height #캐릭터 y좌표 설정
        clear_text_time = 1

    #던전1 우승 했다면
    if win1 == True:
        Dungeon_clear += 1 #던전클리어
        #걸린 시간에 따른 점수
        if time <= 1800: #30초 안에 깨면
            Dungeon_score = Dungeon_score + 50
        elif time <= 2700: #45초 안에 깨면
            Dungeon_score = Dungeon_score + 40
        elif time <= 3600: #60초 안에 깨면
            Dungeon_score = Dungeon_score + 30
        else: #그 밖
            Dungeon_score = Dungeon_score + 20
        #남은 목숨에 따른 점수
        if character_hp == 4:
            Dungeon_score = Dungeon_score  + 50
        elif character_hp == 3:
            Dungeon_score = Dungeon_score + 40
        elif character_hp == 2:
            Dungeon_score = Dungeon_score + 30
        elif character_hp == 1:
            Dungeon_score = Dungeon_score + 20
        #점수에 따른 코인지급
        Dungeon_coin = Dungeon_score / 10

        coin = Dungeon_coin + coin
        score = Dungeon_score + score
        #우승 표시
        win_image_time = 1
        win1 = False
    #던전2 우승 했다면
    if win2 == True:
        Dungeon_score = 0
        Dungeon_coin = 0
        Dungeon_clear += 1 #던전클리어
        #걸린 시간에 따른 점수
        if time <= 3000: #50초
            Dungeon_score = Dungeon_score + 50
        elif time <= 4200: #70초
            Dungeon_score = Dungeon_score + 40
        elif time <= 5400: #90초
            Dungeon_score = Dungeon_score + 30
        else: #그 밖
            Dungeon_score = Dungeon_score + 20
        #남은 목숨에 따른 점수
        if character_hp == 4:
            Dungeon_score = Dungeon_score  + 50
        elif character_hp == 3:
            Dungeon_score = Dungeon_score + 40
        elif character_hp == 2:
            Dungeon_score = Dungeon_score + 30
        elif character_hp == 1:
            Dungeon_score = Dungeon_score + 20
        #점수에 따른 코인지급
        Dungeon_coin = Dungeon_score / 10
        coin = Dungeon_coin + coin
        score = Dungeon_score + score
        #우승 표시
        win_image_time = 1
        win2 = False
    #던전3 우승 했다면
    if win3 == True:
        Dungeon_score = 0
        Dungeon_coin = 0
        Dungeon_clear += 1 #던전클리어
        #걸린 시간에 따른 점수
        if time <= 5400: #90초
            Dungeon_score = Dungeon_score + 50
        elif time <= 6600: #110초
            Dungeon_score = Dungeon_score + 40
        elif time <= 7800: #130초
            Dungeon_score = Dungeon_score + 30
        else: #그 밖
            Dungeon_score = Dungeon_score + 20
        #남은 목숨에 따른 점수
        if character_hp == 4:
            Dungeon_score = Dungeon_score  + 50
        elif character_hp == 3:
            Dungeon_score = Dungeon_score + 40
        elif character_hp == 2:
            Dungeon_score = Dungeon_score + 30
        elif character_hp == 1:
            Dungeon_score = Dungeon_score + 20
        #점수에 따른 코인지급
        Dungeon_coin = Dungeon_score / 10
        coin = Dungeon_coin + coin
        score = Dungeon_score + score
        #우승 표시
        win_image_time = 1
        win3 = False

    if lose == True:
        Dungeon_coin = 0
        Dungeon_score = 0
        lose_image_time = 1
        lose = False


    ##던전1에 들어갔다면##
    if Dungeon1 == True:
        if time == 1:
            character_hp = 4 + plus_hp
            key_press = False #스페이스 눌렀나? 0으로 초기화
            press_time = 0 #스페이스 누른시간 0으로 초기화
            boss1_hp = 100
            boss_hp_bar = pygame.transform.scale(boss_hp_bar, (boss1_hp, 10))
        #보스1 rect
        boss1_rect = boss1.get_rect()
        boss1_rect.left = boss1_x_pos
        boss1_rect.top = boss1_y_pos
        #보스1무기 rect
        boss1_w_rect = boss1_w.get_rect()
        boss1_w_rect.left = boss1_w_x_pos
        boss1_w_rect.top = boss1_w_y_pos
        a = random.randint(0, 1) #a에 0또는 1을 랜덤하게 넣음
        if a == 0: #a가 0이면 보스1 왼쪽으로 이동
            boss1_to_x -= boss1_speed
        else: #아니면 보스1 오른쪽으로 이동
            boss1_to_x += boss1_speed
        ##보스1 벽 닿으면 멈춤##
        boss1_x_pos += boss1_to_x * dt
        if boss1_x_pos < 0: #보스가 왼쪽 벽에 닿았을때
            boss1_x_pos = 0 #보스 x좌표를 0으로 설정
            boss1_to_x = 0
        elif boss1_x_pos > screen_width - boss1_width: #보스가 오른쪽 벽에 닿았을때
            boss1_x_pos = screen_width - boss1_width #보스 x좌표를 (스크린가로 - 보스 가로)로 설정
            boss1_to_x = 0
        ##보스 공격##
        boss1_attack_time = boss1_attack_time + 1 #1초에 60번씩 time에 1씩 +
        if boss1_attack_time >= boss1_attack_random: #time 이 랜덤으로 뽑은 수보다 커지면 (30~180틱)
            boss1_attack_time = 0 #time 0으로 초기화
            boss1_attack_random = random.randrange(120,240) #랜덤수를 또 뽑음
            boss1_attack = True #attack 을 1로 바꿔줌
            if boss1_attack == True: #attack이 1이라면
                boss1_w_x_pos = boss1_x_pos #보스1 무기의 x좌표를 보스 x좌표로 설정
                boss1_w_y_pos = boss1_y_pos #보스1 무기의 y좌표를 보스 y좌표로 설정
                boss1_ws.append([boss1_w_x_pos, boss1_w_y_pos]) #보스1 무기 소환
                boss1_attack = False #attack 초기화
        boss1_ws = [[b1w[0], b1w[1] - boss1_w_speed] for b1w in boss1_ws] #보스1 무기 이동
        boss1_ws = [[b1w[0], b1w[1]] for b1w in boss1_ws if b1w [1] < 490] #바닥에 닿으면 사라짐
        #보스무기-캐릭터 충돌
        for boss1_w_idx, boss1_w_val in enumerate(boss1_ws):
            boss1_w_pos_x = boss1_w_val[0]
            boss1_w_pos_y = boss1_w_val[1]
            #무기 rect정보 업데이트
            boss1_w_rect = boss1_w.get_rect()
            boss1_w_rect.left = boss1_w_pos_x
            boss1_w_rect.top = boss1_w_pos_y
            #보스무기가 캐릭터에 충돌하면
            if boss1_w_rect.colliderect(character_rect):
                boss1_w_remove = boss1_w_idx #무기 없애기 위한 값 설정
                break #for 나가기
        if boss1_w_remove > -1:
            character_hp = character_hp - 1
            del boss1_ws[boss1_w_remove]
            boss1_w_remove = -1
            character_hit = 1
        #보스 hp바 이미지
        screen.blit(boss_hp_bar, (hp_bar_x_pos, hp_bar_y_pos))
        boss_hp_bar.set_alpha(1000)


        #보스-캐릭터무기 충돌
        if weapon_rect.colliderect(boss1_rect): #캐릭터무기를 보스1에 맞추면
            weapon_next = True
            b1_hit = 1 #보스1 맞음 1로 설정
            #hp바 길이
            boss1_hp = boss1_hp - (power + plus_power) #파워만큼 보스 hp감소
            weapon_y_pos = -100 #캐릭터무기 y좌표 설정
            power = 0 #파워 0으로 초기화
            if 0 < boss1_hp - (power + plus_power): #보스1 (hp - 파워)가 0보다 크면(보스hp가 마이너스가 되면 스케일설정 오류남 )
                boss_hp_bar = pygame.transform.scale(boss_hp_bar, (boss1_hp, 10))
            if 0 >= boss1_hp - (power + plus_power): #보스1 (hp - 파워)가 0보다 작으면
                boss_hp_bar.set_alpha(0) #보스1 hp바 숨기기
                Dungeon1_clear = True #보스1스테이지 클리어
                Dungeon_End = True
                boss1_hp = 0 #보스hp = 0
                win1 = True #우승 true
        if b1_hit >= 1: #보스가 맞으면
            b1_hit = b1_hit+1 #맞은시간 +1
            boss1_hit.set_alpha(1000) #보스1 맞은표시 보이기
        if b1_hit == 15: #맞은지 15틱 후에 
            boss1_hit.set_alpha(0) #보스1 맞은표시 숨기기(빨간색)
            b1_hit = 0

        #이미지 보이게(보스, 배경, 파워게이지, hp바)
        screen.blit(boss1_b, (0,0))
        screen.blit(boss1, (boss1_x_pos,boss1_y_pos))
        screen.blit(boss1_hit, (boss1_x_pos, boss1_y_pos))
        gauge.set_alpha(1000)
        background.set_alpha(0)
        boss1_b.set_alpha(1000)
        boss1.set_alpha(1000)
        boss_ui.set_alpha(1000)


        ##던전2에 들어갔다면##
    if Dungeon2 == True:
        boss2_w.set_alpha(1000)
        if time == 1:
            key_press = False
            press_time = 0
            character_hp = 4 + plus_hp
            boss2_hp = 300
            boss_hp_bar = pygame.transform.scale(boss_hp_bar, (boss2_hp/3, 10))
        boss2_rect = boss2.get_rect()
        boss2_rect.left = boss2_x_pos
        boss2_rect.top = boss2_y_pos
        boss2_w_rect = boss2_w.get_rect()
        boss2_w_rect.left = boss2_w_x_pos
        boss2_w_rect.top = boss2_w_y_pos
        a = random.randint(0, 1)
        if a == 0:
            boss2_to_x -= boss2_speed
        else:
            boss2_to_x += boss2_speed
        boss2_x_pos += boss2_to_x * dt
        if boss2_x_pos < 0:
            boss2_x_pos = 0
            boss2_to_x = 0
        elif boss2_x_pos > screen_width - boss2_width:
            boss2_x_pos = screen_width - boss2_width
            boss2_to_x = 0
        ##보스 공격##
        boss2_attack_time = boss2_attack_time + 1
        if boss2_attack_time == boss2_attack_random:
            boss2_attack = True
            boss2_attack_random = random.randrange(60,100) 
            boss2_attack_time = 0 

        if boss2_attack == True: 
            boss2_w_x_pos = boss2_x_pos 
            boss2_w_y_pos = boss2_y_pos 
            boss2_ws.append([boss2_w_x_pos+30, boss2_w_y_pos+60]) 
            boss2_attack = False 
        
        boss2_ws = [[b2w[0], b2w[1] - boss2_w_speed] for b2w in boss2_ws] 
        boss2_ws = [[b2w[0], b2w[1]] for b2w in boss2_ws if b2w [1] < 570]
        for boss2_w_idx, boss2_w_val in enumerate(boss2_ws):
            boss2_w_pos_x = boss2_w_val[0]
            boss2_w_pos_y = boss2_w_val[1]
            boss2_w_rect = boss2_w.get_rect()
            boss2_w_rect.left = boss2_w_pos_x
            boss2_w_rect.top = boss2_w_pos_y

            if boss2_w_rect.colliderect(character_rect):
                boss2_w_remove = boss2_w_idx 
                break
        if boss2_w_remove > -1:
            character_hp -= 1
            del boss2_ws[boss2_w_remove]
            boss2_w_remove = -1
            character_hit = 1

        screen.blit(boss_hp_bar, (hp_bar_x_pos, hp_bar_y_pos))
        boss_hp_bar.set_alpha(1000)


        if weapon_rect.colliderect(boss2_rect):
            weapon_next = True
            b2_hit = 1 

            boss2_hp = boss2_hp - (power + plus_power)
            weapon_y_pos = -100 
            power = 0 
            if 0 < boss2_hp - (power + plus_power): 
                boss_hp_bar = pygame.transform.scale(boss_hp_bar, (boss2_hp/3, 10))
            if 0 >= boss2_hp - (power + plus_power):
                boss_hp_bar.set_alpha(0)
                Dungeon2_clear = 1 
                Dungeon_End = True
                boss2_hp = 0 
                win2 = True 
        if b2_hit >= 1: 
            b2_hit = b2_hit+1 
            boss2_hit.set_alpha(1000) 
            boss2.set_alpha(0)
        if b2_hit == 15: 
            boss2_hit.set_alpha(0)
            boss2.set_alpha(1000)
            b2_hit = 0

        screen.blit(boss2_b, (0,0))
        screen.blit(boss2, (boss2_x_pos,boss2_y_pos))
        screen.blit(boss2_hit, (boss2_x_pos, boss2_y_pos))
        gauge.set_alpha(1000)
        background.set_alpha(0)
        boss2_b.set_alpha(1000)
        boss2.set_alpha(1000)
        boss_ui.set_alpha(1000)


        ##던전3에 들어갔다면##
    if Dungeon3 == True:
        boss3_w.set_alpha(1000)
        if time == 1:
            key_press = False
            press_time = 0
            character_hp = 4 + plus_hp
            boss3_hp = 300
            boss_hp_bar = pygame.transform.scale(boss_hp_bar, (boss3_hp/3, 10))
        boss3_rect = boss3.get_rect()
        boss3_rect.left = boss3_x_pos
        boss3_rect.top = boss3_y_pos
        boss3_w_rect = boss3_w.get_rect()
        boss3_w_rect.left = boss3_w_x_pos
        boss3_w_rect.top = boss3_w_y_pos
        a = random.randint(0, 1)
        if a == 0:
            boss3_to_x -= boss3_speed
        else:
            boss3_to_x += boss3_speed
        boss3_x_pos += boss3_to_x * dt
        if boss3_x_pos < 0:
            boss3_x_pos = 0
            boss3_to_x = 0
        elif boss3_x_pos > screen_width - boss3_width:
            boss3_x_pos = screen_width - boss3_width
            boss3_to_x = 0
        ##보스 공격##
        boss3_attack_time = boss3_attack_time + 1
        if boss3_attack_time == boss3_attack_random:
            boss3_attack1 = True
        if boss3_attack_time == boss3_attack_random + 10:
            boss3_attack2 = True
            boss3_attack_random = random.randrange(60,120) 
            boss3_attack_time = 0 

        if boss3_attack1 == True: 
            boss3_w_x_pos = boss3_x_pos 
            boss3_w_y_pos = boss3_y_pos 
            boss3_ws.append([boss3_w_x_pos+3, boss3_w_y_pos+50]) 
            boss3_attack1 = False 
        if boss3_attack2 == True: 
            boss3_w_x_pos = boss3_x_pos 
            boss3_w_y_pos = boss3_y_pos 
            boss3_ws.append([boss3_w_x_pos+56, boss3_w_y_pos+66])
            boss3_attack2 = False 
        
        boss3_ws = [[b3w[0], b3w[1] - boss3_w_speed] for b3w in boss3_ws] 
        boss3_ws = [[b3w[0], b3w[1]] for b3w in boss3_ws if b3w [1] < 570]
        for boss3_w_idx, boss3_w_val in enumerate(boss3_ws):
            boss3_w_pos_x = boss3_w_val[0]
            boss3_w_pos_y = boss3_w_val[1]
            boss3_w_rect = boss3_w.get_rect()
            boss3_w_rect.left = boss3_w_pos_x
            boss3_w_rect.top = boss3_w_pos_y

            if boss3_w_rect.colliderect(character_rect):
                boss3_w_remove = boss3_w_idx 
                break
        if boss3_w_remove > -1:
            character_hp -= 1
            del boss3_ws[boss3_w_remove]
            boss3_w_remove = -1
            character_hit = 1

        screen.blit(boss_hp_bar, (hp_bar_x_pos, hp_bar_y_pos))
        boss_hp_bar.set_alpha(1000)

        if weapon_rect.colliderect(boss3_rect):
            weapon_next = True
            b3_hit = 1 

            boss3_hp = boss3_hp - (power + plus_power)
            weapon_y_pos = -100 
            power = 0 
            if 0 < boss3_hp - (power + plus_power): 
                boss_hp_bar = pygame.transform.scale(boss_hp_bar, (boss3_hp/3, 10))
            if 0 >= boss3_hp - (power + plus_power):
                boss_hp_bar.set_alpha(0)
                Dungeon3_clear = 1 
                Dungeon_End = True
                boss3_hp = 0 
                win3 = True 
        if b3_hit >= 1: 
            b3_hit = b3_hit+1 
            boss3_hit.set_alpha(1000) 
            boss3.set_alpha(0)
        if b3_hit == 15: 
            boss3_hit.set_alpha(0)
            boss3.set_alpha(1000)
            b3_hit = 0

        screen.blit(boss3_b, (0,0))
        screen.blit(boss3, (boss3_x_pos,boss3_y_pos))
        screen.blit(boss3_hit, (boss3_x_pos, boss3_y_pos))
        gauge.set_alpha(1000)
        background.set_alpha(0)
        boss3_b.set_alpha(1000)
        boss3.set_alpha(1000)
        boss_ui.set_alpha(1000)


    #던전 끝나면
    if Dungeon_End == True:
        Dungeon1 = False
        Dungeon2 = False
        Dungeon3 = False
        Dungeon = False
        Dungeon_End = False
        boss1_w.set_alpha(0)
        boss2_w.set_alpha(0)
        boss3_w.set_alpha(0)
        character_hp1.set_alpha(0)
        character_hp2.set_alpha(0)
        character_hp3.set_alpha(0)
        character_hp4.set_alpha(0)
        hp_bar_b.set_alpha(0)
        gauge.set_alpha(0)
        gauge1.set_alpha(0)
        gauge2.set_alpha(0)
        gauge3.set_alpha(0)
        gauge4.set_alpha(0)
        gauge5.set_alpha(0)
        gauge6.set_alpha(0)
        gaugemax.set_alpha(0)
        if Dungeon1_clear == False:
            magic_circle1.set_alpha(1000)
        elif Dungeon1_clear == True:
            magic_circle1_f.set_alpha(1000)
            magic_circle1.set_alpha(0)
        if Dungeon1_clear == True and Dungeon2_clear == False:
            magic_circle2.set_alpha(1000)
        elif Dungeon1_clear == False or Dungeon2_clear == True:
            magic_circle2_f.set_alpha(1000)
            magic_circle2.set_alpha(0)
        if Dungeon2_clear == True and Dungeon3_clear == False :
            magic_circle3.set_alpha(1000)
        elif Dungeon2_clear == False or Dungeon3_clear == True:
            magic_circle3_f.set_alpha(1000)
            magic_circle3.set_alpha(0) 
        background.set_alpha(1000)
        background_text.set_alpha(1000)
        boss_ui.set_alpha(1000)
        character_x_pos = (screen_width / 2) - (character_width / 2) #캐릭터 x좌표 설정 (화면 가운데)
        character_y_pos = screen_height - character_height #캐릭터 y좌표 설정

    #(배경, 배경텍스트, 캐릭터, 던전입구, 보스무기) 그리기
    for boss1_w_x_pos, boss1_w_y_pos in boss1_ws:
        screen.blit(boss1_w, (boss1_w_x_pos, boss1_w_y_pos))
    for boss2_w_x_pos, boss2_w_y_pos in boss2_ws:
        screen.blit(boss2_w, (boss2_w_x_pos, boss2_w_y_pos))
    for boss3_w_x_pos, boss3_w_y_pos in boss3_ws:
        screen.blit(boss3_w, (boss3_w_x_pos, boss3_w_y_pos))
    if 0 < boss1_hp - power and Dungeon == True:
        boss_hp_bar.set_alpha(1000)
    screen.blit(background, (0,0))
    screen.blit(background_text, (0,0))
    screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(stop, (character_x_pos, character_y_pos))
    screen.blit(up, (character_x_pos, character_y_pos))
    screen.blit(down, (character_x_pos, character_y_pos))
    screen.blit(left, (character_x_pos, character_y_pos))
    screen.blit(right, (character_x_pos, character_y_pos))
    screen.blit(magic_circle1, (73,213))
    screen.blit(magic_circle2, (333,133))
    screen.blit(magic_circle3, (193,83))
    screen.blit(magic_circle1_f, (73,213))
    screen.blit(magic_circle2_f, (333,133))
    screen.blit(magic_circle3_f, (193,83))

    clear_text = game_font3.render('T i p .  비활성화됨.',True,(100,0,0))

    if clear_text_time >= 1:
        clear_text_time += 1
        screen.blit(clear_text, (13, 43))
        if clear_text_time ==150:
            clear_text_time = 0

    #던전 안이면
    if Dungeon == True:
        if time %1800  == 0:
            character_hp += 1
        #비활성화 텍스트 숨기기
        clear_text_time = 0
        #걸린시간 +
        time += 1
        #던전입구, 배경택스트 숨기기
        magic_circle1.set_alpha(0)
        magic_circle2.set_alpha(0)
        magic_circle3.set_alpha(0)
        magic_circle1_f.set_alpha(0)
        magic_circle2_f.set_alpha(0)
        magic_circle3_f.set_alpha(0)
        background_text.set_alpha(0)
        #보이기
        hp_bar_b.set_alpha(1000)
        boss_hp_bar.set_alpha(1000)
        screen.blit(boss_ui, (0,570))
        screen.blit(gauge, (390,220))
        screen.blit(gauge1, (390,220))
        screen.blit(gauge2, (390,220))
        screen.blit(gauge3, (390,220))
        screen.blit(gauge4, (390,220))
        screen.blit(gauge5, (390,220))
        screen.blit(gauge6, (390,220))
        screen.blit(gaugemax, (390, 220))
        screen.blit(hp_bar_b, (hp_bar_x_pos-1, hp_bar_y_pos -1))
        screen.blit(boss_hp_bar, (hp_bar_x_pos, hp_bar_y_pos))
        #캐릭터 y좌표 바닥으로 고정
        character_y_pos = screen_height - character_height - 70
    
        #캐릭터 hp표시
        if character_hp == 6:
            screen.blit(plus_hp2, (hp_bar_x_pos + 80, hp_bar_y_pos - 20))
            screen.blit(character_hp4, (hp_bar_x_pos + 30, hp_bar_y_pos - 20))
            character_hp4.set_alpha(1000)
        elif character_hp == 5:
            screen.blit(plus_hp1, (hp_bar_x_pos + 80, hp_bar_y_pos - 20))
            screen.blit(character_hp4, (hp_bar_x_pos + 30, hp_bar_y_pos - 20))
            character_hp4.set_alpha(1000)
        elif character_hp == 4:
            screen.blit(character_hp4, (hp_bar_x_pos + 30, hp_bar_y_pos - 20))
            character_hp4.set_alpha(1000)
        elif character_hp == 3:
            screen.blit(character_hp3, (hp_bar_x_pos + 30, hp_bar_y_pos - 20))
            character_hp3.set_alpha(1000)
        elif character_hp == 2:
            screen.blit(character_hp2, (hp_bar_x_pos + 30, hp_bar_y_pos - 20))
            character_hp2.set_alpha(1000)
        elif character_hp == 1:
            screen.blit(character_hp1, (hp_bar_x_pos + 30, hp_bar_y_pos - 20)) 
            character_hp1.set_alpha(1000)     
        elif character_hp == 0:
            screen.blit(character_hp0, (hp_bar_x_pos + 30, hp_bar_y_pos - 20))  
            character_hp0.set_alpha(1000)    

        #캐릭터 맞으면
        if character_hit >= 1:
            screen.blit(character_stop_hit, (character_x_pos, character_y_pos))
            character_stop_hit.set_alpha(1000)
            left.set_alpha(0)
            right.set_alpha(0)
            character_hit += 1
            if character_hit == 15:
                character_stop_hit.set_alpha(0)
                character_hit = 0
        #패배
        if character_hp == 0:
            lose = True
            Dungeon_End = True
            character_hp = 4

        #텍스트
        if Dungeon1 == True:
            boss1_hp_text = game_font2.render("BOSS | " + (str(int(boss1_hp))) + " / 100", True, (255, 255, 255)) #hp
            screen.blit(boss1_hp_text, (hp_bar_x_pos, hp_bar_y_pos))
        if Dungeon2 == True:
            boss2_hp_text = game_font2.render("BOSS | " + (str(int(boss2_hp))) + " / 300", True, (255, 255, 255)) #hp
            screen.blit(boss2_hp_text, (hp_bar_x_pos, hp_bar_y_pos))
        if Dungeon3 == True:
            boss3_hp_text = game_font2.render("BOSS | " + (str(int(boss3_hp))) + " / 300", True, (255, 255, 255)) #hp
            screen.blit(boss3_hp_text, (hp_bar_x_pos, hp_bar_y_pos))

        

        Power_red_text = game_font.render(str(int(power)), True, (255,0,0)) #파워 (빨강)출력
        Power_gray_text = game_font.render(str(int(power)), True, (127,127,127)) #파워 (회색)출력
        Power_text = game_font.render('Power ',True,(0,29,132)) #"Power" 출력
        #Power출력
        screen.blit(Power_text, (390,340)) 
        #파워가 30이면 빨간색으로 출력
        if power == 30:
            screen.blit(Power_red_text,(444, 341))
            Power_gray_text.set_alpha(0)
        #아니면 회색
        else:
            Power_gray_text.set_alpha(1000)
            screen.blit(Power_gray_text, (444,341))
        ##게이지 조절##
        if power == 0: 
            gauge.set_alpha(1000)
            gauge1.set_alpha(0)
            gauge2.set_alpha(0)
            gauge3.set_alpha(0)
            gauge4.set_alpha(0)
            gauge5.set_alpha(0)
            gauge6.set_alpha(0)
            gaugemax.set_alpha(0)
        elif power >= 1 and power <= 3:
            gauge1.set_alpha(1000)
            gauge.set_alpha(0)
            gauge2.set_alpha(0)
            gauge3.set_alpha(0)
            gauge4.set_alpha(0)
            gauge5.set_alpha(0)
            gauge6.set_alpha(0)
            gaugemax.set_alpha(0)
        elif power >= 4 and power <= 7:
            gauge2.set_alpha(1000)
            gauge.set_alpha(0)
            gauge1.set_alpha(0)
            gauge3.set_alpha(0)
            gauge4.set_alpha(0)
            gauge5.set_alpha(0)
            gauge6.set_alpha(0)
            gaugemax.set_alpha(0)
        elif power >= 8 and power <= 11:
            gauge3.set_alpha(1000)
            gauge.set_alpha(0)
            gauge1.set_alpha(0)
            gauge2.set_alpha(0)
            gauge4.set_alpha(0)
            gauge5.set_alpha(0)
            gauge6.set_alpha(0)
            gaugemax.set_alpha(0)
        elif power >= 12 and power <= 15:
            gauge4.set_alpha(1000)
            gauge.set_alpha(0)
            gauge1.set_alpha(0)
            gauge2.set_alpha(0)
            gauge3.set_alpha(0)
            gauge5.set_alpha(0)
            gauge6.set_alpha(0)
            gaugemax.set_alpha(0)
        elif power >= 16 and power <= 19:
            gauge5.set_alpha(1000)
            gauge.set_alpha(0)
            gauge1.set_alpha(0)
            gauge2.set_alpha(0)
            gauge3.set_alpha(0)
            gauge4.set_alpha(0)
            gauge6.set_alpha(0)
            gaugemax.set_alpha(0)
        elif power >= 20 and power <= 24:
            gauge6.set_alpha(1000)
            gauge.set_alpha(0)
            gauge1.set_alpha(0)
            gauge2.set_alpha(0)
            gauge3.set_alpha(0)
            gauge4.set_alpha(0)
            gauge5.set_alpha(0)
            gaugemax.set_alpha(0)
        elif power >= 25:
            gaugemax.set_alpha(1000)
            gauge.set_alpha(0)
            gauge1.set_alpha(0)
            gauge2.set_alpha(0)
            gauge3.set_alpha(0)
            gauge4.set_alpha(0)
            gauge5.set_alpha(0)
            gauge6.set_alpha(0)
    #Win, lose띄우기
    if win_image_time >= 1 or lose_image_time >=1:
        if win_image_time >= 1:
            win_image_time += 1
            win_image.set_alpha(1000)
        elif lose_image_time >= 1:
            lose_image_time += 1
            lose_image.set_alpha(1000)
        time_text = score_text_font.render(str(int(time / 60)) , True, (0,0,0))#던전 걸린 시간
        Dungeon_coin_text = score_text_font.render("+" + (str(int(Dungeon_coin))), True, (0,0,0))#던전 코인
        Dungeon_score_text = score_text_font.render("+" + (str(int(Dungeon_score))), True, (0,0,0))#던전 점수
        screen.blit(win_image, (screen_width / 2 - 150, screen_height / 2 - 150))
        screen.blit(lose_image, (screen_width / 2 - 150, screen_height / 2 - 150))
        screen.blit(time_text, (screen_width / 2 - 150 + 179, screen_height / 2 - 150 + 80))
        screen.blit(Dungeon_coin_text, (screen_width / 2 - 150 + 179, screen_height / 2 - 150 + 145))
        screen.blit(Dungeon_score_text, (screen_width / 2 - 150 + 179, screen_height / 2 - 150 + 211))
        #우승패배 이미지 뜰때 shop 끄기
        shop_ = 0
        character_x_pos = (screen_width / 2) - (character_width / 2) #캐릭터 x좌표 설정
        character_y_pos = screen_height - character_height #캐릭터 y좌표 설정 

    #win, lose 지우기
    if win_image_time >= 600 or lose_image_time >= 600:
        win_image_time = 0
        lose_image_time = 0
        win_image.set_alpha(0)
        lose_image.set_alpha(0)
        time = 0
    #던전 밖이면 점수,코인,상점 표시
    if Dungeon == False:
        coin_text = main_font.render(("COIN / ") + (str(int(coin))), True, (255,255,0))#총코인
        score_text = main_font.render(("SCORE / ") + (str(int(score))), True, (255,255,0))#총점수
        screen.blit(coin_text, (11, 9))
        screen.blit(score_text, (240, 9))
        screen.blit(shop, (10, 510))
        shop_text1 = game_font3.render("Press B to open", True, (255,255,255))
        screen.blit(shop_text1,(1, 580))
        if character_rect.colliderect(shop_rect):
            shop_ = 1
    
    if shop_ >= 1:
        screen.blit(shop_b, (0,0))
        character_x_pos = (screen_width / 2) - (character_width / 2) #캐릭터 x좌표 설정
        character_y_pos = screen_height - character_height #캐릭터 y좌표 설정 
        if event.type == pygame.KEYDOWN and shop_key == True: 
            if event.key == pygame.K_RIGHT:
                if shop_ < 5:
                    shop_ += 1
                    shop_key = False
                elif shop_ == 5:
                    shop_ = 1
                    shop_key = False
            if event.key == pygame.K_LEFT:
                if shop_ > 1:
                    shop_ -= 1
                    shop_key = False
                elif shop_ == 1:
                    shop_ = 5
                    shop_key = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                shop_key = True
            if shop_ == 1 and event.key == pygame.K_SPACE:
                if shop1_buy == False and coin >= 8:
                    shop1_buy = True
                    coin -= 8
            if shop_ == 2 and event.key == pygame.K_SPACE:
                if shop2_buy == False and coin >= 8:
                    shop2_buy = True
                    coin -= 8
            if shop_ == 3 and event.key == pygame.K_SPACE:
                if shop3_buy == False and coin >= 8:
                    shop3_buy = True
                    coin -= 8
            if shop_ == 4 and event.key == pygame.K_SPACE:
                if shop4_buy == False and coin >= 9:
                    shop4_buy = True
                    coin -= 9
            if shop_ == 5 and event.key == pygame.K_SPACE:
                if shop5_buy == False and coin >= 9:
                    shop5_buy = True
                    coin -= 9

    if shop_ == 1:
        screen.blit(shop1, (0, 265))
        screen.blit(shop_speed, (20, 265+20))
        screen.blit(shop_heart_f, (115, 265+25))
        screen.blit(shop_power_f, (210, 265+18))
        screen.blit(shop_heal_f, (298, 265+20))
        screen.blit(shop_weapon_f,(388, 256+30))
    if shop_ == 2:
        screen.blit(shop2, (0, 265))
        screen.blit(shop_speed_f, (20, 265+20))
        screen.blit(shop_heart, (115, 265+25))
        screen.blit(shop_power_f, (210, 265+18))
        screen.blit(shop_heal_f, (298, 265+20))
        screen.blit(shop_weapon_f,(388, 256+30))
    if shop_ == 3:
        screen.blit(shop3, (0, 265))
        screen.blit(shop_speed_f, (20, 265+20))
        screen.blit(shop_heart_f, (115, 265+25))
        screen.blit(shop_power, (210, 265+18))
        screen.blit(shop_heal_f, (298, 265+20))
        screen.blit(shop_weapon_f,(388, 256+30))
    if shop_ == 4:
        screen.blit(shop4, (0, 265))
        screen.blit(shop_speed_f, (20, 265+20))
        screen.blit(shop_heart_f, (115, 265+25))
        screen.blit(shop_power_f, (210, 265+18))
        screen.blit(shop_heal, (298, 265+20))
        screen.blit(shop_weapon_f,(388, 256+30))
    if shop_ == 5:
        screen.blit(shop5, (0, 265))
        screen.blit(shop_speed_f, (20, 265+20))
        screen.blit(shop_heart_f, (115, 265+25))
        screen.blit(shop_power_f, (210, 265+18))
        screen.blit(shop_heal_f, (298, 265+20))
        screen.blit(shop_weapon,(388, 256+30))
    if shop_ >= 1:
        if shop1_buy == True:
            screen.blit(shop_buy1_img, (20, 285))
            plus_speed = 0.15
        if shop2_buy == True:
            screen.blit(shop_buy2_img, (112, 285))
            plus_hp = 2
        if shop3_buy == True:
            screen.blit(shop_buy3_img, (204, 285))
            plus_power = 10
        if shop4_buy == True:
            screen.blit(shop_buy4_img, (296, 285))
            hp_heal = 1
        if shop5_buy == True:
            screen.blit(shop_buy5_img, (388, 285))
    #다시 그리기
    pygame.display.update()
#끝내기
pygame.quit()

#폰트출처 – 한국기계연구원, kimm.re.kr