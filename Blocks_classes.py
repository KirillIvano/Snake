import pygame
from pygame.locals import *
import Audio_class
import random

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super(Block, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.movement = []


class FoodBlock(Block):
    def __init__(self, x, y, image):
        super(FoodBlock, self).__init__()
        self.img = image
        self.img.set_colorkey((181, 230, 29))
        self.rect = self.img.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.coordinates = [x, y]
        Audio_class.play_an_apple()


class SnakeHeadDemo(Block):
    def __init__(self, x, y, image):
        super(SnakeHeadDemo, self).__init__()
        self.img = image
        self.img.set_colorkey((181, 230, 29))
        self.rect = self.img.get_rect()
        self.now_img = self.img
        self.now_rect = self.rect
        self.condition = 0
        self.rect.left = x
        self.rect.top = y

    def change_condition(self, before_go, go, x, y):
        if before_go != ['k']:
            # if we change the tail

            if abs(go[1]) != abs(before_go[1]) or abs(go[0]) != abs(before_go[0]):
                go = before_go

        if go == [1, 0]:
            self.condition = 0
        elif go == [-1, 0]:
            self.condition = 2
        elif go == [0, -1]:
            self.condition = 1
        elif go == [0, 1]:
            self.condition = 3

        self.now_img = pygame.transform.rotate(self.img, 90 * self.condition)
        self.now_rect = self.now_img.get_rect()
        self.rect = self.now_rect
        self.now_rect.left = x
        self.now_rect.top = y


class SnakeTail(SnakeHeadDemo):
    def __init__(self, x, y, image):
        super(SnakeTail, self).__init__(x, y, image)
        self.img.set_colorkey((181, 230, 29))


class SnakeBodyBlockDemo(Block):
    # conditions:0 - left,right; 1-down,up; 2,3,4,5 - RU,UL,DL,RD
    def __init__(self, x, y, turn, straight):
        super(SnakeBodyBlockDemo, self).__init__()
        self.new = True
        self.straight_img = straight
        self.turn_img = turn
        self.straight_img.set_colorkey((181, 230, 29))
        self.turn_img.set_colorkey((181, 230, 29))
        self.straight_rect = self.straight_img.get_rect()
        self.turn_rect = self.turn_img.get_rect()
        self.now_img = self.straight_img
        self.now_rect = self.straight_rect
        self.condition = 0
        self.now_rect.left = x
        self.now_rect.top = y

    def change_condition(self, before_go, go, x, y):
        if not before_go:
            before_go = [0, 0]
        if abs(go[0]) != abs(before_go[0]) or abs(go[1]) != abs(before_go[1]):
            # Up - Right turn
            if (go == [0, 1] and before_go == [1, 0]) or (go == [-1, 0] and before_go == [0, -1]):
                self.condition = 2
            # Up - Left turn
            elif (go == [0, 1] and before_go == [-1, 0]) or (go == [1, 0] and before_go == [0, -1]):
                self.condition = 3
            # Right-Down turn
            elif (go == [-1, 0] and before_go == [0, 1]) or (go == [0, -1] and before_go == [1, 0]):
                self.condition = 5
            # Left - Down turn
            elif (go == [1, 0] and before_go == [0, 1]) or (go == [0, -1] and before_go == [-1, 0]):
                self.condition = 4
            self.now_img = pygame.transform.rotate(self.turn_img, 90 * (self.condition - 2))
            self.now_rect = self.turn_rect

        else:
            if go == [1, 0]:
                self.condition = 0
            elif go == [0, -1]:
                self.condition = 1
            elif go == [-1, 0]:
                self.condition = 2
            elif go == [0, 1]:
                self.condition = 3
            self.now_img = pygame.transform.rotate(self.straight_img, 90 * self.condition)
            self.now_rect = self.straight_rect
        self.now_rect.left = x
        self.now_rect.top = y
        self.rect = self.now_rect


class GrassBlock(Block):
    def __init__(self, x, y, grass_num):
        super(GrassBlock, self).__init__()
        self.img = pygame.image.load('images/grass_{}.png'.format(grass_num)).convert()
        self.rect = self.img.get_rect()
        self.rect.left = x
        self.rect.top = y


class MoneyBlock(pygame.sprite.Sprite):
    def __init__(self, image):
        super(MoneyBlock, self).__init__()
        self.img = image
        self.img.set_colorkey((181, 230, 29))
        self.rect = self.img.get_rect()
        self.rect.left = random.randint(1, 22) * 25
        self.rect.top = -25

    def money_update(self):
        self.rect.top += 3



