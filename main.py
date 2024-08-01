import turtle
import Files.paddle as paddleModule
import Files.ball as ballModule
import time
import random

screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0, 0)

art = turtle.Turtle()
art.hideturtle()
art.speed(0)
art.color('white')

def draw_net():
    art.penup()
    art.goto(0, -300)
    art.setheading(90)
    for _ in range(25):
        art.pendown()
        art.forward(10)
        art.penup()
        art.forward(10)

draw_net()

paddle = paddleModule.paddle("player")
paddleAI = paddleModule.paddle("AI")
paddleAI.direction = "up"
ball = ballModule.ball()

screen.listen()
screen.onkeypress(paddle.go_down, key="Down")
screen.onkeypress(paddle.go_up, key="Up")

scoreboard = turtle.Turtle()
scoreboard.color('white')
scoreboard.hideturtle()
scoreboard.penup()

i = 0

while True:
    time.sleep(0.05)
    screen_width = screen.window_width()
    screen_height = screen.window_height()
    
    scoreboard.clear()
    scoreboard.goto(0, screen_height / 2 - 50)
    scoreboard.write(f"Player: {paddle.score}      AI: {paddleAI.score}", align="center", font=("Arial", 24, "normal"))

    paddle.tutel.goto(screen_width / 2 - 50, paddle.tutel.ycor())
    paddleAI.tutel.goto(-screen_width / 2 + 50, paddleAI.tutel.ycor())
    
    ball.move()
    paddleAI.tutel.goto(-screen_width / 2 + 50, ball.tutel.ycor())
    
    if paddle.tutel.ycor() > screen_height / 2 - 50:
        paddle.tutel.sety(screen_height / 2 - 50)
    elif paddle.tutel.ycor() < -screen_height / 2 + 50:
        paddle.tutel.sety(-screen_height / 2 + 50)
    
    if paddleAI.tutel.ycor() > screen_height / 2 - 50:
        paddleAI.tutel.sety(screen_height / 2 - 50)
    elif paddleAI.tutel.ycor() < -screen_height / 2 + 50:
        paddleAI.tutel.sety(-screen_height / 2 + 50)
    
    if i == 100:
        i = 0
        paddleAI.direction = random.choice(("up", "down"))
    else:
        i += 1
        
    if ball.tutel.ycor() > screen_height / 2 - 10 or ball.tutel.ycor() < -screen_height / 2 + 10:
        ball.yspeed *= -1
    if ball.tutel.xcor() > screen_width / 2 - 10 or ball.tutel.xcor() < -screen_width / 2 + 10:
        ball.xspeed *= -1
        if ball.tutel.xcor() > screen_width / 2 - 10:
            paddleAI.score += 1
        else:
            paddle.score += 1
        
    if ball.tutel.xcor() > screen_width / 2 - 70 and paddle.tutel.ycor() - 50 < ball.tutel.ycor() < paddle.tutel.ycor() + 50:
        ball.xspeed *= -1
    if ball.tutel.xcor() < -screen_width / 2 + 70 and paddleAI.tutel.ycor() - 50 < ball.tutel.ycor() < paddleAI.tutel.ycor() + 50:
        ball.xspeed *= -1

    screen.update()
    
screen.exitonclick()



# TODO add collision detection with ball and paddles
# TODO add score system
