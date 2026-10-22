"""2D vector math for the physics simulation."""

from dataclasses import dataclass
from math import hypot


@dataclass(frozen=True, slots=True)
class Vec2:
    """An immutable 2D vector for positions, velocities and forces."""

    x: float
    y: float

    def __add__(self, other: "Vec2") -> "Vec2":
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vec2") -> "Vec2":
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vec2":
        return Vec2(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> "Vec2":
        return self * scalar

    def length(self) -> float:
        """Return the vector's length, sqrt(x**2 + y**2)."""
        return hypot(self.x, self.y)
