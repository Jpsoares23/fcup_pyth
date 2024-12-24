def triangle(a: float | int, b: float | int, c: float | int) -> bool:
    if a < b + c and b < a + c and c < a + b:
        if a > abs(b - c) and b > abs(a - c) and c > abs(a - b):
            return True
    return False
