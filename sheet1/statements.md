# Functions, Cycles and Turtle

| Exercise | Statement                                                                                                                                                                                                                                                                                                   |             Solution              |
|:--------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------:|
|    1     | Normally, interest is calculated based on an integer number of periods. However, in some situations, it is useful to calculate interest as a continuous function of time. Write a function investment_valor(P0, r, t) that returns the investment value, past a t time in years, with a interest rate of r. | [Show](./solutions/exercise01.py) |
|    2     | Implement a function distance_between_two_points(x1, y1, x2, y2) that calculates the distance between two points.                                                                                                                                                                                           | [Show](./solutions/exercise02.py) |
|    3     | Write a function radians(grads, min, sec) that, given the value of an angle in degrees, minutes, and seconds, converts it to radians.                                                                                                                                                                       | [Show](./solutions/exercise03.py) |
|    4     | Write a function time_in_seconds(hour, min, sec) that, given a duration in hours, minutes, and seconds, calculates and returns that same duration in seconds.                                                                                                                                               | [Show](./solutions/exercise04.py) |
|    5     | Write a program that reads an integer amount in euros and shows how to pay that amount using 20€, 10€, 5€ notes and 1€ coins.                                                                                                                                                                               | [Show](./solutions/exercise05.py) |

| (6) Initial Statement |  Consider a program that starts with the following assignment: xs = [5, 0, 42, 10, 24, 30, 81]  |
|:---------------------:|:-----------------------------------------------------------------------------------------------:|

| Item | Statement                                                                                                                                                                                 |              Solution              |
|:----:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------:|
|  a   | Write a for loop that prints each of the values in the list xs on a separate line.<br/>                                                                                                   | [Show](./solutions/exercise06a.py) |
|  b   | Write another for loop that, on each line, prints the number, its square, and its square root.                                                                                            | [Show](./solutions/exercise06b.py) |
|  c   | Write a loop that adds up all the numbers in xs using an auxiliary variable total, and prints on a separate line each of the numbers from the list and the partial sum up to that number. | [Show](./solutions/exercise06c.py) |

| Exercise | Statement                                                                                                                                                                                                                                                                                                                       |             Solution              |
|:--------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------:|
|    7     | Write a function square_table(n) that, for the first n positive integers, prints on each line the number and its square, separated by a space. You can assume that n > 0                                                                                                                                                        | [Show](./solutions/exercise07.py) |
|    8     | Write a program that asks for the initial capital and interest rate, then prints a table showing the final capital after 0 to 24 months, using the formula CF = CI × (1 + r/12)^n.                                                                                                                                              | [Show](./solutions/exercise08.py) |
|    9     | Using the turtle module, write a function regular_polygon(n, side) that draws a regular polygon with n sides, each of length side, and does not return any value.                                                                                                                                                               | [Show](./solutions/exercise09.py) |
|    10    | Using the turtle module, write a function home(side) that has no return value and draws a house (an equilateral triangle on top of a square, both with the same side length).                                                                                                                                                   | [Show](./solutions/exercise10.py) |
|    11    | Using the turtle module, write a function frizz(n, side) that has no return value and draws a frizz in the shape of a wall with n battlements where the width of each segment is side.                                                                                                                                          | [Show](./solutions/exercise11.py) |
|    12    | The current price of gasoline is 1.72 euros per liter. Implement the function value(v) that, given the list v of liters refueled on a trip, returns the total amount spent.                                                                                                                                                     | [Show](./solutions/exercise12.py) |
|    13    | The area A of a triangle whose sides measure a, b, and c can be calculated using the formula of Heron. A = ( s(s − a)(s − b)(s − c) ) ** 0.5. Where, s = (a + b + c)/2 is the semi-perimeter of the triangle. Implement a function triangle_area_calculator(a, b, c) that calculates the area of a triangle using this formula. | [Show](./solutions/exercise13.py) |
|    14    | In a triangle, each side has a length less than the sum of the lengths of the other two sides and greater than their absolute difference. Write a function triangle(a, b, c) that checks this condition for the sides a, b, and c; the result should be True or False.                                                          | [Show](./solutions/exercise14.py) |

| (15) Initial Statement | Write a function classification(p) that, given the score p obtained in an exam (from 0 to 100), returns a classification message according to the following table: | [Show](./solutions/exercise15.py)  |
|:----------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------:|



|    Grade    |     Message      |
|:-----------:|:----------------:|
| < 0 or > 20 |    'Invalid'     |
|   0 - 4.9   |  'Insufficient'  |
|   5 - 9.9   | 'Not Sufficient' |
|  10 - 11.9  |   'Sufficient'   |
|  12 - 14.9  |      'Good'      |
|  15 - 18.9  |   'Very Good'    |
|  19 -  20   |   'Excellent'    |
