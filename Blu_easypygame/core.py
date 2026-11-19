import pygame
from . import var


def init(
    width: int, height: int, bg: str | tuple[int, int, int] = "white", fps: int = 60
):
    pygame.init()
    var.init = True

    var.screen = pygame.display.set_mode((width, height))
    var.width = width
    var.height = height
    var.running = True
    var.bg = bg
    var.clock
    var.fps = 60
    x = True
    while x:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                x = False

        # fill the screen with a color to wipe away anything from last frame
        var.screen.fill(var.bg)

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        var.display.flip()

        var.clock.tick(var.fps)  # limits FPS to 60

    pygame.quit()
