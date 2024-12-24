import turtle


def regular_polygon(n: int, side: int) -> None:
    for rotate in range(0, n):
        turtle.forward(side)
        turtle.left(360/n)


regular_polygon(3, 100)  # example

turtle.done()
