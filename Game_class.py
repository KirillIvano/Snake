import pygame
import random
import Blocks_classes
import Snake_class as Sn
import Map_class
import Text_class
import Wall_class
import sys
import Effect_class
import Audio_class
import Playing
import Encoder
import queue
import threading


def load_it(text, num):
    try:
        return pygame.image.load(text.format(num)).convert()
    except pygame.error:
        return pygame.image.load(text.format(1)).convert()


class LoadScreen(threading.Thread):
    def __init__(self, screen, back, changing, clock):
        super(LoadScreen,self).__init__()
        self.screen = screen
        self.back = back
        self.changing = changing
        self.clock = clock

    def run(self):
        while True:
            self.screen.screen.blit(self.back, (0, 0))
            self.changing = pygame.transform.rotate(self.changing, 2)
            self.screen.screen.blit(self.changing)
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                sys.exit()
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    sys.exit()
            self.clock.tick(30)

class Game:
    def __init__(self, game_type, screen_import, load_img, clock):
        self.changing = pygame.image.load('images/snake_load.png')
        self.changing.set_colorkey((181, 230, 29))
        self.W = 600
        self.H = 500
        self.load = load_img
        self.clock = clock
        self.screen = screen_import
        self.loader = LoadScreen(self.screen, self.load, self.changing, self.clock)
        self.set_load_image()
        self.money = None
        self.musician = Audio_class.Audio(8)
        self.score = 0
        self.tick_time = 9
        self.counter = 0
        self.counter_1 = 0
        self.money_eat_images = [pygame.image.load('images/money_eat/stage_{}.png'.format(i)) for i in range(0, 13)]
        self.food_eat_images = [pygame.image.load('images/food_eat/stage_{}.png'.format(i)) for i in range(0, 10)]
        self.set_pictures()
        self.plus_money_font = pygame.font.SysFont('Consolas', 15).render('+1 coin', False, (102, 0, 102))
        self.plus_score_font = pygame.font.SysFont('Consolas', 15).render('+10 points', False, (0, 0, 0))
        self.effects = []
        self.tail_long = pygame.sprite.Group()
        self.food_img = load_it('images/food_{}.png', game_type)
        self.map = Map_class.GameMap(game_type)
        self.player = Sn.Snake(game_type, self.food_img)
        for now in self.player.body:
            self.head = now
            break
        self.last = [1, 0]
        self.back = pygame.Surface((self.W, self.H))
        self.back.fill((0, 0, 0))
        self.score_text = Text_class.ScoreBlock(0)
        self.praise = None
        self.playing = True
        self.money_img = pygame.image.load('images/coin.png')
        self.wall_img = load_it('images/wall_{}.png', game_type)
        self.wall_img.set_colorkey((0, 0, 0))
        self.obstacles = Wall_class.AllWalls(game_type, self.wall_img).walls
        self.money_score = 0

    def set_pictures(self):
        for one in self.money_eat_images:
            one.set_colorkey((181, 230, 29))
        for another_one in self.food_eat_images:
            another_one.set_colorkey((181, 230, 29))
            pygame.transform.scale(another_one, (50, 50))

    def money_effect(self, x, y):
        self.effects.append(Effect_class.Effect(self.plus_money_font, x, y))
        self.effects.append(Effect_class.ComplexEffect(self.money_eat_images, x-50, y-25))

    def food_effect(self, x, y):
        self.effects.append(Effect_class.Effect(self.plus_score_font, x, y))
        self.effects.append(Effect_class.ComplexEffect(self.food_eat_images, x-50, y-25))

    def update_effects(self):
        for effect in self.effects:
            if effect.update():
                self.effects.remove(effect)
            else:
                self.screen.screen.blit(effect.surf, effect.rect)

    def set_load_image(self):
        load_image = pygame.image.load('images/loading_screen.png')
        rect = load_image.get_rect()
        self.screen.screen.blit(load_image, rect)
        pygame.display.flip()

    def change_score(self, plus):
        self.score += plus
        self.score_text = Text_class.ScoreBlock(self.score)

    def add_food(self):
        while True:
            x_place = random.randint(0, ((self.W - 25) // 25))
            y_place = random.randint(0, ((self.H - 25) // 25))
            self.player.food = Blocks_classes.FoodBlock(x_place * 25, y_place * 25, self.food_img)
            if not (pygame.sprite.spritecollideany(self.player.food, self.player.body) or self.player.food.rect.left ==
                    self.head.rect.left and self.player.food.rect.top == self.head.rect.top
                    or pygame.sprite.spritecollideany(self.player.food, self.obstacles)):
                break

    def food_check(self, x, y):
        if pygame.sprite.spritecollideany(self.player.food, self.player.body):
            self.food_effect(self.player.food.rect.left+25, self.player.food.rect.top)
            self.add_food()
            self.player.last_added_part = self.player.add_part(x, y)
            self.tail_long.add(self.player.last_added_part)
            self.change_score(10)

    def death_check(self):
        if pygame.sprite.spritecollideany(self.head, self.tail_long)\
                or pygame.sprite.collide_rect(self.head, self.player.tail) or \
                pygame.sprite.spritecollideany(self.head, self.obstacles):
            self.screen.screen.blit(self.back, (0, 0))
            Audio_class.play_death()
            self.musician.stop_it_man()
            self.playing = False
            self.money_update()

    def build_obstacles(self):
        for everything in self.obstacles:
            self.screen.screen.blit(everything.wall_img, everything.rect)

    def praise_upd(self):
        if self.praise:
            self.screen.screen.blit(self.praise.img, self.praise.rect)
            if not self.praise.counter_update():
                self.praise = None
        else:
            file = 0
            if self.score == 50:
                file = 'way_to_go'
                self.tick_time = 7
            elif self.score == 100:
                file = 'well_done'
                self.tick_time = 6
            elif self.score == 200:
                file = 'good_work'
                self.tick_time = 6
            elif self.score == 300:
                file = 'nice'
                self.tick_time = 5
            elif self.score == 400:
                file = 'brilliant'
                self.tick_time = 4
            elif self.score == 500:
                self.tick_time = 3
                file = 'perfect'
            elif self.score == 600:
                self.tick_time = 2
            elif self.score == 750:
                file = 'holy_shit'
                self.tick_time = 2
            elif self.score == 1000:
                file = 'oh,jesus'
                self.tick_time = 1
            if file:
                self.praise = Text_class.PraiseBlock(file)

    def change_last_part_condition(self):
        self.counter_1 += 1
        if self.counter_1 == self.tick_time:
            self.counter_1 = 0
            self.player.last_added_part.new = False

    def money_spawn(self):
        self.money = Blocks_classes.MoneyBlock(self.money_img)

    def money_check(self):
        self.money.money_update()
        if pygame.sprite.collide_rect(self.money, self.head):
            self.money_score += 1
            Audio_class.money_sound()
            self.money_effect(self.money.rect.left + 25, self.money.rect.top)

            self.money = None
        elif self.money.rect.top == 500:
            self.money = None

    def money_update(self):
        file = open('util_files/money.txt', 'r')
        all_money = 0

        for num in file:
            all_money = 10*all_money + int(num)
        all_money = Encoder.decrypt(all_money)
        file.close()
        file = open('util_files/money.txt', 'w')
        all_money += self.money_score
        file.write(str(Encoder.encrypt(all_money)))

    def update(self, keys):
        self.counter += 1
        self.death_check()
        flag = 1
        if keys[pygame.K_ESCAPE]:
            sys.exit()
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.head.condition != 2:
                self.last = [1, 0]
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.head.condition != 0:
                self.last = [-1, 0]
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.head.condition != 3:
                self.last = [0, -1]
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.head.condition != 1:
                self.last = [0, 1]
        if keys[pygame.K_f]:
            flag = Playing.pause_screen_playing(self.screen, self.load, self.clock)
        if keys[pygame.K_p] and self.counter == self.tick_time:
                self.musician.stop_it_man()
        elif keys[pygame.K_o] and self.counter == self.tick_time:
                self.musician.play_another_one()
        if (self.last[0] or self.last[1]) and self.counter == self.tick_time:
            self.player.move_part(self.last[0], self.last[1])
            self.head.change_condition(['k'], self.last, self.head.rect.left, self.head.rect.top)
        if self.counter == self.tick_time:
            self.player.last_added_part.new = False
            self.counter = 0
            self.food_check(self.player.digit_coordinate[0], self.player.digit_coordinate[1])
            self.musician.play_something_bro()
        if not flag:
            self.musician.stop_it_man()
        if self.money:
            self.money_check()
        return flag
#        self.death_check()

