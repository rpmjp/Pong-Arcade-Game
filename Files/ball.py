import turtle

class ball:
    def __init__(self):
        self.tutel = turtle.Turtle()
        self.tutel.shape("circle")
        self.tutel.color("white")
        self.tutel.penup()
        self.tutel.goto(0,0)
        self.xspeed = 10
        self.yspeed = 10
        
    def move(self):
        self.tutel.goto(self.tutel.xcor()+self.xspeed,self.tutel.ycor()+self.yspeed)