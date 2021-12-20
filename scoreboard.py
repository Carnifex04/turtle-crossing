from turtle import Turtle

FONT = ("Courier Bold", 13, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(x=-250, y=270)
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align="center", font=("Courier Bold", 24, "normal"))
