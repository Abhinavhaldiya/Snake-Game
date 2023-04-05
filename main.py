from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import  time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("My Snake Game")
screen.tracer(0)

snakuu=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snakuu.up,"Up")
screen.onkey(snakuu.down,"Down")
screen.onkey(snakuu.right,"Right")
screen.onkey(snakuu.left,"Left")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snakuu.move()

    #Detect collision with food.
    if snakuu.head.distance(food)<15:
        food.refresh()
        snakuu.extend()
        scoreboard.increase_score()
    #Detect collision with wall.
    if snakuu.head.xcor()>290 or snakuu.head.xcor()<-290 or snakuu.head.ycor()>290 or snakuu.head.ycor()<-290:
        # game_is_on=False
        # scoreboard.game_over()
        scoreboard.reset()
        snakuu.reset()
        
    #Detect collision with tail.

    # for segment in snakuu.segments:
        # if segment==snakuu.head:
        #     pass
        # elif snakuu.head.distance(segment)<10:
        #     game_is_on=False
        #     scoreboard.game_over()

    for segment in snakuu.segments[1:]:
        if snakuu.head.distance(segment)<10:
            # game_is_on=False
            # scoreboard.game_over()
            scoreboard.reset()
            snakuu.reset()
        
screen.exitonclick()