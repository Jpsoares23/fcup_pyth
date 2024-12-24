from math import e


def investment_value(p0: float, r: float, t: float) -> float:
    return p0 * (e ** (r * t))
