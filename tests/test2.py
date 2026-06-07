import math
import random
import easypygame as epy

# Initialize a dark canvas with a smooth 60 FPS loop.
epy.init(width=900, height=650, bg=(12, 14, 26), frame=60)

# Background accent shapes.
frame_rect = epy.graphics.rect(450, 330, 820, 540, color=(24, 28, 56))
left_panel = epy.graphics.rect(150, 320, 260, 520, color=(18, 22, 42))
top_banner = epy.graphics.rect(450, 70, 760, 100, color=(10, 12, 22))

# Animated shapes.
rotating_star = epy.graphics.polygon(
    [
        (450, 190),
        (480, 290),
        (580, 290),
        (500, 350),
        (530, 450),
        (450, 390),
        (370, 450),
        (400, 350),
        (320, 290),
        (420, 290),
    ],
    color=(255, 195, 0),
    width=0,
)
rotating_star.angle = 0

bouncy_square = epy.graphics.square(380, 520, 70, color=(97, 212, 195))
small_circle = epy.graphics.circle(680, 500, 42, color=(81, 144, 255))
line_path = epy.graphics.line([(80, 80), (180, 220), (260, 140), (370, 250)], width=6, color=(132, 94, 194))

click_circles: list = []
background_toggle = False
time_accumulator = 0.0


def create_click_circle(x: int, y: int) -> None:
    circle = epy.graphics.circle(x, y, random.randint(12, 26), color=(255, 255, 255))
    circle.speed_x = random.uniform(-120.0, 120.0)
    circle.speed_y = random.uniform(-120.0, 120.0)
    click_circles.append(circle)


# Start with a few particles for polish.
for _ in range(8):
    create_click_circle(random.randint(240, 660), random.randint(160, 540))


def main(dt: float) -> None:
    global background_toggle

    # Animate the rotating polygon star.
    rotating_star.angle += 35 * dt

    # Bounce the square vertically.
    global time_accumulator
    time_accumulator += dt
    bounce_direction = 1 if math.sin(time_accumulator * 4) >= 0 else -1
    bouncy_square.y += 180 * dt * bounce_direction
    if bouncy_square.y < 470:
        bouncy_square.y = 470
    elif bouncy_square.y > 560:
        bouncy_square.y = 560

    # Move the small circle horizontally.
    small_circle.x += 120 * dt
    if small_circle.x > epy.getWidth() + 40:
        small_circle.x = -40

    # Update click circles and remove old ones when outside screen.
    for circle in click_circles[:]:
        circle.x += getattr(circle, "speed_x", 0) * dt
        circle.y += getattr(circle, "speed_y", 0) * dt
        circle.color = (255, 255, 255) if random.random() < 0.02 else circle.color
        if circle.x < -40 or circle.x > epy.getWidth() + 40 or circle.y < -40 or circle.y > epy.getHeight() + 40:
            click_circles.remove(circle)

    # Pulse line color.
    if random.random() < 0.02:
        line_path.color = (random.randint(120, 255), random.randint(80, 220), random.randint(160, 255))

    # Toggle background color softly.
    if background_toggle:
        epy.background = (8, 12, 36)
    else:
        epy.background = (12, 14, 26)


def left_click(event) -> None:
    x, y = event
    create_click_circle(x, y)


def right_click() -> None:
    global background_toggle
    background_toggle = not background_toggle


epy.bind("main", main)
epy.bind("leftMouseDown", left_click)
epy.bind("rightMouseDown", right_click)

epy.run()
