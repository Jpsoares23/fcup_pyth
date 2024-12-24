import turtle


def house(side: int) -> None:
    for rotate in range(0, 3):
        turtle.forward(side)
        turtle.left(120)
    for rotate in range(0, 4):
        turtle.forward(side)
        turtle.right(90)


house(100)  # example

turtle.done()
