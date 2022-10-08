import random
import turtle
from turtle import *

screen = Screen()
screen.setup(width=1000, height=800)

color_list = ['red', 'blue', 'green', 'black', 'pink', 'cyan', 'orange']

y_position = [-300, -200, -100, 0, 100, 200, 300]

is_race_on = False

all_turtle = []
for i in range(0, 7):
    tim1 = Turtle(shape="turtle")
    tim1.color(color_list[i])
    tim1.penup()
    tim1.goto(-400, y_position[i])
    all_turtle.append(tim1)

# Set begin line
begin_line = Turtle()
begin_line.color('black')
begin_line.penup()
begin_line.goto(-370, 350)
begin_line.setheading(270)
begin_line.width(5)
begin_line.pendown()
begin_line.forward(700)

finish_line = Turtle()
finish_line.color('black')
finish_line.penup()
finish_line.goto(370, 350)
finish_line.setheading(270)
finish_line.width(5)
finish_line.pendown()
finish_line.forward(700)

user_input = screen.textinput(title='Guest turtle', prompt='Which turtle will win?')
win_color = None
win_turtle = None
if user_input:
    is_race_on = True

while is_race_on:

    for each_turtle in all_turtle:

        random_distance = random.randint(0, 10)
        each_turtle.forward(random_distance)
        turtle_color = each_turtle.color()[0]
        print(f"turtle {turtle_color} at position {each_turtle.xcor()}")
        if each_turtle.xcor() > 350:
            is_race_on = False
            win_color = each_turtle.color()[0]
if user_input:
    print(f"Win turtle is {win_color} turtle")
    print(f"You guessed is {user_input}")
    if win_color == user_input:
        print('You win')
    else:
        print('You Lost')
screen.exitonclick()

