from turtle import Turtle
INITIAL_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT_PACE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for each_position in INITIAL_POSITION:
            self.add_snake(each_position)

    def add_snake(self, position):  # creates a new instances of snake
        snake = Turtle("square")
        snake.penup()
        snake.color("blue")
        snake.goto(position)
        self.snakes.append(snake)

    def extend_snake(self):  # extends the length of snake after eating food
        self.add_snake(self.snakes[-1].position())

    def move_snake(self):  # moves the snake by 20 paces
        for piece in range(len(self.snakes)-1, 0, -1):
            new_x_position = self.snakes[piece-1].xcor()
            new_y_position = self.snakes[piece-1].ycor()
            self.snakes[piece].goto(new_x_position, new_y_position)
        self.snakes[0].forward(MOVEMENT_PACE)

# following methods controls the snake direction with key bindings

    def up(self):
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].setheading(UP)

    def down(self):
        if self.snakes[0].heading() != UP:
            self.snakes[0].setheading(DOWN)

    def left(self):
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].setheading(LEFT)

    def right(self):
        if self.snakes[0].heading() != LEFT:
            self.snakes[0].setheading(RIGHT)
