"""Fixed-timestep game loop logic."""

from swish_rl.physics import Ball, bounce_off_floor, step

PHYSICS_DT = 1 / 120  # s, length of one physics step
MAX_FRAME_TIME = 0.25  # s, the longest frame we simulate (avoids the spiral of death)


def advance(
    ball: Ball, accumulator: float, frame_time: float, dt: float = PHYSICS_DT
) -> tuple[Ball, float]:
    """Return the ball after this frame's physics steps, and the leftover time."""
    accumulator += min(MAX_FRAME_TIME, frame_time)
    while accumulator >= dt:
        ball = bounce_off_floor(step(ball, dt))
        accumulator = accumulator - dt
    return ball, accumulator
