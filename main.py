import turtle
import Files.paddle as paddleModule
import Files.ball as ballModule
import time
import random

screen = turtle.Screen()
art = turtle.Turtle()

def get_screen_lengths():
    width = screen.window_width()
    height = screen.window_height()
    return (width, height)
screen.tracer(0,0)
screen.bgcolor('black')

art.goto(5,-4000)
art.lt(90)
art.ht()
art.color('white')
for _ in range(800):
    art.pd()
    art.begin_fill()
    for _ in range(2):
        art.fd(100)
        art.lt(90)
        art.fd(10)
        art.lt(90)
    art.end_fill()
    art.pu()
    art.fd(150)
    
    
paddle = paddleModule.paddle("player")
paddleAI = paddleModule.paddle()
paddleAI.direction = "up"
ball = ballModule.ball()
screen.listen()
screen.onkeypress(paddle.go_down,key="Down")
screen.onkeypress(paddle.go_up,key="Up")
i=0
scoreboard = turtle.Turtle()
scoreboard.color('white')
scoreboard.ht()
scoreboard.pu()
while True:
    time.sleep(0.05)
    scoreboard.clear()
    paddle.tutel.goto(get_screen_lengths()[0]/2-50,paddle.tutel.ycor())
    paddleAI.tutel.goto(-get_screen_lengths()[0]/2+50,paddleAI.tutel.ycor())
    ball.move()
    paddleAI.tutel.goto(-get_screen_lengths()[0]/2+50,ball.tutel.ycor())
    # if paddleAI.direction == "up":
    #     paddleAI.go_up()
    # else:
    #     paddleAI.go_down()
    if paddle.tutel.ycor() > get_screen_lengths()[1]/2+75:
        paddle.tutel.goto(paddle.tutel.xcor(),-get_screen_lengths()[1]/2-75)
    elif paddle.tutel.ycor() < -get_screen_lengths()[1]/2-75:
        paddle.tutel.goto(paddle.tutel.xcor(),get_screen_lengths()[1]/2+75)
    if paddleAI.tutel.ycor() > get_screen_lengths()[1]/2+75:
        paddleAI.tutel.goto(paddleAI.tutel.xcor(),-get_screen_lengths()[1]/2-75)
    elif paddleAI.tutel.ycor() < -get_screen_lengths()[1]/2-75:
        paddleAI.tutel.goto(paddleAI.tutel.xcor(),get_screen_lengths()[1]/2+75)
    
    if i == 100:
        i=0
        paddleAI.direction = random.choice(("up","down"))
    else:
        i+=1
        
    if ball.tutel.ycor() > get_screen_lengths()[1]/2-10 or ball.tutel.ycor() < -get_screen_lengths()[1]/2+10:
        ball.yspeed *= -1
    if ball.tutel.xcor() > get_screen_lengths()[0]/2-10 or ball.tutel.xcor() < -get_screen_lengths()[0]/2+10:
        ball.xspeed *= -1
        if ball.tutel.xcor() > get_screen_lengths()[0]/2-10:
            paddleAI.score += 1
        else:
            paddle.score += 1
        
    if ball.tutel.xcor() > get_screen_lengths()[0]/2-70 and ball.tutel.ycor() <= paddle.tutel.ycor()+50 and ball.tutel.ycor() >= paddle.tutel.ycor()-50:
        ball.xspeed *= -1
    if ball.tutel.xcor() < (get_screen_lengths()[0]*-1)/2+70 and ball.tutel.ycor() <= paddleAI.tutel.ycor()+50 and ball.tutel.ycor() >= paddleAI.tutel.ycor()-50:
        ball.xspeed *= -1

    scoreboard.write(f"Player: {paddle.score}      AI: {paddleAI.score}",align="right",font=("Arial",24,"normal"))
    scoreboard.goto(0,get_screen_lengths()[1]/2-50)
    screen.update()
screen.exitonclick()


# TODO add collision detection with ball and paddles
# TODO add score system
