import turtle

class paddle:
    def __init__(self,type="AI"):
        self.type = type
        self.tutel = turtle.Turtle('square')
        self.tutel.shapesize(stretch_len=1,stretch_wid=5)
        self.tutel.color('white')
        self.tutel.pu()
        self.score = 0
        if self.type != "AI":
            print("player paddle")
        
    def go_up(self):
        self.tutel.goto(y=self.tutel.ycor()+10,x=self.tutel.xcor())
    def go_down(self):
        self.tutel.goto(y=self.tutel.ycor()-10,x=self.tutel.xcor())
        