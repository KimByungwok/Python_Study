# 1. Add a variable to check if the game is over
# 2. Add a variable to check if the game is finished
# 3. Add a variable to display the game result

# Project) make a game like PongPong in the arcade
#
# [Game Conditions]
# 1. The character is located at the bottom of the screen, and can move only left and right.
# 2. The character fires a weapon with the space bar.
# 3. the ball moves in a random direction at the start of the game.
# 4. The ball bounces off the wall and the character.
# 5. all balls destroyed (success)
# 6. the character is hit by the ball (game over)
# 7. time limit 99 seconds (game over)
# 8. FPS is 30 (speed value is adjusted if necessary)
#
# [game image]
# 1. background : 640 * 480 width, height - background.png
# 2. stage : 640 * 50 - stage.png
# 3. character : 33 * 60 - character.png
# 4. weapon : 20 * 430 - weapon.png
# 5. ball : 160 * 160, 80 * 80, 40 * 40, 20 * 20 - balloon1.png ~ balloon4.png

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
pygame.display.set_caption("classic game")

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

# font set
game_font = pygame.font.Font(None, 40)
total_time = 100
start_ticks = pygame.time.get_ticks()  # start time set

# game over message / time out message , mission complete message, game over message (time out, character hit, failed)
game_result = "Game Over LOL"

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
        else:  # continue the game
            continue  # continue the inner loop
        break # if in the inner loop, break the outer loop

    # for 탈출 조건
    # for 바깥 조건:
    #     바깥 동작
    #     for 안쪽 조건:
    #         안쪽 동작
    #         if 충돌하면 :
    #             break
    #     else:
    #         continue
    #     break

    # remove the ball and weapon that collided
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # if all balls are gone, game clear
    if len(balls) == 0:
        game_result = "Mission Complete"
        running = False

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

    # timer display on the screen
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # convert to seconds
    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    pygame.display.update()

    # # if the time is up
    # if total_time - elapsed_time <= 0:
    #     print("Time Over")
    #     running = False

    # if the time is up2
    msg = game_font.render(game_result, True, (255, 255, 0)) # yellow
    msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
    screen.blit(msg, msg_rect)

pygame.display.update()

# delay 2 seconds
pygame.time.delay(2000)

pygame.quit()
