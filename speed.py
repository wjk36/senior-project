

class Speed:
    def __init__(self, curr_speed):
        self.speed = curr_speed

    def increase_speed(self):
        if self.speed >= 0.98:
            return
        else:
            self.speed += 0.01

    def decrease_speed(self):
        if self.speed != 0.00:
            self.speed -= 0.01

    def get_speed(self):
        return self.speed

    def update(self, surface, font, paused):

        print('speed')
        print(surface)

        if not paused:
            speed_string = "Speed: %sc" % round(self.speed, 2)

            counting_text = font.render(str(speed_string), True, (11, 252, 3))

            counting_rect = counting_text.get_rect(midbottom=(1500, 800))

            surface.blit(counting_text, counting_rect)