import pytest

from swish_rl.physics import Ball, step
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
