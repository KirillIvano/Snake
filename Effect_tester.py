import pygame

pygame.init()
a = pygame.display.set_mode((75, 75))
d = pygame.time.Clock()
i = 0
images = [pygame.image.load('images/food_eat/stage_{}.png'.format(i)) for i in range(0, 10)]
while 1:
    a.blit(images[int(i) % 10], (0, 0))
    keys = pygame.key.get_pressed()
    back = pygame.Surface((75, 75))
    back.fill((0, 0, 0))
    i += 0.2
    if int(i) == 10:
        i = 0
    pygame.event.get()
    images[int(i) % 10].set_colorkey((181, 230, 29))
    a.blit(back, (0, 0))
    a.blit(images[int(i)], (0, 0))
    pygame.display.flip()
    d.tick(15)



