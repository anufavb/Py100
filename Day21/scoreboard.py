from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.penup()
        self.setpos(0, 265)
        self.hideturtle()
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)