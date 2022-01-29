from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_scre = int(self.high_score())
        self.penup()
        self.sety(270)
        self.pencolor("white")
        self.speed("fastest")
        self.score_board()
        self.hideturtle()

    def high_score(self):
        with open("data.txt", mode="r") as file:
            high_scr = file.read()
        return high_scr


    def score_board(self):
        self.clear()
        self.write(arg=f"SCORE : {self.score} HIGH SCORE : {self.high_scre}", move=False, align="center", font=("Arial", 15, "normal"))

    def score_increase(self):
        self.score += 1
        self.clear()
        self.write(arg=f"SCORE : {self.score} HIGH SCORE : {self.high_scre}", move=False, align="center", font=("Arial", 15, "normal"))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="GAME OVER", move=False, align="center", font=("Arial", 15, "normal"))

    def refresh_score(self):
        self.clear()
        if self.score > (self.high_scre):
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
            self.high_scre = int(self.high_score())
            self.score = 0
            self.write(arg=f"SCORE : {self.score} HIGH SCORE : {self.high_scre}", move=False, align="center",font=("Arial", 15, "normal"))





