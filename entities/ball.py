from turtle import *

class Ball:

    def __init__(self) -> None:
        self.ball = Turtle(visible=False)
        self.ball.color("#FF4FCB")
        self.ball.penup()
        self.dx = 1
        self.dy = 4

    def curr_position(self):
        return self.ball.pos()

    def setup(self) -> None:
        self.ball.begin_fill()
        self.ball.circle(10)
        self.ball.end_fill()

    def move(self):
        self.ball.clear()
        x, y = self.ball.pos()

        self.ball.goto(x - self.dx ,y - self.dy)
        self.setup()

