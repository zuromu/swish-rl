import pytest

from swish_rl.play import run


def test_game_loop_runs_headless(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SDL_VIDEODRIVER", "dummy")
    monkeypatch.setenv("SDL_AUDIODRIVER", "dummy")
    run(max_frames=5)
