from turtle import Turtle
from random import randint


class Food:
    def __init__(self):
        super().__init__()
        self.timmy = Turtle("circle")
        self.timmy.penup()
        self.timmy.color("Blue")
        self.timmy.speed("fastest")
        self.timmy.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.refresh()

    def refresh(self):
        x = randint(-14, 14)
        y = randint(-14, 14)
        self.timmy.setpos(x*20, y*20)
