from turtle import Turtle


class Road(Turtle):
    def __init__(self):
        super().__init__()
        self.middle_lane()
        self.left_lane()
        self.right_lane()

    def middle_lane(self):
        self.speed(0)
        self.hideturtle()
        self.color("yellow")
        self.penup()
        self.setposition(x=-300, y=0)

        while self.xcor() < 300:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def left_lane(self):
        self.speed(0)
        self.hideturtle()
        self.color("yellow")
        self.penup()
        self.setposition(x=300, y=-250)
        self.setheading(180)

        while self.xcor() > -320:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def right_lane(self):
        self.speed(0)
        self.hideturtle()
        self.color("yellow")
        self.penup()
        self.setposition(x=300, y=250)
        self.setheading(180)

        while self.xcor() > -320:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
