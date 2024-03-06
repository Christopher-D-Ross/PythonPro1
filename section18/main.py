import random
from turtle import Turtle, Screen

# from turtle import *
# Below, t is an alias name
# import turtle as t

somba = Turtle()
somba.shape("turtle")
somba.color("darkred")
screen = Screen()


# somba_the_turtle.shapesize(2, 2, 6)
def draw_a_square():
    somba.forward(50)
    somba.left(90)
    somba.forward(100)
    somba.left(90)
    somba.forward(100)
    somba.left(90)
    somba.forward(100)
    somba.left(90)
    somba.forward(50)


def draw_a_dashed_line():
    for number in range(0, 25):
        somba.pendown()
        somba.forward(10)
        somba.penup()
        somba.forward(10)


def get_random_color():
    screen.colormode(255)
    random_color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    return random_color


# 360 divided by the number of sides of a shape will give you the angles in each shape.
def draw_shapes(num_of_sides_end):
    num_of_sides = 3
    while num_of_sides < num_of_sides_end:
        screen.colormode(255)
        random_color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        somba.pencolor(random_color)
        for num in range(0, num_of_sides):
            somba.left(360 / num_of_sides)
            somba.forward(100)
        num_of_sides += 1


# draw_shapes(11)


def forward():
    somba.forward(25)


def backward():
    somba.backward(25)


def left():
    somba.left(90)


def right():
    somba.right(90)


v_directions = [forward, backward]
h_directions = [left, right]


def random_walk():
    somba.pensize(10)
    somba.speed("fast")
    for n in range(0, 200):
        screen.colormode(255)
        random_color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        somba.pencolor(random_color)
        v = v_directions[random.randint(0, 1)]
        h = h_directions[random.randint(0, 1)]
        v()
        h()


# random_walk()


def spirograph():
    somba.speed("fastest")
    for circles in range(0, 180):
        somba.pencolor(get_random_color())
        somba.circle(200)
        somba.left(2)


spirograph()

# screen.bgcolor("darkslategrey")


screen.exitonclick()
