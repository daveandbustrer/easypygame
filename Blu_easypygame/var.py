import pygame

varInt = int | None
varBool = bool | None
color = str | tuple[int, int, int]
num = int | float

bg: color = "white"

init: bool = False

running: varBool

width: varInt = 0
height: varInt = 0

functions = {
    "main": None,
}

time = pygame.time
clock = time.Clock()
display = pygame.display

screen: pygame.Surface

fps: int = 60
