import pygame
import WallMaps


class AllWalls:
    def __init__(self, num, image):
        self.map = []
        self.get_map(num)
        self.walls = pygame.sprite.Group()
        self.build_all_walls(image)

    def get_map(self, num):
        self.map = WallMaps.map_return(num)

    def build_all_walls(self, image):
        for i in range(20):
            for j in range(24):
                if self.map[i][j] == 1:
                    self.walls.add(Wall(j*25, i*25, image))


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(Wall, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.wall_img = image
        self.wall_img.set_colorkey((34, 177, 75))
        self.rect = image.get_rect()
        self.rect.left = x
        self.rect.top = y
