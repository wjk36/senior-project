import pyjsdl as pygame
from frame import Frame
from speed import Speed

surface = None


def run_sim():

    font = pygame.font.SysFont(None, 32)

    frame = "Earth"
    paused = False
    running = True

    print(surface)
    print(dir(surface))

    # update frame of reference if need be
    frame_of_reference = Frame(surface, font, frame, paused)

    # speedometer
    speed = 0.01
    speedometer = Speed(speed)

    speed_list = []

    while running:

        clock = pygame.time.Clock()

        # check if user has clicked on a specific key
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_p:
                    paused = not paused

                if event.key == pygame.K_UP:
                    speedometer.increase_speed()

                if event.key == pygame.K_DOWN:
                    speedometer.decrease_speed()

                if event.key == pygame.K_r:
                    run()
                    return

        if not paused:

            surface.fill((0, 0, 0))

            frame_string = " " + frame + " Frame"
            frame_font = pygame.font.SysFont(None, 60)

            frame_text = frame_font.render(str(frame_string), True, (11, 252, 3))
            frame_rect = frame_text.get_rect(topleft=(0, 0))
            surface.blit(frame_text, frame_rect)

            # update and get speed
            speedometer.update(surface, font, paused)
            speed = speedometer.get_speed()
            speed_list.append(speed)

            paused = frame_of_reference.update(surface, frame, paused, speed, speed_list)

            # update display
            pygame.display.update()

            clock.tick(25)

    # Done! Time to quit.
    pygame.quit()


def run():      #pyjsdl: callback function
    run_sim()


def setup(x=1600, y=800):
    global surface
    pygame.init()
    pygame.display.set_caption('Special Relativity')
    surface = pygame.display.set_mode((x, y))
    background = pygame.Surface((x,y))
    background.fill((50, 50, 50))
    for line in range(0, 300, 25):
        pygame.draw.line(background, (43, 50, 58), (0, line), (400, line), 1)
    for line in range(0, 400, 25):
        pygame.draw.line(background, (43, 50, 58), (line, 0), (line, 300), 1)


def main():
    setup()
    images = ['./data/airship.png', './data/destination.png', './data/earth.png']
    pygame.display.setup(run, images)


if __name__ == '__main__':
    main()
