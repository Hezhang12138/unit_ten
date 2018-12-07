import pygame, sys, logo
from pygame.locals import *

pygame.init()
mainSurface = pygame.display.set_mode((500, 250), 0, 32)
pygame.display.set_caption("Pygame Test Window")
ssfs = logo.Logo(mainSurface)
ssfs.draw_rectangles()
ssfs.draw_trellis()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()