"""Drawing helpers that turn the simulation into pixels."""

import pygame

from swish_rl.physics import Ball
from swish_rl.vec import Vec2

PIXELS_PER_METER = 100.0
BACKGROUND_COLOR = (20, 20, 30)
BALL_COLOR = (255, 140, 0)  # basketball orange


def world_to_screen(
    point: Vec2, screen_height: int, pixels_per_meter: float = PIXELS_PER_METER
) -> tuple[int, int]:
    """Return the pixel position of a world point (meters, y up)."""
    pixel_x = round(point.x * pixels_per_meter)
    pixel_y = round(screen_height - point.y * pixels_per_meter)
    return (pixel_x, pixel_y)


def draw(screen: pygame.Surface, ball: Ball) -> None:
    """Draw the background and the ball onto the screen."""
    screen.fill(BACKGROUND_COLOR)
    center = world_to_screen(ball.position, screen.get_height())
    radius = round(ball.radius * PIXELS_PER_METER)
    pygame.draw.circle(screen, BALL_COLOR, center, radius)
