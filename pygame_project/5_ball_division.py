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

import os
import pygame

##############################################################
# normal init (must do)
pygame.init()

# display size set
screen_width = 480  # width size
screen_height = 640  # height size
screen = pygame.display.set_mode((screen_width, screen_height))

# display title set
pygame.display.set_caption("고전 게임")

# FPS
clock = pygame.time.Clock()
##############################################################

# 1. user game init (background, game image, location, speed, font '''others''')
current_path = os.path.dirname(__file__)  # return current file path
image_path = os.path.join(current_path, "image")  # return image folder path

# make background
background = pygame.image.load(os.path.join(image_path, "background.png"))

# make stage
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]  # character location up on the stage

# make character
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

# character move direction
character_to_x = 0

# character speed
character_speed = 5

# make weapon
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# shoot multiple weapons
weapons = []

# weapon speed
weapon_speed = 10

# make ball (4 size)
ball_images = [
	pygame.image.load(os.path.join(image_path, "balloon1.png")),
	pygame.image.load(os.path.join(image_path, "balloon2.png")),
	pygame.image.load(os.path.join(image_path, "balloon3.png")),
	pygame.image.load(os.path.join(image_path, "balloon4.png"))]

# ball size init speed
ball_speed_y = [-18, -15, -12, -9]  # index 0, 1, 2, 3 에 해당하는 값

# balls
balls = []

# first ball add
balls.append({
	"pos_x": 50,  # 공의 x 좌표
	"pos_y": 50,  # 공의 y 좌표
	"img_idx": 0,  # 공의 이미지 인덱스
	"to_x": 3,  # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
	"to_y": -6,  # y축 이동방향,
	"init_spd_y": ball_speed_y[0]})  # y 최초 속도

# remove ball, weapon
weapon_to_remove = -1
ball_to_remove = -1

running = True
while running:
	datetime = clock.tick(30)

	# 2. event process (keyboard, mouse)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:  # character to the left
				character_to_x -= character_speed
			elif event.key == pygame.K_RIGHT:  # character to the right
				character_to_x += character_speed
			elif event.key == pygame.K_SPACE:  # weapon shoot
				weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
				weapon_y_pos = character_y_pos
				weapons.append([weapon_x_pos, weapon_y_pos])

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				character_to_x = 0

	# 3. game character position
	character_x_pos += character_to_x

	if character_x_pos < 0:
		character_x_pos = 0
	elif character_x_pos > screen_width - character_width:
		character_x_pos = screen_width - character_width

	# weapon position
	# 100, 200 -> 180, 160, 140, ...
	# 500, 200 -> 180, 160, 140, ...
	weapons = [[w[0], w[1] - weapon_speed] for w in weapons]  # weapon position up

	# weapon position remove when it is above the screen
	weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

	# ball position
	for ball_idx, ball_val in enumerate(balls):
		ball_pos_x = ball_val["pos_x"]
		ball_pos_y = ball_val["pos_y"]
		ball_img_idx = ball_val["img_idx"]

		ball_size = ball_images[ball_img_idx].get_rect().size
		ball_width = ball_size[0]
		ball_height = ball_size[1]

		# change the ball direction when it hits the wall
		if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
			ball_val["to_x"] = ball_val["to_x"] * -1

		# change the ball direction when it hits the stage
		if ball_pos_y >= screen_height - stage_height - ball_height:
			ball_val["to_y"] = ball_val["init_spd_y"]
		else:  # when it is in the air
			ball_val["to_y"] += 0.5

		ball_val["pos_x"] += ball_val["to_x"]
		ball_val["pos_y"] += ball_val["to_y"]

	# 4. collision check

	# character rect information update
	character_rect = character.get_rect()
	character_rect.left = character_x_pos
	character_rect.top = character_y_pos

	for ball_idx, ball_val in enumerate(balls):
		ball_pos_x = ball_val["pos_x"]
		ball_pos_y = ball_val["pos_y"]
		ball_img_idx = ball_val["img_idx"]

		# ball rect information update
		ball_rect = ball_images[ball_img_idx].get_rect()
		ball_rect.left = ball_pos_x
		ball_rect.top = ball_pos_y

		# character and ball collision check
		if character_rect.colliderect(ball_rect):
			print("응 ㅅㄱ 님 털림ㅋ")
			running = False
			break

		# ball and weapon collision check
		for weapon_idx, weapon_val in enumerate(weapons):
			weapon_pos_x = weapon_val[0]
			weapon_pos_y = weapon_val[1]

			# weapon rect information update
			weapon_rect = weapon.get_rect()
			weapon_rect.left = weapon_pos_x
			weapon_rect.top = weapon_pos_y

			# collision check
			if weapon_rect.colliderect(ball_rect):
				weapon_to_remove = weapon_idx  # set the value of that weapon to be removed
				ball_to_remove = ball_idx  # set the value of that ball to be removed

				# if the ball is small, it disappears
				if ball_img_idx < 3:
					# get the current ball size
					ball_width = ball_rect.size[0]
					ball_height = ball_rect.size[1]

					# divide the ball into 2 small balls
					small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
					small_ball_width = small_ball_rect.size[0]
					small_ball_height = small_ball_rect.size[1]

					# add the small ball to the left
					balls.append({
						"pos_x": ball_pos_x + (ball_width / 2) - (small_ball_width / 2),  # ball position x
						"pos_y": ball_pos_y + (ball_height / 2) - (small_ball_height / 2),  # ball position y
						"img_idx": ball_img_idx + 1,  # ball image index
						"to_x": -3,  # x position move direction, -3 is left, 3 is right
						"to_y": -6,  # y position move direction
						"init_spd_y": ball_speed_y[ball_img_idx + 1]})  # y speed

					# add the small ball to the right
					balls.append({
						"pos_x": ball_pos_x + (ball_width / 2) - (small_ball_width / 2),  # ball position x
						"pos_y": ball_pos_y + (ball_height / 2) - (small_ball_height / 2),  # ball position y
						"img_idx": ball_img_idx + 1,  # ball image index
						"to_x": 3,  # x position move direction, -3 is left, 3 is right
						"to_y": -6,  # y position move direction
						"init_spd_y": ball_speed_y[ball_img_idx + 1]})  # y speed

				break

	# remove the ball and weapon that collided
	if ball_to_remove > -1:
		del balls[ball_to_remove]
		ball_to_remove = -1

	if weapon_to_remove > -1:
		del weapons[weapon_to_remove]
		weapon_to_remove = -1

	# 5. draw on the screen
	screen.blit(background, (0, 0))

	for weapon_x_pos, weapon_y_pos in weapons:
		screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

	for idx, val in enumerate(balls):
		ball_pos_x = val["pos_x"]
		ball_pos_y = val["pos_y"]
		ball_img_idx = val["img_idx"]
		screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

	screen.blit(stage, (0, screen_height - stage_height))
	screen.blit(character, (character_x_pos, character_y_pos))

	pygame.display.update()

pygame.quit()