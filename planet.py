import pyjsdl as pygame
import math
import os


class Planet:
    def __init__(self, surface, pos_x, pos_y, frame, image):

        print('planet')
        print(surface)
        print('image')
        print(image)

        self.isVisible = True
        self.x = pos_x
        self.y = pos_y
        if frame == "Earth":
            self.scale = (300, 300)
        else:
            self.scale = (100, 100)

        image_path = os.path.join('data', image)
        self.earth = pygame.image.load(image_path)
        earth_img = pygame.transform.scale(self.earth, self.scale)
        surface.blit(earth_img, (pos_x, pos_y))

    def update(self, surface, paused, frame, speed):

        print('planet')
        print(surface)

        if not paused:
            if frame == "Earth":
                self.scale = (300, 300)
            else:
                self.scale = (300 * math.sqrt(1 - speed**2), 300)
                self.x -= (0.9 * speed)

            self.set_visible()
            if self.isVisible:
                earth_img = pygame.transform.scale(self.earth, self.scale)
                surface.blit(earth_img, (self.x, self.y))

    def set_visible(self):

        for value in self.scale:
            if value <= 5:
                self.isVisible = False

    def getPosition(self):
        return self.x

