from turtle import Turtle
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_point=10
        self.y_point=10
        self.move_speed=0.1


    def move(self):
        new_x=self.xcor()+self.x_point
        new_y=self.ycor()+self.y_point
        self.setpos(new_x,new_y)


    def rebound_y(self):
        # everytime we have to just reverse action of y and action of x will be unaffected
        self.y_point *=-1

    def rebound_x(self):
        self.x_point *=-1
        self.move_speed *=0.9
    def refresh_ball(self):
        self.home()
        self.x_point *=-1 # now we want to reverse the x direction means chance given to next player
        self.move_speed=0.1