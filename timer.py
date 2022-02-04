import math
import pyjsdl as pygame


class Timer:
    def __init__(self, frame, speed):
        self.start_time = pygame.time.get_ticks()
        self.frame = frame
        self.speed = speed
        self.font = pygame.font.SysFont(None, 32)

    def update(self, surface, paused, speed, frame):

        if not paused:

            # update speed if need be
            self.speed = speed

            # update total time from start time
            counting_time = pygame.time.get_ticks() - self.start_time

            # check if current frame is now the prime frame

            if self.frame == "Earth":
                counting_time /= math.sqrt(1 - speed**2)

            if self.frame == frame:
                self.font = pygame.font.SysFont(None, 60)
            # change milliseconds into minutes, seconds, milliseconds
            counting_minutes = str(round(counting_time // 60000)).zfill(2)
            counting_seconds = str(round(counting_time % 60000 // 1000)).zfill(2)
            counting_millisecond = str(round(counting_time % 1000)).zfill(3)

            counting_string = " " + self.frame + ": %s:%s:%s " % (counting_minutes, counting_seconds, counting_millisecond)

            counting_text = self.font.render(str(counting_string), True, (11, 252, 3))
            if self.frame != frame:
                counting_rect = counting_text.get_rect(bottomleft=(5, 790))
            elif self.frame == frame:
                counting_rect = counting_text.get_rect(bottomleft=(0, 760))
            else:
                counting_rect = counting_text.get_rect(center=(500, 500))

            surface.blit(counting_text, counting_rect)

    def get_time(self):
        counting_time = pygame.time.get_ticks() - self.start_time
        if self.frame == "Earth":
            return counting_time / math.sqrt(1 - self.speed**2)
        else:
            return counting_time
