import turtle


def frizz(n: int, side: int) -> None:
    number_of_crenel_drawn = 0

    while number_of_crenel_drawn < n:
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.right(90)
        turtle.forward(side)
        turtle.right(90)
        turtle.forward(side)
        turtle.left(90)

        number_of_crenel_drawn += 1


frizz(3, 50)  # example

turtle.done()
