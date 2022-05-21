from turtle import Turtle
POSITION = (350, 0)

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.color("blue")
        self.shape("square")
        self.turtlesize(stretch_len= 5)
        self.penup()
        self.setheading(90)
        self.goto(position)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
