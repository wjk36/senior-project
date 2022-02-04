import pyjsdl as pygame


def construct_time_string(counting_time):
    counting_minutes = str(round(counting_time // 60000)).zfill(2)
    counting_seconds = str(round(counting_time % 60000 // 1000)).zfill(2)
    counting_millisecond = str(round(counting_time % 1000)).zfill(3)
    counting_string = "%s:%s:%s " % (counting_minutes, counting_seconds, counting_millisecond)
    return counting_string


def construct_distance_string(distance):
    distance_string = "{:,}".format(distance)
    return distance_string


class End:
    def __init__(self, surface, rocket_time, earth_time, rocket_distance, earth_distance):
        self.font = pygame.font.SysFont(None, 32)

        surface.fill((0, 0, 0))

        rocket_string_time = "Time: %s" % construct_time_string(rocket_time)
        rocket_string_distance = "Distance: %s km" % construct_distance_string(rocket_distance)
        earth_string_time = "Time: %s" % construct_time_string(earth_time)
        earth_string_distance = "Distance: %s km" % construct_distance_string(earth_distance)

        label = [self.font.render(" JOURNEY END", True, (11, 252, 3)),
                 self.font.render("--------------------------", True, (11, 252, 3)),
                 self.font.render("Rocket Frame", True, (11, 252, 3)),
                 self.font.render(rocket_string_time, True, (11, 252, 3)),
                 self.font.render(rocket_string_distance, True, (11, 252, 3)),
                 self.font.render("--------------------------", True, (11, 252, 3)),
                 self.font.render("Earth Frame", True, (11, 252, 3)),
                 self.font.render(earth_string_time, True, (11, 252, 3)),
                 self.font.render(earth_string_distance, True, (11, 252, 3))]

        for line in range(len(label)):
            surface.blit(label[line], (500, 200 + (line * 25) + (15 * line)))
