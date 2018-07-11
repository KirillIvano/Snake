import pygame
import Blocks_classes


class Snake:
    def __init__(self, style, food_img):
        self.body = pygame.sprite.Group()
        self.food = Blocks_classes.FoodBlock(100, 100, food_img)
        self.straight_img = pygame.image.load('images/snake_body_{}.png'.format(style)).convert()
        self.turn_img = pygame.image.load('images/turn_{}.png'.format(style)).convert()
        self.head_img = pygame.image.load('images/snake_head_{}.png'.format(style)).convert()
        self.tail_img = pygame.image.load('images/tail_{}.png'.format(style)).convert()
        self.add_part(50, 25, True)
        self.last_added_part = self.add_part(25, 25)
        self.X_speed = 25
        self.Y_speed = 25
        self.coordinate = [0, 0]
        self.digit_coordinate = [0, 0]
        self.tail = Blocks_classes.SnakeTail(0, 0, self.tail_img)
        self.inter_movement = []
        self.before_tale = []

    def add_part(self, x, y, head=False):
        if head:
            f = Blocks_classes.SnakeHeadDemo(x, y, self.head_img)
            self.body.add(f)
            return f
        else:
            f = Blocks_classes.SnakeBodyBlockDemo(x, y, self.turn_img, self.straight_img)
            self.body.add(f)
            return f

    def move_part(self, x, y):
        i = 0
        for now in self.body:
            #
            self.digit_coordinate = self.coordinate
            # for the head; controls edges of the screen
            if i == 0:
                self.coordinate = [now.now_rect.left, now.now_rect.top]
                self.inter_movement = now.movement = [x, y]
                now.rect.move_ip(x*self.X_speed, y*self.Y_speed)
                if now.rect.left < 0:
                    now.rect.left = 600 - self.X_speed
                elif now.rect.right > 600:
                    now.rect.right = self.X_speed
                elif now.rect.bottom > 500:
                    now.rect.bottom = self.Y_speed
                elif now.rect.top < 0:
                    now.rect.top = 500 - self.Y_speed
            #
            else:
                # for new elements
                self.coordinate = [now.now_rect.left, now.now_rect.top]
                if now.movement:
                    now.movement, self.inter_movement = self.inter_movement, now.movement
                else:
                    now.movement = self.inter_movement
                now.change_condition(now.movement, self.inter_movement, self.digit_coordinate[0], self.digit_coordinate[1])
                now.now_rect.left = self.digit_coordinate[0]
                now.now_rect.top = self.digit_coordinate[1]
                self.before_tale = self.inter_movement
                # remember , where the tail should turn

            i += 1
        self.tail.change_condition(self.before_tale, self.inter_movement, self.coordinate[0],
                                   self.coordinate[1])



