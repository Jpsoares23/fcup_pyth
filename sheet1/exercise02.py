import math


def distance_between_two_points(x1: int | float, y1: int | float, x2: int | float, y2: int | float) -> float:
    dx = x1 - x2
    dy = y1 - y2
    return math.sqrt(dx ** 2 + dy ** 2)
