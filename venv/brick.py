import pygame


class Brick:

    def __init__(self, main_surface, width, height, color):
        self.main_surface = main_surface
        self.width = width
        self.height = height
        self.color = color

    def draw(self, x, y):
        pygame.draw.rect(self.main_surface, self.color, (x, y, self.width, self.height), 0)
        pygame.display.update()
