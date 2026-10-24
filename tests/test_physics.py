import pytest

from swish_rl.physics import Ball, bounce_off_floor, step
from swish_rl.vec import Vec2


def test_moves_in_straight_line_without_gravity() -> None:
    ball = Ball(position=Vec2(0, 0), velocity=Vec2(2, 0))
    moved = step(ball, dt=0.5, gravity=Vec2(0, 0))
    assert moved.position == Vec2(1, 0)


def test_one_step_from_rest_uses_semi_implicit_euler() -> None:
    ball = Ball(position=Vec2(0, 0), velocity=Vec2(0, 0))
    moved = step(ball, dt=0.1)
    assert moved.position.y == pytest.approx(-0.0981)
    assert moved.velocity.y == pytest.approx(-0.981)


def test_free_fall_matches_formula() -> None:
    ball = Ball(position=Vec2(0, 0), velocity=Vec2(0, 0))
    for _ in range(600):
        ball = step(ball, dt=1 / 600)
    assert ball.position.y == pytest.approx(-4.905, abs=0.01)


def test_step_does_not_change_input() -> None:
    ball = Ball(position=Vec2(0, 0), velocity=Vec2(2, 0))
    step(ball, dt=0.5)
    assert ball == Ball(position=Vec2(0, 0), velocity=Vec2(2, 0))


def test_ball_above_floor_is_unchanged() -> None:
    ball = Ball(position=Vec2(0, 1), velocity=Vec2(0, -2))
    assert bounce_off_floor(ball) == ball


def test_ball_hitting_floor_bounces() -> None:
    ball = Ball(position=Vec2(0, 0.1), velocity=Vec2(3, -5))
    bounced = bounce_off_floor(ball)
    assert bounced.position.y == pytest.approx(0.12)
    assert bounced.velocity.y == pytest.approx(4.0)
    assert bounced.velocity.x == 3


def test_ball_moving_up_is_not_bounced() -> None:
    ball = Ball(position=Vec2(0, 0.1), velocity=Vec2(0, 1))
    assert bounce_off_floor(ball) == Ball(position=Vec2(0, 0.1), velocity=Vec2(0, 1))


def test_first_bounce_height_matches_restitution() -> None:
    ball = Ball(position=Vec2(0, 2.12), velocity=Vec2(0, 0))
    highest = 0.0
    for _ in range(900):
        ball = bounce_off_floor(step(ball, dt=1 / 600))
        if ball.velocity.y >= 0:
            highest = max(highest, (ball.position.y - ball.radius))
    assert highest == pytest.approx((0.8**2 * 2.0), abs=0.02)
