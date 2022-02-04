import pyjsdl as pygame


class Train:
    def __init__(self, surface):

        self.reverse = False

        self.x = -400
        self.y = 300
        self.scale = (400, 423)

        self.train = pygame.image.load("output/assets/train.png")
        self.train_img = pygame.transform.scale(self.train, self.scale)

        self.man = pygame.image.load("output/assets/Hat_man/Walk/Hat_man3.png")
        self.man_img = pygame.transform.scale(self.man, (100, 100))

        surface.blit(self.train_img, (self.x, self.y))
        surface.blit(self.man_img, (self.x + 150, self.y + 130))

    def update(self, surface):
        if self.x >= 1200:
            self.reverse = True

        elif self.x <= 10:
            self.reverse = False

        if not self.reverse:
            self.x += 5

        elif self.reverse:
            self.x -= 5

        surface.blit(self.train_img, (self.x, self.y))
        surface.blit(self.man_img, (self.x + 150, self.y + 130))
