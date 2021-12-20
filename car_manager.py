from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

        self.cars_left = []
        self.cars_right = []
        self.car_reserve_left = []
        self.car_reserve_right = []

        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 4) == 1:

            if self.car_reserve_left or self.car_reserve_right:
                if self.car_reserve_left:
                    new_car = self.car_reserve_left.pop()
                if self.car_reserve_right:
                    new_car = self.car_reserve_right.pop()
            else:
                new_car = Turtle("square")
                new_car.shapesize(stretch_wid=1, stretch_len=2)
                new_car.color(random.choice(COLORS))
                new_car.penup()

            if random.randint(1, 2) == 1:
                new_car.setposition(x=300, y=random.randrange(-240, -50, 20))
                self.cars_right.append(new_car)
            else:
                new_car.setposition(x=-300, y=random.randrange(50, 220, 20))
                self.cars_left.append(new_car)

    def move(self):
        for car in self.cars_right:
            car.backward(self.car_speed)

        for car in self.cars_left:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
