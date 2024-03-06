import random
from turtle import Turtle, Screen

somba = Turtle()
somba.color("red")
somba.penup()
somba.shape("turtle")
greysar = Turtle()
greysar.color("grey")
greysar.penup()
greysar.shape("turtle")
icen = Turtle()
icen.color("blue")
icen.penup()
icen.shape("turtle")
kalen = Turtle()
kalen.color("green")
kalen.penup()
kalen.shape("turtle")
nova = Turtle()
nova.color("gold")
nova.penup()
nova.shape("turtle")
screen = Screen()
screen.setup(500, 400)
answer = screen.textinput("Make Your Bet", "Which turtle will win the race? Enter a color:")
somba.goto(-240, 0)
greysar.goto(-240, -40)
icen.goto(-240, -80)
kalen.goto(-240, 40)
nova.goto(-240, 80)

finished = False
winner = ""
while not finished:
    somba.forward(random.randint(1, 10))
    greysar.forward(random.randint(1, 10))
    icen.forward(random.randint(1, 10))
    kalen.forward(random.randint(1, 10))
    nova.forward(random.randint(1, 10))
    if somba.xcor() > 249:
        finished = True
        winner = "Red"
    elif greysar.xcor() > 249:
        finished = True
        winner = "Grey"
    elif icen.xcor() > 249:
        finished = True
        winner = "Blue"
    elif kalen.xcor() > 249:
        finished = True
        winner = "Green"
    elif nova.xcor() > 249:
        finished = True
        winner = "Gold"

if answer.lower() == winner.lower():
    print("You win! You picked the winning turtle.")
else:
    print(f"You lose. The {winner} turtle won.")

screen.exitonclick()
