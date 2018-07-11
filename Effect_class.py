

class Effect:
    def __init__(self, font, x, y):
        self.lifetime = 0
        self.surf = font
        self.rect = [x, y]

    def update(self):
        self.lifetime += 1
        self.rect[1] -= 0.5
        if self.lifetime > 50:
            return True


class ComplexEffect:
    def __init__(self, images, x, y):
        self.stage = 0
        self.rect = [x, y]
        self.pictures = images
        self.surf = self.pictures[0]

    def update(self):
        self.stage += 0.5
        if int(self.stage) == self.pictures.__len__() - 1:
            return True
        self.surf = self.pictures[int(self.stage)]

