# Frank Zhang
# Jan.25th
# Finish the unit_ten project

import pygame, brick, sys
from pygame.locals import *


def main():
    pygame.init()
    mainSurface = pygame.display.set_mode((500, 250), 0, 32)
    pygame.display.set_caption("Brick Pyramid")
    width = (450 / 9)
    height = 20
    space = 5
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    WHITE = (255, 255, 255)
    x = 0
    y = 230
    number_bricks = 9
    color = [RED, ORANGE, YELLOW, GREEN, CYAN]
    mainSurface.fill(WHITE)
    for b in range(5):
        c = color[b]
        x = (width + space) * b
        for a in range(number_bricks):
            bricks = brick.Brick(mainSurface, width, height, c)
            bricks.draw(x,y)
            x = x + width + space
        y = y - height - space
        number_bricks = number_bricks - 2


    # for c in range(9):
    #     bricks = brick.Brick(mainSurface, width, height, RED)
    #     bricks.rect.x = x
    #     bricks.rect.y = y
    #     mainSurface.blit(bricks.image, bricks.rect)
    #     x = x + width + space
    #     y = y + height + width
    #     x = 0
    # bricks.draw(0, 245)


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

main()