from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, -0)]
MOVE_DISTANCE = 20
MOVE_UP = 90
MOVE_RIGHT = 0
MOVE_DOWN = 270
MOVE_LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_snake(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            num_x = self.segments[seg_num - 1].xcor()
            num_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=num_x, y=num_y)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        self.add_snake(self.segments[-1].position())

    def add_snake(self, position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.segments.append(new_snake)

    def up(self):
        if self.head.heading() != MOVE_DOWN:
            self.segments[0].setheading(MOVE_UP)

    def right(self):
        if self.head.heading() != MOVE_LEFT:
            self.segments[0].setheading(MOVE_RIGHT)

    def down(self):
        if self.head.heading() != MOVE_UP:
            self.segments[0].setheading(MOVE_DOWN)

    def left(self):
        if self.head.heading() != MOVE_RIGHT:
            self.segments[0].setheading(MOVE_LEFT)

