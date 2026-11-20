import pygame
from . import var


def init(
    width: int,
    height: int,
    bg: str | tuple[int, int, int] = "white",
    fps: int = 60,
):
    pygame.init()

    var.init = True
    var.width = width
    var.height = height
    var.running = True
    var.bg = bg
    var.fps = fps
    var.screen = pygame.display.set_mode((width, height))


def bind(functype: str, func: object | None):
    if functype in var.functions and (
        isinstance(func, type(bind)) or isinstance(func, type(None))
    ):
        var.functions[functype] = func  # type: ignore


def unbind(functype: str):
    bind(functype, None)


def run():
    while var.running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                var.running = False

        # fill the screen with a color to wipe away anything from last frame
        var.screen.fill(var.bg)

        for shapes in var.draw:
            shapes._draw()  # type: ignore

        if var.functions["main"]:
            var.functions["main"]()

        # flip() the display to put your work on screen
        var.display.flip()

        var.clock.tick(var.fps)  # limits FPS to 60

    pygame.quit()
