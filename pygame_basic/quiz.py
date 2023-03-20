# Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오

# [게임 조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
# 2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. FPS 는 30 으로 고정

# [게임 이미지]
# 1. 배경 : 640 * 480 (세로 가로) - background.png
# 2. 캐릭터 : 70 * 70 - character.png
# 3. 똥 : 70 * 70 - enemy.png

import pygame
################################################
# 기본 초기화 (반드시 해야 함)

pygame.init() # init 으로 초기화 하기

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 크기 설정

# 화면 타이틀 설정
pygame.display.set_caption("Quiz")

# fps
clock = pygame.time.Clock()
#################################################

# 1. 사용자 게임 초기화(배경,이미지,좌표,폰트,속도 등)
# 배경 만들기
background = pygame.image.load("/Users/byungwook/python_game/pygame_basic/backgroud.png")

# 캐릭터 만들기
character = pygame.image.load("/Users/byungwook/python_game/pygame_basic/character.png")
character_size = character.get_size()
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = (screen_height) - (character_height)


# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    datetime = clock.tick(30) # 30
    #print("fps: " + str(clock.get_fps()))
    
    # 2. 이벤트 처리    
    for event in pygame.event.get(): # event가 발생하였는가?
        if event.type == pygame.QUIT: # 창을 닫는 버튼을 눌렀는가?
            running = False # 나가기 이벤트가 발생되면 QUIT 이벤트 발생
            
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         to_x -= character_speed
        #     elif event.key == pygame.K_RIGHT:
        #         to_y += character_speed
        # if event.type == pygame.KEYUP:
        #     to_x
    
    # 3. 게임 캐릭터 위치 정의
    
    # 4. 충돌 처리
    
    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    
    pygame.display.update() # 매번 게임화면을 새로 그려야 함
# False 가 되면 pygame 종료 시키기
pygame.quit()

