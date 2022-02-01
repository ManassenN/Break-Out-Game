from turtle import *
from paddle import *
from brick import *
from ball import *
import time
NUMBER_OF_BRICKS = 52


# TODO Set Up The Screen
# Screen Setup
screen = Screen()
screen.setup(height = 700,width =1000)
screen.title('Break-Out-Game')
screen.bgcolor('black')
screen.tracer(0)

#TODO Build A Lower Paddle Class
paddle = Paddle((0,-330))
screen.update()

#TODO Add Functionalty To The Paddle (Left And Right)

screen.listen()
screen.onkey(paddle.move_left,'Left')
screen.onkey(paddle.move_right,'Right')

#TODO Creating The Bricks (With Different Colors)

color_palette = ['#1572A1','#FF6464','#FFE162','#7900FF']
bricks ={}


def brick_to_list(bricks, outter_loop, inner_loop, color_palette, k):
    for j in range(4):
        for i in range(13):
            bricks['brick_' + str(k)] = Brick(position=(outter_loop, inner_loop), color=color_palette[j])
            outter_loop -= 70
            k += 1
        outter_loop = 420
        inner_loop -= 20
    return list(bricks.values())


bricks = brick_to_list(bricks=bricks,outter_loop=420,inner_loop=320,k=0,color_palette=color_palette)
print(bricks[51])

#TODO Create Ball Class
ball = Ball()


game_is_on = True
while game_is_on:
    time.sleep(0.09)
    screen.update()
    ball.move()


#TODO Detect Paddle Collision With The Ball
    if paddle.distance(ball) < 100 and ball.ycor() < -299:
        ball.bounce_y()

#TODO Detect Wall Collision With The Ball
    if ball.ycor() > 320:
        ball.bounce_y()
    elif ball.xcor() > 470 or ball.xcor() < -475:
        ball.bounce_x()
    elif ball.ycor() < -340:
        ball.reset_position()
#TODO Detect Bricks Collision With The Ball
    for i in range(NUMBER_OF_BRICKS):
        if ball.distance(bricks[i])<28:
            bricks[i].hideturtle()
            ball.bounce_y()


#TODO Create Score Board
#


screen.exitonclick()