import pygame

pygame.init() # init 으로 초기화 하기

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 #세로

screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 크기 설정

# 화면 타이틀 설정
pygame.display.set_caption("파이썬 게임")

# 배경 이미지 불러오기
background_image = pygame.image.load("/Users/byungwook/Python/pygame_basic/backgroud.png")

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # event가 발생하였는가?
        if event.type == pygame.QUIT: # 창을 닫는 버튼을 눌렀는가?
            running = False # 나가기 이벤트가 발생되면 QUIT 이벤트 발생

    #screen.fill((0, 0, 100)) # rgb를 줘서 배경 색을 정할 수도 있음
    screen.blit(background_image, (0, 0)) # 배경 그리기 좌표
    pygame.display.update() # 매번 게임화면을 새로 그려야 함
# False 가 되면 pygame 종료 시키기
pygame.quit()

