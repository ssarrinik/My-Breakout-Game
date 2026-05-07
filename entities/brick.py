import turtle

class Brick:

    def __init__(self, positions: tuple[int,int], color: str) -> None:
        self.brick = turtle.Turtle(visible=False)
        self.brick.color(color)
        self.brick.penup()
        self.brick.setposition(positions[0], positions[1])

    def draw_brick(self, x:int, y:int) -> None:
        self.brick.pendown()
        self.brick.begin_fill()
        self.brick.forward(x)
        self.brick.left(90)
        self.brick.forward(y)
        self.brick.left(90)
        self.brick.forward(x)
        self.brick.left(90)
        self.brick.forward(y)
        self.brick.left(90)
        self.brick.end_fill()
        self.brick.penup()

    def curr_position(self) -> tuple:
        return self.brick.pos()

    def delete_brick(self):
        self.brick.clear()