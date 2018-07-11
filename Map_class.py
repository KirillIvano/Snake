import pygame


class GameMap(pygame.sprite.Sprite):
    def __init__(self, num):
        super(GameMap, self).__init__()
        try:
            self.img = pygame.image.load('images/map_{}.png'.format(num))
        except pygame.error:
            self.img = pygame.image.load('images/map_0.png')
        self.rect = self.img.get_rect()
        self.rect.left = self.rect.top = 0





