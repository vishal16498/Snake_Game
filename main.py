from turtle import Screen
import time
from snake import Snake
from scoreboard import Scoreboard
from food import Food

SCREEN_COLOR = "black"
screen_width = 800
screen_height = 700
screen = Screen()

screen.title("Welcome to Snake Game")
screen.bgcolor(SCREEN_COLOR)
screen.setup(width=screen_width, height=screen_height)
screen.tracer(0)
snake = Snake()
score = Scoreboard()
food = Food()

score.write_score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.08)
    snake.move_snake()
    # food refresh and score update
    if snake.snakes[0].distance(food) < 15:
        food.refresh()
        score.score_update()
        snake.extend_snake()

# tail collision
    for piece in snake.snakes[1:]:
        if snake.snakes[0].distance(piece) < 10:
            game_over = True
            score.game_over()

# wall collision
    if snake.snakes[0].xcor() > 390 or snake.snakes[0].ycor() > 340 or \
            snake.snakes[0].xcor() < -390 or snake.snakes[0].ycor() < -340:
        game_over = True
        score.game_over()


screen.exitonclick()
