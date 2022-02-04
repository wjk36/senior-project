import math
import pyjsdl as pygame
import random
import os


class Rocket:
    def __init__(self, surface, x_pos, y_pos):

        print('rocket')
        print(surface)

        self.x = x_pos
        self.y = y_pos

        self.scale = (100, 123)

        image_path = os.path.join('data', 'airship.png')
        self.rocket = pygame.image.load(image_path)
        print(self.rocket)
        rocket_img = pygame.transform.scale(self.rocket, self.scale)

        surface.blit(rocket_img, (x_pos, y_pos))

    def update(self, surface, paused, frame, speed):

        print('rocket')
        print(surface)
        print(self.rocket)

        if frame == "Rocket":
            self.scale = (100, 53)
        else:
            self.scale = (100 * math.sqrt(1 - speed**2), 83)
            self.x += (0.9 * speed)

        if not paused:

            if self.y <= 100:
                self.y += 2
            elif self.y >= 500:
                self.y -= 2
            else:
                self.y += random.randint(-1, 1)

            rocket_img = pygame.transform.scale(self.rocket, self.scale)
            surface.blit(rocket_img, (self.x, self.y))

    def getPosition(self):
        return self.x
