"""Drawing helpers that turn the simulation into pixels."""

from swish_rl.vec import Vec2

PIXELS_PER_METER = 100.0


def world_to_screen(
    point: Vec2, screen_height: int, pixels_per_meter: float = PIXELS_PER_METER
) -> tuple[int, int]:
    """Return the pixel position of a world point (meters, y up)."""
    pixel_x = round(point.x * pixels_per_meter)
    pixel_y = round(screen_height - point.y * pixels_per_meter)
    return (pixel_x, pixel_y)
