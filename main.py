import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from road import Road

screen = Screen()
screen.bgcolor("grey")
screen.setup(width=600, height=600)

turtle = Player()
road = Road()
scoreboard = Scoreboard()
screen.tracer(0.05)

car_manager = CarManager()

screen.listen()
screen.onkeypress(turtle.move_up, "Up")
screen.onkeypress(turtle.move_left, "Left")
screen.onkeypress(turtle.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.09)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    # player hits a car
    for car in car_manager.cars_left:
        if turtle.distance(car) < 22:
            game_is_on = False
            scoreboard.game_over()

    for car in car_manager.cars_right:
        if turtle.distance(car) < 22:
            game_is_on = False
            scoreboard.game_over()

    # player reaches the end
    if turtle.ycor() > 280:
        turtle.reset()
        scoreboard.update_scoreboard()
        car_manager.level_up()

screen.exitonclick()
