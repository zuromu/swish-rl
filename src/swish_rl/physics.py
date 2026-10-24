"""Ball physics: state and time-stepping under gravity."""

from dataclasses import dataclass

from swish_rl.vec import Vec2

GRAVITY = Vec2(0.0, -9.81)  # m/s², points down (y is up)
FLOOR_Y = 0.0  # m
RESTITUTION = 0.8  # fraction of vertical speed kept after a bounce


@dataclass(frozen=True, slots=True)
class Ball:
    """The state of a ball at one moment in time."""

    position: Vec2  # m, center of the ball
    velocity: Vec2  # m/s
    radius: float = 0.12  # m


def step(ball: Ball, dt: float, gravity: Vec2 = GRAVITY) -> Ball:
    """Return the ball dt seconds later, using semi-implicit Euler."""
    # Semi-implicit Euler: update velocity first, then move using the NEW velocity.
    # Doing it the other way round adds energy, so bounces would grow higher.
    new_velocity = ball.velocity + gravity * dt
    new_position = ball.position + new_velocity * dt
    return Ball(position=new_position, velocity=new_velocity, radius=ball.radius)


def bounce_off_floor(
    ball: Ball, floor_y: float = FLOOR_Y, restitution: float = RESTITUTION
) -> Ball:
    """Return the ball bounced off the floor, or unchanged if it isn't hitting it."""
    if ((ball.position.y - ball.radius) >= floor_y) or (ball.velocity.y >= 0):
        return ball
    new_position = Vec2(ball.position.x, floor_y + ball.radius)
    new_velocity = Vec2(ball.velocity.x, -(ball.velocity.y) * restitution)
    return Ball(new_position, new_velocity, ball.radius)
