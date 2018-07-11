import pygame
import Encoder
# rewrites record if needed
# returns record


def record_check(score, game_num):
    file = open('util_files/record_{}.txt'.format(game_num), 'r')
    last_score = ''
    for letter in file:
        last_score += str(letter)
    last_score = Encoder.decrypt(int(last_score))
    file.close()
    if score > last_score:
        file = open('util_files/record_{}.txt'.format(game_num), 'w')
        file.write(str(Encoder.encrypt(score)))
        file.close()
        return [last_score, True]
    else:
        return [last_score, False]


def record(new_record, num):
    old_record = record_check(new_record, num)

    if old_record[1]:
        new_record = '    new record: ' + str(new_record)
    else:
        new_record = '              score: ' + str(new_record)
    for_print = 'record: ' + str(old_record[0]) + new_record
    return for_print


def print_record(x, y, screen, for_print):
    my_font = pygame.font.Font('util_files/Futurist Stencil Regular.ttf', 35)
    surf = my_font.render(for_print, False, (168, 0, 64))
    screen.screen.blit(surf, (x, y))




