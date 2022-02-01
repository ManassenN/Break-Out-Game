from turtle import *


class Brick(Turtle):
    def __init__(self,color,position):
        super().__init__()
        self.color(color)
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=3,stretch_wid=0.7)
        self.goto(position)




