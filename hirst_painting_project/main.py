import colorgram
from turtle import Turtle, Screen
import random

somba = Turtle()
somba.hideturtle()
somba.color("darkred")
screen = Screen()

colors = colorgram.extract("hirst-for-python.jpeg", 16)

# list_of_colors = []
#
# for c in colors:
#     color_tuple = (c.rgb.r, c.rgb.g, c.rgb.b)
#     list_of_colors.append(color_tuple)
#
# print(list_of_colors)

saved_colors = [(235, 234, 232), (235, 232, 234), (184, 148, 95), (151, 104, 46), (229, 230, 232), (179, 150, 22),
                (83, 34, 27), (12, 56, 72), (32, 100, 120), (101, 41, 47), (57, 136, 121), (228, 233, 229),
                (107, 40, 30), (23, 65, 50), (40, 80, 7), (109, 8, 10)]


# 10 x 10 rows
# dot size 20
# space between = 50


def hirst():
    somba.speed("fast")
    screen.colormode(255)
    count = 1
    somba.penup()
    somba.setheading(225)
    somba.forward(300)
    somba.setheading(0)
    tp = somba.pos()
    multi = 1
    for num in range(0, 90):
        somba.dot(20, random.choice(saved_colors))
        somba.penup()
        somba.forward(50)
        somba.dot(20, random.choice(saved_colors))
        count += 1
        if count == 10:
            somba.teleport(tp[0], tp[1] + 50 * multi)
            count = 1
            multi += 1


hirst()


screen.exitonclick()
