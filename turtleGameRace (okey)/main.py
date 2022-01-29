from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=550, height=400)
screen.title("Turtle Race")

chosen_turtle_color = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["green", "yellow", "blue", "red", "purple", "orange"]
all_turtles = []
isnt_Race_finish = False
x = -230
y = 125
for turtle_index in range(0, 6):
    turtle = Turtle("turtle")
    all_turtles.append(turtle)
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(x=x, y=y)
    y = y - 50

if chosen_turtle_color:
    isnt_Race_finish = True

i = 0
while isnt_Race_finish:
    is_it_finish = all_turtles[i].xcor()
    if is_it_finish > 230:
        isnt_Race_finish = False
        if all_turtles[i].pencolor() == chosen_turtle_color:
            print("Your turtle has won")
        else:
            print(f"The winner is {all_turtles[i].pencolor()}, you have lost the bet.")
    random_distance = random.randint(0, 5)
    all_turtles[i].forward(random_distance)
    i = i + 1
    if i == 6:
        i = 0

screen.exitonclick()
