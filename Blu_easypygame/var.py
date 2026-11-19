import pygame

varInt = int | None
varBool = bool | None


bg: str | tuple[int, int, int] = "white"

init: bool = False

running: varBool

width: varInt = 0
height: varInt = 0

time = pygame.time
clock = time.Clock()
display = pygame.display

screen: pygame.Surface

fps: int = 60
