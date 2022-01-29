from turtle import Turtle

POSITION = [0, -20, -40]


class Snake:
    def __init__(self):
        self.segment_list = []
        self.snake_making()
        self.segment_head = self.segment_list[0]

    def snake_making(self):
        for pos in POSITION:
            self.segment = Turtle("square")
            self.segment.penup()
            self.segment.color("white")
            self.segment.setpos(pos, 0)
            self.segment_list.append(self.segment)

    def move(self):
        for i in range(len(self.segment_list)-1, 0, -1):
            x_cor = self.segment_list[i-1].xcor()
            y_cor = self.segment_list[i-1].ycor()
            self.segment_list[i].setpos(x_cor, y_cor)
        self.segment_head.fd(20)

    def up(self):
        if self.segment_head.heading() != 270:
            self.segment_head.setheading(90)

    def down(self):
        if self.segment_head.heading() != 90:
            self.segment_head.setheading(270)

    def right(self):
        if self.segment_head.heading() != 180:
            self.segment_head.setheading(0)

    def left(self):
        if self.segment_head.heading() != 0:
            self.segment_head.setheading(180)

    def length_increase(self):
        self.segment = Turtle("square")
        self.segment.penup()
        self.segment.color("white")
        x_cor = self.segment_list[len(self.segment_list) - 1].xcor()
        y_cor = self.segment_list[len(self.segment_list) - 1].ycor()
        self.segment.setpos(x_cor, y_cor)
        self.segment_list.append(self.segment)

    def collision_wall(self):
        if self.segment_head.xcor() > 280 or self.segment_head.xcor() < -280 or self.segment_head.ycor() > 280 or self.segment_head.ycor() < -280:
            return True

    def collision_tail(self):
        for i in range(1, len(self.segment_list)):
            if self.segment_head.position() == self.segment_list[i].position():
                return True

    def snake_refresh(self):
        for seg in self.segment_list:
            seg.goto(1000, 1000)
        self.segment_list.clear()
        self.snake_making()
        self.segment_head = self.segment_list[0]