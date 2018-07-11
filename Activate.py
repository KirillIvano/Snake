import Playing
import pygame
import Screen_class
import Money
from pygame.locals import *


pygame.init()
pygame.font.init()
d = pygame.time.Clock()
screen = Screen_class.Screen(600, 500)
introducing = pygame.image.load('images/starting.png')
Playing.pause_screen_playing(screen, introducing, d)
main_menu_img = [pygame.image.load('images/main_menu_{}.png'.format(i)).convert() for i in range(0, 4)]
inf = Money.money_checker(Money.get_money())
num_of_skins = inf[0]
text_for_money = inf[1]
MONEY_SPAWN = USEREVENT + 2

rules = pygame.image.load('images/rules.png').convert()
while True:
    Playing.main_menu(screen, main_menu_img, d, MONEY_SPAWN, rules, introducing)