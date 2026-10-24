"""The game window and main loop."""

import pygame

from swish_rl.game import advance
from swish_rl.physics import Ball
from swish_rl.render import draw
from swish_rl.vec import Vec2

WINDOW_SIZE = (800, 600)  # pixels: 8 m × 6 m of world
FPS = 60


def run(max_frames: int | None = None) -> None:
    """Open the game window and run the loop until it is closed."""
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Swish RL")
    clock = pygame.time.Clock()
    ball = Ball(position=Vec2(4.0, 5.0), velocity=Vec2(0, 0))
    accumulator = 0.0
    frames = 0
    running = True
    while running and (max_frames is None or frames < max_frames):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        frame_time = clock.tick(FPS) / 1000
        ball, accumulator = advance(ball, accumulator, frame_time)
        draw(screen, ball)
        pygame.display.flip()
        frames += 1
    pygame.quit()
