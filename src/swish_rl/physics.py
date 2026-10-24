"""Ball physics: state and time-stepping under gravity."""

from dataclasses import dataclass

from swish_rl.vec import Vec2

GRAVITY = Vec2(0.0, -9.81)  # m/s², points down (y is up)


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
