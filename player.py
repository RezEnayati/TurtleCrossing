from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape('turtle')
        self.set_pos()
        self.shapesize(stretch_wid=1.1, stretch_len=1.1)
        self.seth(90)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def set_pos(self):
        self.goto(STARTING_POSITION)
