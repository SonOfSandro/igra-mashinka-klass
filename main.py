import os
import sys

import pygame
from Button import Button
from map import spawn, draw_text, check_collision


def load_image(name):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    return pygame.image.load(fullname)


if __name__ == '__main__':
    image = load_image("6f0ba123694237563273de19be2.gif")
    pygame.init()
    ball = pygame.image.load('Car.png')
    ballX = 335
    ballY = 600
    speed = 7
    to_left = False
    to_right = False
    to_up = False
    to_down = False
    size = width, height = 1350, 720
    screen = pygame.display.set_mode(size)
    surf = image
    rect = surf.get_rect()
    screen.blit(surf, rect)
    btn = Button()
    btn.create_button(screen, "black", 625, 360, 100, 40, 5, "start", "white")
    pygame.display.update()
    running = True
    box_y = -100
    gs_size = w, h = 800, 800
    game_image = load_image("field.png")
    game_rect = game_image.get_rect()
    game_screen = screen
    btn_pressed = False
    your_score = 0
    box_spawn = spawn()
    text_x = 40
    box = pygame.image.load("box.png")
    while running:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if btn.pressed(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and not btn_pressed:
                game_screen = pygame.display.set_mode(gs_size)
                game_screen.blit(game_image, game_rect)
                game_screen.blit(ball, (ballX, ballY))
                pygame.draw.rect(game_screen, "black", (0, 0, 100, 70))
                btn_pressed = True
                pygame.display.update()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_left = True
                if event.key == pygame.K_RIGHT:
                    to_right = True
                if event.key == pygame.K_DOWN:
                    to_down = True
                if event.key == pygame.K_UP:
                    to_up = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    to_left = False
                if event.key == pygame.K_RIGHT:
                    to_right = False
                if event.key == pygame.K_DOWN:
                    to_down = False
                if event.key == pygame.K_UP:
                    to_up = False
        if to_right:
            ballX += speed
        if to_left:
            ballX -= speed
        if to_down:
            ballY += speed
        if to_up:
            ballY -= speed
        if btn_pressed:
            game_screen.blit(game_image, game_rect)
            game_screen.blit(ball, (ballX, ballY))
            pygame.draw.rect(game_screen, "black", (0, 0, 100, 70))
            pygame.draw.rect(game_screen, "white", (0, 0, 100, 70), 5)
            if 99 >= your_score >= 10:
                text_x = 27
            elif your_score > 99:
                text_x = 15
            draw_text(game_screen, str(your_score), text_x, 17)
            for i in range(len(box_spawn)):
                game_screen.blit(box, (box_spawn[i], box_y))
                cube_point = (box_spawn[i], box_y)
                rectangle_point = (ballX, ballY)
                collision = check_collision(cube_point, rectangle_point)
                print("Столкновение:", collision)

            box_y += 10
            if box_y >= 900:
                your_score += 1
                box_spawn = spawn()
                box_y = -100

            pygame.display.update()
        if ballX >= 624 or ballX <= 48:
            pass
        if ballY >= 800 or ballY <= 0:
            pass
    pygame.quit()
