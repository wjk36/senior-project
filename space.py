import pyjsdl as pygame
import random


class Space:
    def __init__(self):
        self.color_list = [(232, 240, 161), (238, 240, 218), (230, 216, 147)]
        self.star_pos_list = []

        for i in range(0, 2000):

            star_starting_pos_y = random.randint(100, 700)
            star_starting_pos_x = random.randint(0, 2000)
            star_color = self.color_list[random.randint(0, 2)]
            self.star_pos_list.append([star_starting_pos_x, star_starting_pos_y, star_color])

    def update(self, surface, paused, speed, frame):

        print('space')
        print(surface)

        if frame == "Rocket":
            if not paused:
                star_color = self.color_list[random.randint(0, 2)]

                for star_pos in self.star_pos_list:
                    if star_pos[0] < 0:
                        self.star_pos_list.remove(star_pos)

                    elif star_pos[0] < 600 and speed > 0.01:
                        star_pos[2] = (250, 65, 65)
                        star_pos[0] -= 1 * speed
                        pygame.draw.line(surface, star_pos[2], (star_pos[0], star_pos[1]),
                                         (star_pos[0] + 2, star_pos[1]))

                    elif star_pos[0] > 1000 and speed > 0.01:
                        star_pos[2] = (96, 200, 247)
                        star_pos[0] -= 1 * speed
                        pygame.draw.line(surface, star_pos[2], (star_pos[0], star_pos[1]),
                                         (star_pos[0] + 2, star_pos[1]))

                    else:
                        star_pos[0] -= 1 * speed
                        star_pos[2] = star_color
                        pygame.draw.line(surface, star_pos[2], (star_pos[0], star_pos[1]),
                                         (star_pos[0] + 2, star_pos[1]))

        if frame == "Earth":
            for star_pos in self.star_pos_list:
                surface.set_at((star_pos[0], star_pos[1]), star_pos[2])
