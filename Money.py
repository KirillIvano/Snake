import pygame
import Encoder


def money_checker(money):
    if money < 10:
        num = 0
        text = '{} / 10'.format(money)
    elif money < 25:
        num = 1
        text = '{} / 25'.format(money)
    elif money < 50:
        num = 2
        text = '{} / 50'.format(money)
    else:
        num = 3
        text = '{} /inf'.format(money)
    return [num, text]


def get_num_of_skins():
    file = open('util_files/sn.txt', 'r')
    txt = file.read()
    file.close()
    return txt


def get_money():
    file = open('util_files/money.txt', 'r')
    all_money = 0

    for num in file:
        all_money = 10 * all_money + int(num)

    file.close()
    return Encoder.decrypt(all_money)


def print_money(text, x, y, screen):
    my_font = pygame.font.SysFont('Impact', 25)
    surf = my_font.render(text, False, (255, 211, 95))
    screen.screen.blit(surf, (x, y))
    coin = pygame.image.load('images/coin.png')
    coin.set_colorkey((181, 230, 29))
    pygame.transform.scale(coin, (30, 30))
    screen.screen.blit(coin, (x-30, y+3))
