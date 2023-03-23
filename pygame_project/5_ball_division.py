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


# fps
clock = pygame.time.Clock()
#################################################

# 1. 사용자 게임 초기화(배경,이미지,좌표,폰트,속도 등)
current_path = os.path.dirname(__file__)  # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "image")  # image 폴더 위치 반환

# background make
background = pygame.image.load(os.path.join(image_path, "background.png"))
# stage make
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]  # stage 의 높이 위에 캐릭터를 두기 위해 사용
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
	"pos_x": 50,  # ball x_pos
	"pos_y": 50,  # ball y_pos
	"img_index": 0,  # ball image index
	"ball_x": 3,  # x축 이동방향, -3 이면 왼쪽, 3 이면 오른쪽
	"ball_y": -6,  # y 축 이동방향
	"init_speed_y": ball_speed_y[0]  # y 최초 속도
})

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
	datetime = clock.tick(30)  # 30
	# print("fps: " + str(clock.get_fps()))

	# 2. 이벤트 처리(키보드, 마우스 등)
	for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
		if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
			running = False  # 게임이 진행중이 아님

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
	weapons = [[w[0], w[1] - weapon_speed] for w in weapons]

	# weapon destruction
	weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

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

		# 세로 위치
		if ball_pos_y >= screen_height - stage_height - ball_height:
			ball_value["ball_y"] = ball_value["init_speed_y"]
		else:  # 그 외의 모든 경우에는 속도를 증가
			ball_value["ball_y"] += 0.5

		ball_value["pos_x"] += ball_value["ball_x"]
		ball_value["pos_y"] += ball_value["ball_y"]

	# 4. 충돌 처리

	# character rect info update
	character_rect = character.get_rect()
	character_rect.left = character_x_pos
	character_rect.top = character_y_pos

	for ball_index, ball_value in enumerate(balls):
		ball_pos_x = ball_value["pos_x"]
		ball_pos_y = ball_value["pos_y"]
		ball_img_index = ball_value["img_index"]

		# ball rect info update
		ball_rect = ball_img[ball_img_index].get_rect()
		ball_rect.left = ball_pos_x
		ball_rect.top = ball_pos_y

		# character & ball collision
		# if character_rect.colliderect(ball_rect):
		# 	print("응 ㅅㄱ 부딪힘")
		# 	running = False
		# 	break
		# ball & weapon collision
		for weapon_index, weapon_value in enumerate(weapons):
			weapon_pos_x = weapon_value[0]
			weapon_pos_y = weapon_value[1]

			# weapon rect info update
			weapon_rect = weapon.get_rect()
			weapon_rect.left = weapon_pos_x
			weapon_rect.top = weapon_pos_y

			# collision check
			if weapon_rect.colliderect(ball_rect):
				weapon_to_remove = weapon_index # 해당 무기 없애기 위한 값 설정
				ball_to_remove = ball_index # 해당 공 없애기 위한 값 설정

			# 가장 작은 공이 아니라면 다음 단계의 공으로 나눠주기
			if ball_img_index < 3:
				# 현재 공 크기 정보를 가지고 옴
				ball_width = ball_rect.size[0]
				ball_height = ball_rect.size[1]

				# 나눠진 공 정보
				small_ball_rect = ball_img[ball_img_index + 1].get_rect()
				small_ball_width = small_ball_rect.size[0]
				small_ball_height = small_ball_rect.size[1]

				# 왼쪽으로 튕겨나가는 작은 공
				balls.append({
					"pos_x": ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 공의 x 좌표
					"pos_y": ball_pos_y + (ball_height / 2) - (small_ball_height / 2), # 공의 y 좌표
					"to_x": -3, # x축 이동 방향, -3이면 왼쪽으로, 3이면 오른쪽으로
					"to_y": -6, # y축 이동 방향
					"init_speed_y": ball_speed_y[ball_img_index + 1]})
				# 오른쪽으로 튕겨나가는 작은 공
				balls.append({
					"pos_x": ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 공의 x 좌표
					"pos_y": ball_pos_y + (ball_height / 2) - (small_ball_height / 2), # 공의 y 좌표
					"img_index": ball_img_index + 1, # 공의 이미지 인덱스
					"to_x": 3, # x축 이동 방향, -3이면 왼쪽으로, 3이면 오른쪽으로
					"to_y": -6, # y축 이동 방향
					"init_speed_y": ball_speed_y[ball_img_index + 1]})
			break



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

pygame.display.update()  # 게임화면을 다시 그리기!
# 딜레이 2초
pygame.time.delay(2000)
# False = 게임이 진행중이 아님
pygame.quit()
