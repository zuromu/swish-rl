import pytest

from swish_rl.game import MAX_FRAME_TIME, advance
from swish_rl.physics import Ball
from swish_rl.vec import Vec2

BALL = Ball(position=Vec2(0, 5), velocity=Vec2(0, 0))


def test_short_frame_takes_no_step() -> None:
    moved, leftover = advance(BALL, accumulator=0.0, frame_time=0.005, dt=0.01)
    assert moved == BALL
    assert leftover == pytest.approx(0.005)


def test_frame_runs_whole_steps_and_keeps_leftover() -> None:
    moved, leftover = advance(BALL, accumulator=0.0, frame_time=0.025, dt=0.01)
    assert moved.velocity.y == pytest.approx(-9.81 * 0.02)
    assert leftover == pytest.approx(0.005)


def test_leftover_from_last_frame_is_used() -> None:
    moved, leftover = advance(BALL, accumulator=0.008, frame_time=0.005, dt=0.01)
    assert moved.velocity.y == pytest.approx(-9.81 * 0.01)
    assert leftover == pytest.approx(0.003)


def test_long_frame_is_capped() -> None:
    assert advance(BALL, 0.0, 10.0, dt=0.01) == advance(
        BALL, 0.0, MAX_FRAME_TIME, dt=0.01
    )
