from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highScore.txt") as file:
            self.high_score = int(file.read())

        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALLIGNMENT, font=FONT)

    def scored(self):
        self.score += 1
        self.undo()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highScore.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

