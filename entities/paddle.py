import turtle

class Paddle:

    def __init__(self) -> None :
        self.paddle = turtle.Turtle(visible=False)
        self.paddle.color("#00F5FF")
        self.paddle.penup()
        self.paddle.setposition(-100, -250)

    def draw_paddle(self) -> None:
        self.paddle.pendown()
        self.paddle.begin_fill()
        self.paddle.forward(50)
        self.paddle.circle(8, extent=180)
        self.paddle.forward(50)
        self.paddle.circle(8, extent=180)
        self.paddle.end_fill()
        self.paddle.penup()

    def curr_position(self) -> tuple:
        return self.paddle.pos()

    def move_left(self):
        self.paddle.clear()
        self.paddle.back(5)
        self.draw_paddle()

    def move_right(self):
        self.paddle.clear()
        self.paddle.forward(5)
        self.draw_paddle()