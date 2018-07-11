import pygame


class Screen:
    def __init__(self, screen_width, screen_height):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('COMMON SNAKE')
        self.img = pygame.image.load('images/icon.png')
        pygame.display.set_icon(self.img)