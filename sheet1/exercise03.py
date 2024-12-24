import math


def radians(degrees: float, min: int, sec: int) -> float:

    minutes_to_degrees = min / 60
    seconds_to_degrees = sec / 3600

    total_degrees = degrees + minutes_to_degrees + seconds_to_degrees

    return math.radians(total_degrees)
