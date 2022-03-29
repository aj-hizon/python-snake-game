from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from design import Design
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
design_proku = Design(goto = (0, -270), text = "SNAKE GAME", font = ("Arial", 13, "bold"))
design_author = Design(goto = (0, -280), text = "-BY PROKU-", font = ("Arial", 6, "bold"))

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
       scoreboard.reset()
       snake.reset()
       

    #Detect collision with tail.
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

            
            
          





screen.exitonclick()
