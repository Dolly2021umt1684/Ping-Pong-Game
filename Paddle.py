from turtle import Turtle
import random


class p_addle(Turtle):

    def __init__(self,position):
        super().__init__()
        # paddle.hideturtle() this could have worked but not an efficient way
        self.create_paddle(position)


    def create_paddle(self,position):
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.speed("fastest")
        self.setpos(position)
        # paddle.showturtle()

    def up(self):
        self.setpos(self.xcor(), self.ycor() + 20)

    def down(self):
        self.setpos(self.xcor(), self.ycor() - 20)