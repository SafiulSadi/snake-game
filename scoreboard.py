from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.txt = f"Score: {self.score}"
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color("white")

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)