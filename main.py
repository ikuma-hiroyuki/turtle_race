from turtle import Screen, Turtle
import random

TURTLE_SIZE = 40
SCREEN_WIDTH = 500
SCREEN_EDGE = (SCREEN_WIDTH - (TURTLE_SIZE / 2)) / 2

screen = Screen()
screen.setup(height=400, width=SCREEN_WIDTH)
user_bet = screen.textinput(title="Make your bet.", prompt="Witch turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y_pos = 90
for turtle_index in range(len(colors)):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=SCREEN_EDGE * -1, y=y_pos)
    y_pos -= 30
    all_turtles.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

        if turtle.xcor() >= SCREEN_EDGE:
            winning_color = turtle.pencolor()
            is_race_on = False

            if user_bet == winning_color:
                print("You win!")
            else:
                print(f"You lose. Winner is {winning_color}.")

screen.exitonclick()
