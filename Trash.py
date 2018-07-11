

# to Blocks_classes
class SnakeBodyBlock(Block):
    def __init__(self, x, y):
        super(SnakeBodyBlock, self).__init__()
        self.surf.fill((255, 165, 79))
        self.rect.left = x
        self.rect.top = y
        self.all_rect = []
        self.all_img = []
        #self.rect = self.all_rect[0]
        #self.img = self.all_img[0]
        self.condition = 0


class SnakeHead(Block):
    def __init__(self, x, y, file_name):
        super(SnakeHead, self).__init__()
        self.file = file_name
        self.surf.fill((181, 230, 29))
        self.all_conditions = []
        self.all_images = []
        self.add_conditions(x, y)
        self.rect = self.all_conditions[0]
        self.img = self.all_images[0]
        self.condition = []

    def add_conditions(self, x, y):
        for num in range(4):
            inter_img = pygame.image.load(self.file.format(num)).convert()
            inter_img.set_colorkey((181, 230, 29), RLEACCEL)
            inter_rect = inter_img.get_rect()
            self.all_conditions.append(inter_rect)
            self.all_images.append(inter_img)
        self.rect.left = x
        self.rect.top = y

    def change_condition(self, before_go, go, x, y):
        if before_go != ['k']:
            # if we change the tail
            if abs(go[1]) != abs(before_go[1]) or abs(go[0]) != abs(before_go[0]):
                go = before_go

        if go == [1, 0]:
            self.rect = self.all_conditions[0]
            self.img = self.all_images[0]
            self.condition = 0
        elif go == [-1, 0]:
            self.rect = self.all_conditions[2]
            self.img = self.all_images[2]
            self.condition = 2
        elif go == [0, -1]:
            self.rect = self.all_conditions[1]
            self.img = self.all_images[1]
            self.condition = 1
        elif go == [0, 1]:
            self.rect = self.all_conditions[3]
            self.img = self.all_images[3]
            self.condition = 3
        self.rect.left = x
        self.rect.top = y

pygame.init()
pygame.font.init()
MONEYSPAWN = USEREVENT + 2
pygame.time.set_timer(MONEYSPAWN, 20000)
k = Game_class.Game(1)
d = pygame.time.Clock()
while k.playing:
    keys1 = pygame.key.get_pressed()
    k.update(keys1)
    k.screen.screen.blit(k.back, (0, 0))
    k.screen.screen.blit(k.map.img, k.map.rect)
    k.screen.screen.blit(k.player.food.img, k.player.food.rect)
    for entity in k.player.body:
        if entity != k.head:
            if not entity.new:
                k.screen.screen.blit(entity.now_img, entity.now_rect)
    k.screen.screen.blit(k.player.tail.now_img, k.player.tail.now_rect)
    k.screen.screen.blit(k.head.now_img, k.head.now_rect)
    k.build_obstacles()
    k.screen.screen.blit(k.score_text.surf, k.score_text.rect)
    k.praise_upd()
    if k.money:
        k.screen.screen.blit(k.money.img, k.money.rect)
    for event in pygame.event.get():
        if event.type == MONEYSPAWN:
            k.money_spawn()
        if event.type == QUIT:
            quit()

    pygame.display.flip()
    k.death_check()
    d.tick(60)

