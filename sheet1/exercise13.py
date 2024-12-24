def triangle_area_calculator(a: float | int, b: float | int, c: float | int) -> float:
    s = (a + b + c) / 2

    triangle_area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    return triangle_area
