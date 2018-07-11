import pygame
from Blocks_classes import Block


class StaticTextBlock(pygame.sprite.Sprite):

    def __init__(self, img_name, x, y):
        super(StaticTextBlock, self).__init__()
        self.img = pygame.image.load('images/' + img_name + '.png')
        self.img.set_colorkey((181, 230, 29))
        self.rect = self.img.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.kill()


class GameOver:
    def __init__(self, x, y):
        self.my_font = pygame.font.Font('util_files/Futurist Stencil Regular.ttf', 90)
        self.surf = self.my_font.render('GAME OVER', False, (168, 0, 64))
        self.rect = self.surf.get_rect()
        self.rect.left = x
        self.rect.top = y


class ScoreBlock(Block):
    def __init__(self, score):
        font_type = 'util_files/sin.ttf'
        font_size = 25
        super(ScoreBlock).__init__()
        self.my_font = pygame.font.Font(font_type, font_size)
        self.surf = self.my_font.render('score: ' + str(score), False, (0, 0, 0))
        self.rect = self.surf.get_rect()
        self.rect.left = 450
        self.rect.top = 28


class PraiseBlock(Block):
    def __init__(self, file_name):
        super(PraiseBlock, self).__init__()
        self.img = None
        self.rect = None
        self._counter = 0
        self.choose(file_name)
        self.rect.left = 0
        self.rect.top = -10

    def choose(self, file_name):
        self.img = pygame.image.load('images/' + file_name + '.png')
        self.img = pygame.transform.rotate(self.img, 45)
        self.img = pygame.transform.scale(self.img, (200, 150))
        self.img.set_colorkey((0, 0, 0))
        self.rect = self.img.get_rect()

    def counter_update(self):
        self._counter += 1
        if self._counter == 100:
            return 0
        else:
            return 1


class ScoreViewer(Block):
    def __init__(self, fontname, x, y):
        super(ScoreViewer).__init__()
        self.score_color = (0, 0, 0)
