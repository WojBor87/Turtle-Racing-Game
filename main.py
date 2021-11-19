import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

x = -230
y = -100

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=x, y=y)
    y += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for cur_turtle in all_turtles:
        if cur_turtle.xcor() > 230:
            is_race_on = False
            win = cur_turtle.pencolor()
            break
        random_distance = random.randint(0, 10)
        cur_turtle.forward(random_distance)

if win == user_bet:
    print(f"Your bet is {user_bet}. You've won! The {win} turtle is the winner!")
else:
    print(f"Your bet is {user_bet}. You've lost! The {win} turtle is the winner!")

screen.exitonclick()
