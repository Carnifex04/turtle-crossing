from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("lime")
        self.setheading(90)
        self.penup()
        self.setposition(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        if self.xcor() > -280:
            self.setposition(x=self.xcor() - MOVE_DISTANCE, y=self.ycor())

    def move_right(self):
        if self.xcor() < 280:
            self.setposition(x=self.xcor() + MOVE_DISTANCE, y=self.ycor())

    def reset(self):
        self.setposition(STARTING_POSITION)
