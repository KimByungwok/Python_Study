import pygame

pygame.init() # init 으로 초기화 하기

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 #세로

screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 크기 설정

# 화면 타이틀 설정
pygame.display.set_caption("파이썬 게임")

# fps
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background_image = pygame.image.load("/pygame_project/image/background.png")

# 캐릭터 (스프라이트) 생성
character_image = pygame.image.load("/Users/byungwook/PycharmProjects/python_game/pygame_basic/character.png")
character_size = character_image.get_size() # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 새로 크기
character_x_position = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 위치하도록 설정
character_y_position = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이속
speed = 0.5

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    datetime = clock.tick(60) # 30
    #print("fps: " + str(clock.get_fps()))
    
    for event in pygame.event.get(): # event가 발생하였는가?
        if event.type == pygame.QUIT: # 창을 닫는 버튼을 눌렀는가?
            running = False # 나가기 이벤트가 발생되면 QUIT 이벤트 발생
            
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는가?
            if event.key == pygame.K_LEFT: # 왼쪽으로
                to_x -= speed 
            elif event.key == pygame.K_RIGHT: # 오른쪽
                to_x += speed
            elif event.key == pygame.K_UP:  # 위로
                to_y -= speed
            elif event.key == pygame.K_DOWN: # 아래로
                to_y += speed
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    # 프레임별 이속 유지
    character_x_position += to_x * datetime
    character_y_position += to_y * datetime
    
    # 가로 경계값 처리
    if character_x_position < 0:
        character_x_position = 0
    elif character_x_position > screen_width - character_width:
        character_x_position = screen_width - character_width
    
    # 세로 경계값 처리
    if character_y_position < 0:
        character_y_position = 0
    elif character_y_position > screen_height - character_height:
        character_y_position = screen_height - character_height
    
    #screen.fill((0, 0, 100)) # rgb를 줘서 배경 색을 정할 수도 있음
    screen.blit(background_image, (0, 0)) # 배경 그리기 좌표
    screen.blit(character_image, (character_x_position, character_y_position)) # 캐릭터 그리기 좌표
    
    pygame.display.update() # 매번 게임화면을 새로 그려야 함
# False 가 되면 pygame 종료 시키기
pygame.quit()

