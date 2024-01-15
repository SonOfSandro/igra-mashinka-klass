import os
import sys

import pygame
from pygame.locals import *

from Button import Button


def load_image(name):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    return pygame.image.load(fullname)


image = load_image("6f0ba123694237563273de19be2.gif")
if __name__ == '__main__':
    pygame.init()
    size = width, height = 1350, 720
    screen = pygame.display.set_mode(size)
    surf = image
    rect = surf.get_rect()
    screen.blit(surf, rect)
    btn = Button()
    btn.create_button(screen, "black", 625, 360, 100, 40, 5, "start", "white")
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                if btn.pressed(pygame.mouse.get_pos()):
                    gs_size = w, h = 800, 800
                    game_screen = pygame.display.set_mode(gs_size)
                    game_image = load_image("field.png")
                    game_rect = game_image.get_rect()
                    game_screen.blit(game_image, game_rect)
                    pygame.display.flip()
        pygame.display.update()
    pygame.quit()
