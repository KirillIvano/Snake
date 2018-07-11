import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((600, 500))
for i in range(24):
    for j in range(20):
        image = pygame.image.load('sands/sand_7.png')
        rect = image.get_rect()
        rect.left = i * 25
        rect.top = j * 25
        screen.blit(image, rect)

pygame.display.flip()
time.sleep(100)