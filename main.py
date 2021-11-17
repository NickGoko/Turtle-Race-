from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Choose Turtle that will win: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coordinates = [-300, -200, -100, 0, 100, 200]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-500, y=y_coordinates[turtle_index])
    all_turtles.append(new_turtle)
is_race_on = False
if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 350:
            # print(turtle.pencolor()) # to see if there is more than one color/ tie
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won the bet the {winning_color} turtle won!!")
            else:
                print(f"You have lost the bet the {winning_color} turtle won!!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        turtle.speed('fastest')


screen.exitonclick()