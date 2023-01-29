import time
from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scored = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")

game_running = True

while game_running:
    time.sleep(0.1)
    screen.update()
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scored.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_running = False
        scored.game_over()

    # Detect collision with wall
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_running = False
            scored.game_over()



screen.exitonclick()