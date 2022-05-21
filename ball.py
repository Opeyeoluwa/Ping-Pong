from turtle import Turtle
POSITION = (0, 0)


class Ball (Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.meter = 0.1
       
        
    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)
        
    def bounce_y(self):
        self.y_move *= -1

        
    def bounce_x(self):
        self.x_move *= -1
        self.meter *= 0.95
        
    def refresh(self):
        self.goto(0,0)
        self.bounce_x()
        self.meter = 0.1
        
    
        