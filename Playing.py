import pygame
from pygame.locals import *
import Game_class
import Text_class
import Record_check
import Money
import sys
import Threads


def play_arcade(screen_import, event_user, clock, skins_num, load_img):
    k = Game_class.Game(skins_num, screen_import, load_img, clock)
    pygame.time.set_timer(event_user, 7000)
    d = clock
    while k.playing:
        keys1 = pygame.key.get_pressed()
        flag = k.update(keys1)
        if not flag:
            return k.score
        k.screen.screen.blit(k.back, (0, 0))
        k.screen.screen.blit(k.map.img, k.map.rect)

        for entity in k.player.body:
            if entity != k.head:
                if not entity.new:
                    k.screen.screen.blit(entity.now_img, entity.now_rect)
        k.screen.screen.blit(k.player.tail.now_img, k.player.tail.now_rect)
        k.screen.screen.blit(k.head.now_img, k.head.now_rect)
        k.build_obstacles()
        k.screen.screen.blit(k.score_text.surf, k.score_text.rect)
        k.praise_upd()
        k.screen.screen.blit(k.player.food.img, k.player.food.rect)
        if k.money:
            k.screen.screen.blit(k.money.img, k.money.rect)
        for event in pygame.event.get():
            if event.type == event_user:
                k.money_spawn()
            if event.type == QUIT:
                sys.exit()
        k.update_effects()
        pygame.display.flip()
        k.death_check()
        d.tick(60)
    pygame.time.set_timer(event_user, 0)
    return k.score


def death_playing(screen, score, clock, rules_import, skin_num):
    rules = rules_import
    inf = Money.money_checker(Money.get_money())
    record_text = Record_check.record(score, skin_num)
    while True:
        x = Text_class.GameOver(40, 50)
        screen.screen.blit(x.surf, x.rect)
        screen.screen.blit(rules, (30, 300))
        Record_check.print_record(30, 200, screen, record_text)
        Money.print_money(inf[1], 465, 450, screen)
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            return inf
        elif keys[K_SPACE]:
            return -1
        elif keys[K_f]:
            pass
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        pygame.display.flip()
        clock.tick(45)


def game_cycle(screen, clock, rules, event_user, load_img, num):
    while True:
        score = play_arcade(screen, event_user, clock, num, load_img)
        x = death_playing(screen, score, clock, rules, num)
        if x != -1:
            return x


def pause_screen_playing(screen, image, clock):
    screen.screen.blit(image, (0, 0))
    pygame.display.flip()
    while True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return 1
        elif keys[pygame.K_ESCAPE]:
            return 0
        pygame.event.get()
        clock.tick(60)


def main_menu(screen, images, clock, user_event, rules, load_image):
    inf = Money.money_checker(Money.get_money())
    flag = 0
    while True:
        mouse_click = pygame.mouse
        flag -= 1
        if mouse_click.get_pressed()[0]:
            x = mouse_click.get_pos()[0]
            y = mouse_click.get_pos()[1]
            if (x > 19) and (x < 581):
                if (y > 10) and (y < 90):
                    flag = 30
                    inf = game_cycle(screen, clock, rules, user_event, load_image, 0)
                elif (y > 110) and (y < 190) and inf[0] > 0:
                    flag = 30
                    inf = game_cycle(screen, clock, rules, user_event, load_image, 1)
                elif (y > 210) and (y < 290) and inf[0] > 1:
                    flag = 30
                    inf = game_cycle(screen, clock, rules, user_event, load_image, 2)
                elif (y > 310) and (y < 390) and inf[0] > 2:
                    flag = 30
                    inf = game_cycle(screen, clock, rules, user_event, load_image, 3)
        if pygame.key.get_pressed()[pygame.K_ESCAPE] and flag <= 0:
            sys.exit()
        for event in pygame.event.get():
            if event == QUIT:
                sys.exit()
        screen.screen.blit(images[inf[0]], (0, 0))
        Money.print_money(str(inf[1][0:inf[1].find('/'):1]), 220, 462, screen)
        pygame.event.get()
        pygame.display.flip()
        clock.tick(60)


def check_if_new():
    file = open('util_files/new_player.txt', 'r')
    flag = 0
    for letter in file:
        flag = letter
    file.close()
    if int(flag):
        file = open('util_files/new_player.txt', 'w')
        file.write('0')
        file.close()
        return 1
    else:
        return 0
