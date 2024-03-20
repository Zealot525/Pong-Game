from turtle import Turtle

class Baton(Turtle):
    def __init__(self, coordinate):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5,1)
        self.pu()
        self.goto(coordinate)
        

    def up(self):
        if self.ycor() > 250:
            self.goto(self.xcor(), 250)
        elif self.ycor() < -250:
            self.goto(self.xcor(), -250)
        else:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > 250:
            self.goto(self.xcor(), 250)
        elif self.ycor() < -250:
            self.goto(self.xcor(), -250)
        else:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
