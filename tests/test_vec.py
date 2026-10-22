from dataclasses import FrozenInstanceError

import pytest
from swish_rl.vec import Vec2


def test_add() -> None:
    assert Vec2(1, 2) + Vec2(3, 4) == Vec2(4, 6)


def test_sub() -> None:
    assert Vec2(4, 6) - Vec2(3, 4) == Vec2(1, 2)


def test_mul_by_scalar() -> None:
    assert Vec2(1, 2) * 3 == Vec2(3, 6)


def test_mul_scalar_first() -> None:
    assert 3 * Vec2(1, 2) == Vec2(3, 6)


def test_length() -> None:
    assert Vec2(3, 4).length() == pytest.approx(5)


def test_is_immutable() -> None:
    v = Vec2(2, 2)
    with pytest.raises(FrozenInstanceError):
        v.x = 5.0  # pyright: ignore[reportAttributeAccessIssue]
