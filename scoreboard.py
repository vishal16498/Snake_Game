from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write_score()
        self.penup()
        self.color("White")
        self.goto(x=0, y=310)
        self.hideturtle()
        self.game_speed = 0.1

    # prints the score on the screen

    def write_score(self):
        self.write(f"Score: {self.score}", align="center", font=("courier", 20, "bold"))

    # updates score each time called

    def score_update(self):
        self.score += 1
        self.clear()
        self.write_score()
        self.game_speed *= 0.98

    # prints game over statement on screen

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("courier", 32, "normal"))
        self.game_speed = 0.1
