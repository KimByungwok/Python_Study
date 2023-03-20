import pygame
################################################
# 기본 초기화 (반드시 해야 함)

pygame.init() # init 으로 초기화 하기

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 크기 설정

# 화면 타이틀 설정
pygame.display.set_caption("파이썬 게임")

# fps
clock = pygame.time.Clock()
#################################################

# 1. 사용자 게임 초기화(배경,이미지,좌표,폰트,속도 등)

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    datetime = clock.tick(30) # 30
    #print("fps: " + str(clock.get_fps()))
    
    # 2. 이벤트 처리    
    for event in pygame.event.get(): # event가 발생하였는가?
        if event.type == pygame.QUIT: # 창을 닫는 버튼을 눌렀는가?
            running = False # 나가기 이벤트가 발생되면 QUIT 이벤트 발생
    
    # 3. 게임 캐릭터 위치 정의
    
    # 4. 충돌 처리
    
    # 5. 화면에 그리기
    
    pygame.display.update() # 매번 게임화면을 새로 그려야 함
# 종료 후 대기
pygame.time.delay(2000)
# False 가 되면 pygame 종료 시키기
pygame.quit()

