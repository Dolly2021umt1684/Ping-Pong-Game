from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()


    def update(self):
        self.clear()
        self.setpos(-100, 200)
        self.write(self.l_score, False, "center", ("Courier", 80, "normal"))
        self.setpos(100, 200)
        self.write(self.r_score, False, "center", ("Courier", 80, "normal"))

    def l_points(self):
        self.l_score +=1
        self.update()


    def r_points(self):
        self.r_score +=1
        self.update()


    def game_over(self):
        self.home()
        self.write("GAME OVER",False,"center",("Courier",60,"normal"))