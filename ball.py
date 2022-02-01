from turtle import *

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.speed(0)
        self.penup()
        self.goto((0,0))
        self.x_move = 20
        self.y_move = 20

    def reset_position(self):
        self.goto((0,0))

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1