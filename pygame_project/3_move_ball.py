# Project) 오락실 팡팡 게임 만들기
#
# [게임 조건]
# 1. 캐릭터는 화면 아래에 위치, 좌우로만 이동 가능
# 2. 스페이스를 누르면 총알이 나감
# 3. 큰 공 1개가 나타나서 바운스
# 4. 무기에 닿으면 공은 작은 크기 2개로 분할, 가장 작은 크기의 공은 사라지면서 코인을 떨굼
# 5. 모든 공을 없애면 게임 종료 (성공)
# 6. 캐릭터는 공에 닿으면 사망 (실패)
# 7. 시간 제한 99초 초과 시 게임 종료
# 8. FPS 는 30 으로 고정 (필요시 speed 값을 조정)
#
# [게임 이미지]
# 1. 배경 : 640 * 480 가로 세로 - background.png
# 2. 무대 : 640 * 50 - stage.png
# 3. 캐릭터 : 33 * 60 - character.png
# 4. 무기 : 20 * 430 - weapon.png
# 5. 공 : 160 * 160, 80 * 80, 40 * 40, 20 * 20 - balloon1.png ~ balloon4.png

import pygame
import os

################################################
# 기본 초기화 (반드시 해야 함)

pygame.init()  # init 으로 초기화 하기

# 화면 크기 설정
screen_width = 480  # 가로
screen_height = 640  # 세로
screen = pygame.display.set_mode((screen_width, screen_height))  # 화면 크기 설정

# 화면 타이틀 설정
pygame.display.set_caption("고전 게임")

# fps
clock = pygame.time.Clock()
#################################################

# 1. 사용자 게임 초기화(배경,이미지,좌표,폰트,속도 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "image") # image 폴더 위치 반환

# background make
background = pygame.image.load(os.path.join(image_path, "background.png"))
# stage make
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # stage 의 높이 위에 캐릭터를 두기 위해 사용
# character make
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = (screen_height - character_height)

# character
character_to_x = 0

# character speed
character_speed = 5

# weapon make
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# weapon is one time many attack
weapons = []

# weapon speed
weapon_speed = 10

# make move_ball
ball_img = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))
]

# ball_size_init_speed
ball_speed_y = [-18, -15, -12, -9]

# ball_info
balls = []

balls.append({
    "pos_x" : 50, # ball x_pos
    "pos_y" : 50, # ball y_pos
    "img_index" : 0, # ball image index
    "ball_x" : 3, # x축 이동방향, -3 이면 왼쪽, 3 이면 오른쪽
    "ball_y" : -6, # y 축 이동방향
    "init_speed_y" : ball_speed_y[0] # y 최초 속도
})

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    datetime = clock.tick(30)  # 30
    # print("fps: " + str(clock.get_fps()))

    # 2. 이벤트 처리
    for event in pygame.event.get():  # event가 발생하였는가?
        if event.type == pygame.QUIT:  # 창을 닫는 버튼을 눌렀는가?
            running = False  # 나가기 이벤트가 발생되면 QUIT 이벤트 발생

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # weapon location
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]

    # weapon destruction
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    # ball location
    for ball_index, ball_value in enumerate(balls):
        ball_pos_x = ball_value["pos_x"]
        ball_pos_y = ball_value["pos_y"]
        ball_img_index = ball_value["img_index"]

        ball_size = ball_img[ball_img_index].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 가로벽에 닿았을 때 공 이동 위치 변경(튕겨 나오는 효과)
        if ball_pos_x <= 0 or ball_pos_x > screen_width - ball_width:
            ball_value["ball_x"] = ball_value["ball_x"] * -1

        # 세로 위치, 스테이지에 튕겨서 올라가는 처리
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_value["ball_y"] = ball_value["init_speed_y"]
        else: # 그 외의 모든 경우에는 속도를 증가
            ball_value["ball_y"] += 0.5

        ball_value["pos_x"] += ball_value["ball_x"]
        ball_value["pos_y"] += ball_value["ball_y"]

    # 4. 충돌 처리


    # 5. 화면에 그리기
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for index, value in enumerate(balls):
        ball_pos_x = value["pos_x"]
        ball_pos_y = value["pos_y"]
        ball_img_index = value["img_index"]
        screen.blit(ball_img[ball_img_index], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos - stage_height))

    pygame.display.update()  # 매번 게임화면을 새로 그려야 함
# 종료 후 대기
pygame.time.delay(2000)
# False 가 되면 pygame 종료 시키기
pygame.quit()



