import pygame

varInt = int | None
varBool = bool | None
color = str | tuple[int, int, int]
num = int | float

bg: color

init: bool = False

running: varBool

width: varInt
height: varInt

functions = {
    "main": None,
}

time = pygame.time
clock = time.Clock()
display = pygame.display

screen: pygame.Surface

fps: int

draw: list[object] = []
