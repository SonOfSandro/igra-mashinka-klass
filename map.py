import random

import pygame


def draw_text(screen, text, x, y):
    text_surface = pygame.font.Font(None, 60).render(text, True, (255, 255, 255))
    screen.blit(text_surface, (x, y))


def spawn():
    line = random.randint(0, 4)
    times = random.randint(3, 4)
    boxes_x = []
    for i in range(times):
        boxes_x.append(100 + 120 * line)
        line = random.randint(0, 4)
    return boxes_x


def check_collision(cube_point, rectangle_point):
    cube_x, cube_y = cube_point
    rectangle_x, rectangle_y = rectangle_point

    cube_width = 128
    cube_height = 128

    rectangle_width = 40
    rectangle_height = 104

    if (cube_x < rectangle_x + rectangle_width and
            cube_x + cube_width > rectangle_x and
            cube_y < rectangle_y + rectangle_height and
            cube_y + cube_height > rectangle_y):
        return True
    else:
        return False
