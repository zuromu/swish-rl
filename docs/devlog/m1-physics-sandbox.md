# M1: Physics sandbox

## What I built

When you run `uv run swish-rl`, a window opens and a basketball drops from 5 m,
bounces on the floor, and loses a bit of height every bounce until it settles.
Everything under it is my own small physics engine:

- `Vec2`, a tiny immutable 2D vector, so the physics code reads like the math
  (`position + velocity * dt`)
- a `Ball` and a `step()` function that moves it forward in time under gravity
- `bounce_off_floor()`, which flips the ball's vertical speed and keeps 80% of it
  (that's the restitution, about what a real basketball does)
- a fixed-timestep game loop, so the physics runs at 120 steps per second no
  matter how fast the frames come in

It's all in meters with y pointing up, and only gets turned into pixels at the very
end when drawing. 22 tests check all of it, and CI runs them on every pull request.

## What I learned

- **The order of two lines matters a lot.** If you update position before
  velocity (explicit Euler), the ball gains energy every bounce. In a test run a
  ball dropped from 2 m was bouncing up to 4.87 m after 20 seconds. Updating
  velocity first (semi-implicit Euler) keeps it at about 2 m. I have a test that
  locks this in.
- **Writing tests first.** Red, then green, then clean up. Seeing a test fail
  first is how you know it actually checks something.
- **Fixed timestep is like a time bank.** Every frame deposits its time, the
  physics withdraws it in exact 1/120 s chunks, and whatever's left waits for the
  next frame.
- **Floats are never exact.** One step from rest gave `-0.09810000000000002`
  instead of `-0.0981`, and 0.25 s of 0.01 s steps came out as 24 steps, not 25.
  That's why the tests use `pytest.approx`.

## What was hard

The weirdest one: CI failed on my PR even though every check passed on my
laptop. It turned out ruff had cached an old result for my test file from before
`vec.py` existed, so it never re-checked the imports. The CI machine has no cache,
so it saw the real problem. `ruff clean` fixed it, and it showed me why CI runs on
a fresh machine.

Most of my other bugs were in the tests, not the code. I checked `BALL` (the
starting ball) instead of `moved` (the ball that came back), passed
`screen_height=0` when the expected answer needed 600, and treated
`pygame.event.get()` like one event when it actually returns a list. Next time I'll
work out the expected value by hand before trusting a test.

## What's next

M2: a real court with a backboard and a rim, bouncing off both, and shooting the
ball with click-and-drag. After that the game gets its first release, `v0.1.0`.
