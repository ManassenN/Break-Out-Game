from turtle import *

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1,stretch_len=9)
        self.color('red')
        self.penup()
        self.goto(position)
        
    def move_right(self):
        new_x = self.xcor() + 100
        self.goto(new_x,self.ycor())
        
    def move_left(self):
        new_x = self.xcor() - 100
        self.goto(new_x,self.ycor())