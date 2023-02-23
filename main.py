import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.left, key="Left")
screen.onkeypress(fun=snake.right, key="Right")
screen.onkeypress(fun=snake.down, key="Down")

game_running = True
while game_running:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

#    DETECT COLLISION WITH WALL
    if snake.head.xcor()>280 or snake.head.xcor()< -280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_running = False
        scoreboard.game_over()

#     DETEXT COLLISION WITH THE SNAKE TAIL
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment)<10:
            game_running = False
            scoreboard.game_over()



screen.exitonclick()