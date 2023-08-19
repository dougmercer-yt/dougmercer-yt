import math
import time

import taichi as ti

ti.init(arch=ti.cpu)

num_points = 100_000_000
points_inside_circle = ti.field(dtype=int, shape=())


# I don't remember why I did this one...
@ti.kernel
def monte_carlo_approximation() -> float:
    points_inside_circle[None] = 0

    for _ in ti.grouped(ti.ndrange(num_points)):
        x = ti.random()
        y = ti.random()

        distance = x * x + y * y

        if distance <= 1:
            ti.atomic_add(
                points_inside_circle[None], 1
            )  # Use atomic operation to avoid race conditions

    return 4 * points_inside_circle[None] / num_points


# This one seems easier, faster, and better
@ti.kernel
def monte_carlo_pi(n: int) -> float:
    total = 0
    for _ in range(n):
        x = ti.random()
        y = ti.random()
        if x * x + y * y < 1:
            total += 1
    return 4 * total / n


t = time.perf_counter()
approximation = monte_carlo_approximation()
print(f"\nRun Time: {time.perf_counter() - t} for {num_points}.")
print(f"Approximation of Pi: {approximation}")
print(f"Error: {abs(math.pi - approximation)}\n")

t = time.perf_counter()
approximation = monte_carlo_pi(num_points)
print(f"(Simple One) Run Time: {time.perf_counter() - t} for {num_points}.")
print(f"(Simple One) Approximation of Pi: {approximation}")
print(f"(Simple One) Error: {abs(math.pi - approximation)}")
