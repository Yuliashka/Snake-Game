
from turtle import Turtle
ALIGMENT = "center"
FONT = ("Arial", 18, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Current score: {self.score}",  align="center", font=("Arial", 18, "normal"))
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Current score: {self.score}", align="center", font=("Arial", 18, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        # to clear the previous score before we update:
        self.clear()
        self.update_score()


