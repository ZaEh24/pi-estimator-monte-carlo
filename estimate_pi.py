import math
import random

total_points = 10000

points_inside_circle = sum(
    1 for _ in range(total_points) if random.random() ** 2 + random.random() ** 2 < 1
)

calculated_pi = 4 * (points_inside_circle / total_points)
print(f"Calculated value of π: {calculated_pi}")
print(f"Value of π from math library: {math.pi}")
print(f"Difference: {calculated_pi - math.pi}")
