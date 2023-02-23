from turtle import Turtle

MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        x_cor = 0
        for i in range(3):
            owen = Turtle(shape="square")
            owen.color("white")
            owen.penup()
            owen.setx(x=x_cor)
            x_cor -= 20
            owen.speed("fast")
            self.snake_segments.append(owen)

    # THE (POSITION) IS WHERE TO ADD A NEW SEGMENT, SO LIKE WHEN
    # THE SNAKE EATS FO
    def add_segment(self, position):
        owen = Turtle(shape="square")
        owen.color("white")
        owen.penup()
        owen.goto(position)
        owen.speed("fast")
        self.snake_segments.append(owen)

    def move(self):
        for segment_number in range(len(self.snake_segments) - 1, 0, -1):
            # in_front_cor = owen_bodyparts[body_part_num-1].position()
            new_x = self.snake_segments[segment_number - 1].xcor()
            new_y = self.snake_segments[segment_number - 1].ycor()
            self.snake_segments[segment_number].goto(new_x, new_y)
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())
