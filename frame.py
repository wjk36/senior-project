from rocket import Rocket
from planet import Planet
from space import Space
from timer import Timer
from end import End


class Frame:
    def __init__(self, surface, font, frame, paused):
        if not paused:
            speed = 0.01

            print('frame')
            print(surface)

            self.frame_string = " " + frame + " Frame"

            self.frame_text = font.render(str(self.frame_string), True, (11, 252, 3))
            self.frame_rect = self.frame_text.get_rect(topleft=(0, 0))

            surface.blit(self.frame_text, self.frame_rect)

            self.rocket_in_rocket_frame = Rocket(surface, 600, 350)
            self.earth_in_rocket_frame = Planet(surface, 300, 200, "Rocket", "earth.png")
            self.planet_in_rocket_frame = Planet(surface, 1200, 200, "Rocket", "destination.png")
            self.space_in_rocket_frame = Space()
            self.timer_in_rocket_frame = Timer("Rocket", speed)

            self.rocket_in_earth_frame = Rocket(surface, 400, 350)
            self.earth_in_earth_frame = Planet(surface, 100, 200, "Earth", "earth.png")
            self.space_in_earth_frame = Space()
            self.planet_in_earth_frame = Planet(surface, 1000, 200, "Earth", "destination.png")
            self.timer_in_earth_frame = Timer("Earth", speed)

    def update(self, surface, frame, paused, speed, speed_list):

        self.timer_in_earth_frame.update(surface, paused, speed, frame)
        self.timer_in_rocket_frame.update(surface, paused, speed, frame)

        if self.rocket_in_earth_frame.getPosition() >= self.planet_in_rocket_frame.getPosition():
            rocket_time = self.timer_in_rocket_frame.get_time()
            earth_time = self.timer_in_earth_frame.get_time()
            avg_speed = sum(speed_list) / len(speed_list)
            rocket_distance = (rocket_time / 1000) * avg_speed * 3e8
            earth_distance = (earth_time / 1000) * avg_speed * 3e8
            End(surface, rocket_time, earth_time, rocket_distance, earth_distance)
            return True

        else:
            if frame == "Rocket":
                self.rocket_in_rocket_frame.update(surface, paused, frame, speed)
                self.space_in_rocket_frame.update(surface, paused, speed, frame)
                self.earth_in_rocket_frame.update(surface, paused, frame, speed)
                self.planet_in_rocket_frame.update(surface, paused, frame, speed)

            elif frame == "Earth":
                self.earth_in_earth_frame.update(surface, paused, frame, speed)
                self.space_in_earth_frame.update(surface, paused, speed, frame)
                self.rocket_in_earth_frame.update(surface, paused, frame, speed)
                self.planet_in_earth_frame.update(surface, paused, frame, speed)
            return False
