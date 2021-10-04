from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("green")
        self.speed(0)
        self.refresh()

    # creates a new food every time snake eats

    def refresh(self):
        x_position = random.randint(-250, 250)
        y_position = random.randint(-250, 250)
        self.goto(x_position, y_position)
