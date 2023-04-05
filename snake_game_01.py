#Without Rotation
from turtle import Turtle,Screen
import time
screen=Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.setup(600,600)
screen.tracer(0)

starting_positions=[(0,0),(-20,0),(-40,0)]
segments=[]

for position in starting_positions:
    new_segment=Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(10)
        # screen.update()
    # segments[0].left(90)







screen.exitonclick()