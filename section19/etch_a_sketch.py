from turtle import Turtle, Screen

somba = Turtle()
screen = Screen()
somba.shape("turtle")
somba.color("darkred")
somba.speed("fast")


def forward():
    somba.forward(10)


def backward():
    somba.backward(10)


def left():
    somba.left(10)


def right():
    somba.right(10)


def clear():
    screen.resetscreen()
    somba.color("darkred")


screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(clear, "space")
screen.listen()

screen.exitonclick()
