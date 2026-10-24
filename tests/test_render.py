from swish_rl.render import world_to_screen
from swish_rl.vec import Vec2


def test_world_origin_is_bottom_left_of_screen() -> None:
    assert world_to_screen(Vec2(0, 0), screen_height=600) == (0, 600)


def test_one_meter_up_and_right() -> None:
    assert world_to_screen(Vec2(1, 1), screen_height=600) == (100, 500)


def test_custom_scale() -> None:
    assert world_to_screen(Vec2(2, 1), screen_height=600, pixels_per_meter=50) == (
        100,
        550,
    )
